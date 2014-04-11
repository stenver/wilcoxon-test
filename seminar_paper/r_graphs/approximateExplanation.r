
pihta <- c(0, 0, 2, 3, 9, 12, 21, 26, 30, 35, 41, 46, 54, 59, 67, 74, 82, 89, 97, 106, 116, 125, 133, 144, 154, 163, 173, 184, 196, 207, 219, 230, 242, 255, 267, 280, 292, 305, 319, 332, 346, 361, 375, 390, 404, 419, 435, 450, 466, 481)

#X11.options(type="nbcairo")
plot(pihta, type="o", col="blue", ylim=c(0, 1300), xlab = "N", ylab="K")

title(main="P = 0 and P approximate tail comparisson")
leg <- c("P approximate error < 5%")
cols <- c("red")
legend(0, 1300, leg, cex = 1, cols, pch=22, lty=1:2)
