#Program to find the Probability of k>n(some number) in a poisson distribution.
import math as m
def fac(n): return 1 if n == 0 else n*fac(n-1)
lmbda=int(input("Enter the mean of Distribution:"))
print("The probability of k exceeding n is:",1-sum([(lmbda**i)/fac(i) for i in range(int(input("Enter a number(n):"))+1)])*m.exp(-lmbda))