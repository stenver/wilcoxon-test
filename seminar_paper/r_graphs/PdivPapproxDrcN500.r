library('drc')



X11.options(type="nbcairo")
valuesFrame500 <- data.frame(x=c(1:124751), y=relativeValues500)

model500 <- drm(y~x, data=valuesFrame500, fct = LL.4())

plot(model500, type="o", col="blue", xlab = "K", ylab="P/Papprox * drc", ylim=c(0.0, 1.0))

title(main="P/Papprox when n == 500")