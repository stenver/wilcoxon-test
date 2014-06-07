x = c(3, 7, 12)
y = c(1, 3, 5)
ma = rbind(x, y)
print("R wilcoxon: ") 
print(wilcox.test(x, y, paired = TRUE)$p.value)
print("RcppWilcoxon: ")
print(RcppWilcoxonTest::WilxTest(ma, testIndexes = 0, controlIndexes = 1))

