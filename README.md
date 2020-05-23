# Generation-of-sample-for-given-distribution

This program generate simulated samples from a giving distribution by using samples generated from a Standard Uniform Distribution (Random Number Generator).

Also display the sample mean and sample variance (calculated from the samples) and the population mean and population variance (calculated from the parameters)

The type of distribution and the parameters are given as command line arguments.Command line format issimulateDist <number-of-samples> <distribution> <parameters>

An example of a call would besimulateDist50bernoulli 0.3Here we want to generate 50separate samples of bernoullitrials where each trial has a probability of 0.3 of succeeding. The program must also calculate sample mean, sample variance, population mean and population variance.

One possible output is:Values: [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0]

Sample Mean: 0.38

Sample Variance: 0.240408163265

Population Mean: 0.3

Population Variance: 0.21 

The possible arguments(not including number of samples)are

bernoulli <p>

binomial <n> <p>

geometric <p>

neg-binomial <k> <p>

poisson <λ>

arb-discrete  <p0> <p1> <p2> ... <pn>

uniform <a> <b>

exponential <λ>

gamma <α> <λ>

normal <μ> <σ>

How to compile program?

In order to compile code just write [python damt.py] and required command line arguments.

format for command line is - python damt.py <number-of-samples> <distribution> <parameters>

after succesfull compilation of program program will ask you to input seed value and on the basis of that seed value,random value will be generated.


Libraries used 


sys - This library is used to take command line argument

random - This library is used to generate random values 

math - This library is used to calculate cos and sin value that is used in box-muller and a gamma value and log value

