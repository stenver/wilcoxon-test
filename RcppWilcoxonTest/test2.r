first <- c(125, 115, 140, 115, 140, 125, 140, 135)
second <- c(110, 122, 120, 124, 123, 137, 135, 145)

t1 <- wilcox.test(first, second, paired=TRUE, alternative='two.sided')
t2 <- wilcox.test(second, first, paired=TRUE, alternative='two.sided')


ma <-  matrix(c(first, second), 2, 8)
library(RcppWilcoxonTest)

rtest1 <- RcppWilcoxonTest::WilxTest(ma, 0, 1)
rtest2 <- RcppWilcoxonTest::WilxTest(ma, 1, 0)
