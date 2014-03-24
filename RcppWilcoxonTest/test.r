
first <- c(125, 115, 130, 140, 140, 115, 140, 125, 140, 135)
second <- c(110, 122, 125, 120, 140, 124, 123, 137, 135, 145)

t1 <- wilcox.test(first, second)

#2 -2
#1 -1
#-5 5
#53 -53
#9 -9


ma <-  matrix(c(first, second), 1, 20)


library(RcppWilcoxonTest)

t2 <- RcppWilcoxonTest::WilxTest(ma, c(0:9), c(10:19))
