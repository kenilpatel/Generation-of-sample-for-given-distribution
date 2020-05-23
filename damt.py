import sys
import random
import math


seed=int(input("Enter seed value:"))

#-----------------------------------------------------------------------------------------------------------------#

def bernoulli(p):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=random.random()
		if(rn<p):
			random_data.append(1)
		else:
			random_data.append(0)
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",p)
	print("Population variance",p*(1-p))

#-----------------------------------------------------------------------------------------------------------------#

def binomial(p,n1):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		x=0
		for i in range(0,n1):
			rn=random.random()
			if(rn<p):
				x=x+1 
		random_data.append(x)
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",n1*p)
	print("Population variance",n1*p*(1-p))

#-----------------------------------------------------------------------------------------------------------------#

def geometric(p):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		x=1
		while(random.random()>p):
			x=x+1
		random_data.append(x)
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",1/p)
	print("Population variance :",(1-p)/(p*p))

#-----------------------------------------------------------------------------------------------------------------#

def negbinomial(k,p):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	
	for i in range(0,n):
		nk=0
		trial=0
		while(nk!=k):
			rn=random.random()
			if(rn<p): 
				nk=nk+1
			trial=trial+1 
		random_data.append(trial)
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",k/p)
	print("Population variance :",(k*(1-p))/(p*p))

#-----------------------------------------------------------------------------------------------------------------#

def poisson(Lambda):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=random.random()
		i=0
		e=2.71828
		cdf=e**(-Lambda)
		while(rn>cdf):
			cdf=cdf+(e**(-Lambda))*(Lambda**i)/math.gamma(i+1)
			i=i+1
		random_data.append(i)
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",Lambda)
	print("Population variance :",Lambda)

#-----------------------------------------------------------------------------------------------------------------#

def arbdiscrete(probability):
	n1=len(probability)
	expectation=0
	var=0
	for i in range(0,n1):
		expectation=expectation+i*probability[i]
	for i in range(0,n1):
		var=var+((i-expectation)**2)*probability[i]
	rangep=[]
	rangep.append(0)
	
	for i in range(0,n1):
		if i==0:
			rangep.append(probability[0])
		else:
			rangep.append(rangep[len(rangep)-1]+probability[i]) 
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=random.random()
		i=0
		while(rn>rangep[i+1]):
			rn=random.random()
			i=i+1
		random_data.append(i) 
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",expectation)
	print("Population variance :",var)

#-----------------------------------------------------------------------------------------------------------------#

def uniform(a,b):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=a+(b-a)*random.random()
		random_data.append(rn)
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",(a+b)/2)
	print("Population variance :",(b-a)*(b-a)/12)

#-----------------------------------------------------------------------------------------------------------------#

def exponential(Lambda):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=(-1/Lambda)*math.log(random.random())
		random_data.append(rn)
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean) 
	print("sample variance :",sample_variance) 
	print("Population mean : ",1/Lambda) 
	print("Population variance :",1/(Lambda*Lambda))

#-----------------------------------------------------------------------------------------------------------------#

def gamma(alpha,Lambda):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	for i in range(0,n):
		rn=0
		for j in range(0,alpha):
			rn=rn+(-1/Lambda)*math.log(random.random())
		random_data.append(rn)
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",alpha/Lambda)
	print("Population variance :",alpha/(Lambda*Lambda))

#-----------------------------------------------------------------------------------------------------------------#

def normal(mue,sigma):
	random_data=[]
	data=[]
	random.seed(seed)
	n=int(sys.argv[1])
	if (n%2==0):
		x=int(n/2)
		for i in range(0,x):
			u1=random.random()
			u2=random.random()
			z1=((-2)*math.log(u1))**0.5
			z1=z1*math.cos(2*math.pi*u2)
			z2=((-2)*math.log(u1))**0.5
			z2=z2*math.cos(2*math.pi*u2)
			x=mue+sigma*z1
			y=mue+sigma*z2
			random_data.append(x)
			random_data.append(y) 
	else:
		x1=int(n/2)+1  
		for i in range(0,x1):
			u1=random.random()
			u2=random.random()
			z1=((-2)*math.log(u1))**0.5
			z1=z1*math.cos(2*math.pi*u2)
			z2=((-2)*math.log(u1))**0.5
			z2=z2*math.cos(2*math.pi*u2)
			x=mue+sigma*z1
			y=mue+sigma*z2
			if(i!=x1-1): 
				random_data.append(x)
				random_data.append(y)
			else:
				random_data.append(x) 
	'''print("\n")
	print(random_data)
	print("\n\n")'''
	sample_mean=sum(random_data)/n
	data=list(map(lambda x: (x-sample_mean)**2 ,random_data))  
	sample_variance=sum(data)/(n-1)
	print("sample mean : ",sample_mean)
	print("sample variance :",sample_variance)
	print("Population mean : ",mue)
	print("Population variance :",sigma**2) 

#-----------------------------------------------------------------------------------------------------------------#


if (sys.argv[2]=="bernoulli"):
	p=float(sys.argv[3])
	bernoulli(p)
elif(sys.argv[2]=="binomial"): 
	n=int(sys.argv[3])
	p=float(sys.argv[4])
	binomial(p,n)
elif(sys.argv[2]=="geometric"): 
	p=float(sys.argv[3])
	geometric(p)
elif(sys.argv[2]=="neg-binomial"): 
	k=int(sys.argv[3])
	p=float(sys.argv[4])
	negbinomial(k,p)
elif(sys.argv[2]=="poisson"):
	print("poisson")
	Lambda=float(sys.argv[3])
	poisson(Lambda)
elif(sys.argv[2]=="arb-discrete"):
	probability=[]
	for i in range(3,len(sys.argv)):
		probability.append(float(sys.argv[i]))
	arbdiscrete(probability) 
elif(sys.argv[2]=="uniform"):
	print("uniform")
	a=float(sys.argv[3])
	b=float(sys.argv[4])
	uniform(a,b)
elif(sys.argv[2]=="exponential"):
	print("exponential")
	Lambda=float(sys.argv[3])
	exponential(Lambda)
elif(sys.argv[2]=="gamma"):
	print("gamma")
	alpha=int(sys.argv[3])
	Lambda=float(sys.argv[4])
	gamma(alpha,Lambda)
elif(sys.argv[2]=="normal"): 
	mue=float(sys.argv[3])
	sigma=float(sys.argv[4])
	normal(mue,sigma)
else:
	print("enter proper name of distribution")
