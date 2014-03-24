# Testing the power of paired tests
# We generate data from shifted normal distributions and
# measure how the power of different tests depends on
# - the sample size (n)
# - the shift between distributions (delta)

X11.options(type="nbcairo")

# Example run
n <- 100
delta <- 1


x <- rnorm(n, mean = 0, sd = 1)
y <- rnorm(n, mean = delta, sd = 1)


# T-test versus W-test
p <- t.test(x, y, paired = TRUE)$p.value
q <- wilcox.test(x, y, paired = TRUE)$p.value

# W-test is much more conservative and gives out larger p-value
# It is inevitable, since it works under less constrained assuptions
# We can now ask what is the power of both tests
# - What is the probability that p-value is below rejection threshold
#
# Lets compute it empirically by simulation lots of data

p <- rep(NA, 1000)
q <- rep(NA, 1000)
for(i in c(1:1000)){
	x <- rnorm(n, mean = 0, sd = 1)
	y <- rnorm(n, mean = delta, sd = 1)
	p[i] <- t.test(x, y, paired = TRUE)$p.value
	q[i] <- wilcox.test(x, y, paired = TRUE)$p.value
}

# Now we can compute rejection probability for different thresholds
alpha <-0.05/c(1, 10, 100, 1000, 10000)

r <- rep(NA, 5)
s <- rep(NA, 5)
for(i in seq_along(alpha)){
	r[i] <- sum(p < alpha[i])/length(p)
	s[i] <- sum(q < alpha[i])/length(q)
}

# Lets do the corresponding plot
plot(factor(alpha), r, type="p", ylim=c(0.9, 1.0))
points(factor(alpha), s, col="red")

# As you can see the power of w-test is smaller when the rejection threshold is
# smaller --- The difference between T and W test becomes more pronounced when
# we do many tests in parallel and  use Bonferroni correction

# You should do the same graph for your implementation
# - Paired T-test
# - GNU R W-test (exact)
# - Your W-test using the standard approximation
# - Your W-test with exact computation
# - Your W-test with tuned approximation




