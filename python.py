n=int(input("enter the number of elements: "))
def fibo(n):
	result=[]
	a,b=0,1
	while a<n:
		result.append(a)
		a,b=b,a+b
	return result
print fibo(n)

		
