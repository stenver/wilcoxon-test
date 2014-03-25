#ifndef WILCOXONPARALLELTESTS_H
#define WILCOXONPARALLELTESTS_H
#include <fstream>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <cstring>
#include <gsl/gsl_cdf.h>

using namespace std;

struct approximatePosition {
    int x;
    double y;
};

class WilcoxonTest {
public:
    WilcoxonTest(float * _data, int _dataXsize, int _dataYsize, string _testIndexes, string _controlIndexes);
    WilcoxonTest(float * _data, int _dataXsize, int _dataYsize, vector<int> * _testIndexes, vector<int> * _controlIndexes);
	vector<double> * test();
private:

    //Variables
    int dataYsize;
    int dataXsize;
    float * data;
    vector<double> * pValues;
    string netCdfFileName;
    vector<int> * testIndexes;
    vector<int> * controlIndexes;
    std::vector<std::vector<approximatePosition> * > * approximatePTable;

    //Set up
    void readNetCdfFile(string dataName, string xDimension, string yDimension);
    std::vector<approximatePosition> * getPositions(string positionsLine);
    std::vector<string> * splitLine(string inputString, char lineSplit = ';');
    void readApproximatePtable();
    vector<int> * parseIntString(string input);

    //Wilcoxon Test main methods
    float calculateWValue(int yIndex, float * absoluteValues, float * signs);
    double calculatePValue(float w, int numberOfZeroes);
    float calculateZValue(float w, int Nr);

    //Wilcoxon Test helper methods
    double getApproximatePValue(float w);
    double approximateP(float w, approximatePosition beginningPos, approximatePosition endPos);
    float * rankThePairs(int yIndex, float * absoluteValues);
    int getSign(float value);
    int getNumberOfZeroes(int yIndex, float * absoluteValues);
    
    //sorting
    void quicksort(int m, int n, float * absoluteValues, float * signs);
    void swap(float * x, float * y);
    int choose_pivot(int i, int j );
};

#endif
