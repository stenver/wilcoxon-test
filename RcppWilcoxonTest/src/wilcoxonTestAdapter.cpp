#include <WilcoxonTest.h>

#include <gsl/gsl_cdf.h>
#include <Rcpp.h>

#include <iostream>
#include <exception>

using namespace std;


RcppExport SEXP wilcoxonTestAdapter(
  SEXP dataMatrix,
  SEXP testIndexes,
  SEXP controlIndexes) {
BEGIN_RCPP
  try{
    Rcpp::NumericMatrix rccpData(dataMatrix);
    Rcpp::NumericVector rccpTestIndexes(testIndexes);
    Rcpp::NumericVector rccpControlIndexes(controlIndexes);
    std::vector<float> dataVector = Rcpp::as<std::vector<float> >(rccpData);
    float* _data = &dataVector[0];
    int _dataXsize = rccpData.ncol();
    int _dataYsize = rccpData.nrow();
    std::vector<int> _testIndexes = Rcpp::as<std::vector<int> >(rccpTestIndexes);
    std::vector<int> _controlIndexes = Rcpp::as<std::vector<int> >(rccpControlIndexes);

    WilcoxonTest wilx(_data, _dataXsize, _dataYsize, &_testIndexes, &_controlIndexes);

    std::vector<double> * pValues = wilx.test();

    Rcpp::NumericVector results( pValues->begin(), pValues->end() );

    return results;

  }catch(exception& e)
  {
    std::cout << "Error" << std::endl;
    std::cout << e.what() << std::endl;
    return R_NilValue;
  }
END_RCPP
}
