#Wilcoxon Signed-rank test

##This readme might be outdated, as this project is in active development

This project is an implementation of Wilcoxon signed-rank test.

For more information about the test, read:
http://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test

The goal of this project is to create a C++ library that can be run from R statistics program and terminal. The library should be able to run tens of thousands of Wilcoxon Signed Ranked Tests in in mere seconds. It should also be able to run these tests relatevly accurately, regardless of the sample size(The number of pairs) and take into account that some test might be missing or flawed. The library is developed for BIIT(Bioinformatics, Algorithmics and Data mining group). BIIT is joint research group between the Department of Computer Science (University of Tartu), Quretec, and the Estonian Biocenter. Its main research topics and capabilities include the gene regulation, gene expression data analysis, biological data mining and others.

The repository contains a number of folders.

##WilcoxonTestLibrary
Implementation of the wilcoxon test shared library. Since this is a shared library, not an executable, you cannot run it. However, you can install (and create new) interfaces for it, some of which are available in this project. The library can be installed by going to the folder and running:
```
>make install
```

After installing, you can run tests of the project with the command:
```
>make test
```

##RcppWilcoxonTest
An interface that connects the implementation of the optimized Wilcoxon algorithm to the R.
Note that you must have installed the implementation to use it.

You need [Rcpp](http://cran.r-project.org/web/packages/Rcpp/index.html) packages for R to use it.

To install Rcpp, open R console and run:

```
$install.packages("Rcpp")
```

After that, the R wilcoxon package can be installed by navigating to the package folder in the terminal and running the command:

```
$R CMD INSTALL .
```

You can now load the library in R by calling:

```
>library('RcppWilcoxonTest')
```

you can invoke the function by calling:

```
>RcppWilcoxonTest::WilxTest(dataMatrix, dataXsize, dataYsize, testIndexes, controlIndexes)
```

##TerminalWilcoxonTest
An interface that connects the implementation Wilcoxon library to the terminal.

Note that you must have installed the implementation to use it.

The interface can be compiled by going to the folder and running

```
$make
```

You can then run

```
$WilcoxonTest --help
```

for further help. Currently only supports NetCDF file as input data.

##WilcoxonVTable
Python program that can calculate V and P tables, print them, create files of the tables and create a number of graphs on the tables. These methods were mostly made for caulculations and research and are not structured very well, nor meant to be used publicly. Use them at your own risk.

##Seminar_paper
The folder that contains this paper and all images attached to it. It also contains R programs to create those images.

For any suggestions, send me a message.
