
first <- c(125, 115, 130, 140, 140, 115, 140, 125, 140, 135)
second <- c(110, 122, 125, 120, 140, 124, 123, 137, 135, 145)

t1 <- wilcox.test(first, second)

ma <-  matrix(c(first, second), 2, 10)


library(RcppWilcoxonTest)

t2 <- RcppWilcoxonTest::WilxTest(ma, 0, 1)
