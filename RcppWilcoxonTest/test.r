x <- c(125, 115, 130, 140, 140, 115, 140, 125, 140, 135)
y <- c(110, 122, 125, 120, 140, 124, 123, 137, 135, 145)
ma <-  matrix(c(x, y), 2, 10)

wilxResult = wilcox.test(x, y, exact = TRUE, paired = TRUE, alternative = "greater")$p.value
rcppResult = RcppWilcoxonTest::WilxTest(ma, testIndexes = 0, controlIndexes = 1)
cat("R wilcoxon: ", wilxResult, " and RcppWilcoxon: ", rcppResult,  "\n")

###########################################

x <- c(125, 115, 140, 115, 140, 125, 140, 135)
y <- c(110, 122, 120, 124, 123, 137, 135, 145)
ma <-  matrix(c(x, y), 2, 8)
wilxResult = wilcox.test(x, y, paired = TRUE, alternative = "greater")$p.value
rcppResult = RcppWilcoxonTest::WilxTest(ma, testIndexes = 0, controlIndexes = 1)
cat("R wilcoxon: ", wilxResult, " and RcppWilcoxon: ", rcppResult,  "\n")

############################################

x = c(3, 7, 12)
y = c(1, 3, 5)
ma = rbind(x, y)
wilxResult = wilcox.test(x, y, paired = TRUE, alternative = "greater")$p.value
rcppResult = RcppWilcoxonTest::WilxTest(ma, testIndexes = 0, controlIndexes = 1)
cat("R wilcoxon: ", wilxResult, " and RcppWilcoxon: ", rcppResult,  "\n")

###########################################

#p = 120
#a = rnorm(p)
#b = rnorm(p) + 2
#n = 20000
#pv = rep(NA, n)
#t1 = proc.time()[3]
#for(i in 1:n){
#  pv[i] = wilcox.test(a, b, paired = TRUE, exact = TRUE)$p.value
#}
#t2 = proc.time()[3]
#t2 - t1
#
#ma = rbind(a, b)
#le = rbind(a, b)
#for(i in 1:n){
#  le = rbind(le, ma)
#}
#
#t1 = proc.time()[3]
#RcppWilcoxonTest::WilxTest(le, c(0:19999), c(20000:39999))
#t2 = proc.time()[3]
#t2-t1
#cat("lols")
