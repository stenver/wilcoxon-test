#include <fstream>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <string.h>
#include <netcdfcpp.h>
#include <gsl/gsl_cdf.h>
#include <boost/random.hpp>
#include <boost/math/distributions/inverse_gaussian.hpp>
#include <boost/random/normal_distribution.hpp>
#include <boost/program_options.hpp>
#include <WilcoxonTest.h>
namespace po = boost::program_options;
using namespace std;

const string help = "help";
const string dataFileName = "dataFile";
const string configFileName = "configFile";

int dataYsize;
int dataXsize;

void commandConfigMessage()
{
        cout << "Alternatively, instead of config file, you can write configuration arguments directly to the command line, ";
        cout << "overwriting some or all the arguments. " << endl;
        cout << "Note! testIndexes and ontrolIndexes must be a Comma separated integer list _WITHOUT_ spaces!" << endl << endl;
        cout << "Example: WilcoxonTest --" << dataFileName << " data.nc ";
        cout << "--DataName data " << "--xDimension  n " << " --yDimension m ";
        cout << "--testIndexes  0,2,4,6 " << " --controlIndexes 1,3,5,7" << endl<< endl;
        cout << "Note that if both Command line config parameters and Config file is given, then the command line parameters will be used" << endl<< endl;
}

bool validateCommandLine(po::variables_map * vm, po::options_description * commandArgs)
{
    if(!vm->count(dataFileName)){
        cout << "Invalid parameters." << endl;
        cout << *commandArgs << endl;
        cout << "Example: WilcoxonTest --" << dataFileName << " data.nc --" << configFileName << " conf.cfg" << endl<< endl;

        commandConfigMessage();
        return false;
    }
    return true;
}

bool validateConfiguration(po::variables_map * vm, po::options_description * configuration)
{
    if(!vm->count("DataName") || !vm->count("xDimension") || !vm->count("yDimension")
            || !vm->count("testIndexes") || !vm->count("controlIndexes")){

        cout << "Configuration file has missing options" << endl;
        cout << *configuration << endl;
        cout << "Example: conf.cfg:" << endl;
        cout << "DataName = data" << endl;
        cout << "xDimension = n" << endl;
        cout << "yDimension = m" << endl;
        cout << "testIndexes = 0, 2, 4, 6" << endl;
        cout << "controlIndexes = 1, 3, 5, 7" << endl<< endl;

        commandConfigMessage();
        return false;
    }
    return true;
}

float * readNetCdfFile(string fileName, string dataName, string xDimension, string yDimension)
{
    NcFile file(fileName.c_str(), NcFile::ReadOnly);
    if (!file.is_valid())
    {
        cout << "Couldn't open file!\n";
        throw;
    }

    NcVar *experimentData = file.get_var(dataName.c_str());

    dataYsize = file.get_dim(yDimension.c_str())->size();
    dataXsize = file.get_dim(xDimension.c_str())->size();

    float * data = new float[dataYsize * dataXsize];;


    experimentData->get(&data[0], dataYsize, dataXsize);
    return data;
}

//TODO optimize this thing
void writeResultsFile(string dataFileName, string yDimension, vector<double> * pValues)
{
    NcFile file(dataFileName.c_str(), NcFile::ReadOnly);
    NcVar *geneNames = file.get_var("gene");
    int dataYsize = file.get_dim(yDimension.c_str())->size();

    FILE * pFile;
    pFile = fopen ("results.txt","w");

    cout << "Writing results to file.." << endl;

    int percentage = dataYsize / 10;
    int percentageCount = 10;
    for(int i = 0; i < dataYsize; i++){
        char * c = geneNames->as_string(i*28);
        std::string str;
        if(pValues->at(i) > 0.05){
            std::ostringstream strs;
            strs << pValues->at(i);
            str = strs.str();
        }else{
            str = "NA";
        }
        fprintf (pFile, "%-20s-%20s", c, str.c_str());
        fprintf (pFile, "\n");
        if(i == percentage)
        {
            cout <<  percentageCount << "% complete" << endl;
            percentageCount += 10;
            percentage += dataYsize / 10;
        }
        delete c;
    }
    fclose(pFile);
}

int main(int argc, char* argv[])
{
    po::options_description commandArgs("Command line arguments");
    commandArgs.add_options()
        (help.c_str(), "produce help message")
        (dataFileName.c_str(), po::value< string > (), "A NetCDF file containing the data that tests will be run on")
        (configFileName.c_str(), po::value< string > (), "A configuration INI file containing all the specified options under 'Configuration'")
    ;

    po::options_description config("Configuration");
    config.add_options()
        ("DataName", po::value<string>(), "Name of the data variable in NetCDF file - string")
        ("xDimension", po::value<string>(), "Name of the Y dimension of the data matrix - string")
        ("yDimension", po::value<string>(), "Name of the X dimension of the data matrix - string")
        ("testIndexes", po::value<string>(), "Test group column indexes - comma separated int array")
        ("controlIndexes", po::value<string>(), "Control group column indexes - comma separated int array")
        ;
    commandArgs.add(config);

    po::variables_map vm;
    po::store(po::parse_command_line(argc, argv, commandArgs), vm);
    po::notify(vm);

    if (!vm[help].empty()) {
        cout << commandArgs << endl;
        cout << config << endl;
        return 1;
    }
    else if (validateCommandLine(&vm, &commandArgs)) {

        //This doesnt overwrite command line parameters
        if(vm.count(configFileName)){
            std::ifstream file;
            file.open(vm[configFileName].as<string>().c_str());
            if (!file.is_open())
            {
                cerr << "Config file does not exist! " << endl;
                throw;
            }

            po::store(po::parse_config_file(file, config), vm);
            po::notify(vm);
        }

        if(validateConfiguration(&vm, &config)){
            string dataFileName = vm.at("dataFile").as<string>();
            string testIndexes = vm.at("testIndexes").as<string>();
            string controlIndexes = vm.at("controlIndexes").as<string>();
            string dataName = vm.at("DataName").as<string>();
            string xDimension = vm.at("xDimension").as<string>();
            string yDimension = vm.at("yDimension").as<string>();
            float * data = readNetCdfFile(dataFileName, dataName, xDimension, yDimension);
            WilcoxonTest wilx(data, dataXsize, dataYsize, testIndexes, controlIndexes);
            vector<double> * pValues = wilx.test();
            writeResultsFile(dataFileName, yDimension, pValues);
        }
    }
    return EXIT_SUCCESS;
}
