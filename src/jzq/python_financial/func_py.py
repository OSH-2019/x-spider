import math
def is_prime(n):
	if n <= 1:
		return False
	if n % 2 == 0:
		return False
	k = int(math.sqrt(n))+1;
	for i in range(3, k,2):
		if n % i == 0:
			return False
	return True 

class prime():

	def __init__(self):
		self.prime_str="2"
	

	def append(self,n):
		for i in range(3,n,2):
			if is_prime(i):
				self.prime_str=self.prime_str + " " + str(i)

def main():
	n= input("prime number in 2~n: ")
	n = int(n)
	p = prime()
	p.append(n)
	print(p.prime_str)

if __name__=="__main__" :
	main()


