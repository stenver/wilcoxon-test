#Wilcoxon Signed-rank test

##This readme might be outdated, as this project is in active development

This project is an implementation of Wilcoxon signed-rank test. 

For more information about the test, read: 
http://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test

The goal of this project is to create a C++ library that can be run from R statistics program and terminal. The library should be able to run tens of thousands of Wilcoxon Signed Ranked Tests in in mere seconds. It should also be able to run these tests relatevly accurately, regardless of the sample size(The number of pairs) and take into account that some test might be missing or flawed. The library is developed for BIIT(Bioinformatics, Algorithmics and Data mining group). BIIT is joint research group between the Department of Computer Science (University of Tartu), Quretec, and the Estonian Biocenter. Its main research topics and capabilities include the gene regulation, gene expression data analysis, biological data mining and others.

The repository contains a number of folders.

##RcppWilcoxonTest
An interface that connects our implementation of the optimized Wilcoxon algorithm to the R. 
Note that you must have installed our implementation to use it. 
The interface must be compiled with separate R commands from the command line. 
You need Rcpp packages for R to use it. 
It can be installed in R console by running 

```$install.packages("Rcpp")```

After that, our package can be installed to R by running the command in the command line in the folder 

```$R CMD INSTALL .```

You can now load our library in R by calling 

```>library('RcppWilcoxonTest')```

and you invoke the function by calling 

```>RcppWilcoxonTest::WilxTest(dataMatrix, dataXsize, dataYsize, testIndexes, controlIndexes)```

##TerminalWilcoxonTest
An interface that connects our implementation of the optimized Wilcoxon algorithm to the R. 
Note that you must have installed our implementation to use it. 
The interface can be compiled by going to the folder and running 

```$make```

You can then run 

```$WilcoxonTest --help```

for further help. Currently only supports NetCDF file as input data.

##WilcoxonTestLibrary 
Our implementation for the optimized wilcoxon test. You library can be installed by going to the folder and running $>make install$.

##WilcoxonVTable
Python program that can calculate $V$ and $P$ tables, print them, create files of the tables and create a number of graphs on the tables.

##Seminar_paper
The folder that contains this paper and all images attached to it. It also contains R programs to create those images.

For any suggestions, send an email to Stenver1010@gmail.com