x <- c(125, 115, 130, 140, 140, 115, 140, 125, 140, 135)
y <- c(110, 122, 125, 120, 140, 124, 123, 137, 135, 145)
ma <-  matrix(c(x, y), 2, 10)

cat("R wilcoxon: ", wilcox.test(x, y, paired = TRUE, alternative = "greater")$p.value, " and RcppWilcoxon: ", RcppWilcoxonTest::WilxTest(ma, testIndexes = 0, controlIndexes = 1), "\n")

x <- c(125, 115, 140, 115, 140, 125, 140, 135)
y <- c(110, 122, 120, 124, 123, 137, 135, 145)
ma <-  matrix(c(x, y), 2, 8)

cat("R wilcoxon: ", wilcox.test(x, y, paired = TRUE, alternative = "greater")$p.value, " and RcppWilcoxon: ", RcppWilcoxonTest::WilxTest(ma, testIndexes = 0, controlIndexes = 1), "\n")

############################################
x = c(3, 7, 12)
y = c(1, 3, 5)
ma = rbind(x, y)
cat("R wilcoxon: ", wilcox.test(x, y, paired = TRUE, alternative = "greater")$p.value, " and RcppWilcoxon: ", RcppWilcoxonTest::WilxTest(ma, testIndexes = 0, controlIndexes = 1), "\n")

