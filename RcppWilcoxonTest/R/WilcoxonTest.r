WilxTest <- function(dataMatrix, testIndexes, controlIndexes) {

  if (missing(dataMatrix) || missing(testIndexes) || missing(controlIndexes)) {
    cat("\nOne or more parameters are missing!\n")

  }else if(length(testIndexes) != length(controlIndexes)){
    cat("\nThe test and control indexes must be of same size\n")

  }
  else if(any(testIndexes >= (length(dataMatrix) - 1)) || any(testIndexes < 0) ||
          any(controlIndexes >= (length(dataMatrix) - 1) || any(controlIndexes < 0))){
    cat("\nThe test or control indexes point to out of matrix bounds!\n")
  }
  else{
    .Call('wilcoxonTestAdapter', dataMatrix, testIndexes, controlIndexes, PACKAGE = 'RcppWilcoxonTest')
  }
}

