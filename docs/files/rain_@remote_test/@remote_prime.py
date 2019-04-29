from rain.client import Client,remote
import operator
import json
import profile
import pstats
def is_prime(n):
	if n <= 1:
		return False
	if n % 2 == 0:
		return False
	for i in range(3, n//2 + 1,2):
		if n % i == 0:
			return False
	return True 

class prime():

	def __init__(self):
		self.prime_str="2"
	'''
	@remote()
	def append(self,ctx,n):
		for i in range(3,n,2):
			if is_prime(i):
				self.prime_lists.append(i)
		byte = json.dumps(self.prime_lists)
		return byte
	'''

@remote()
def append(ctx,input,n):
	for i in range(3,n,2):
		if is_prime(i):
			input.prime_str=input.prime_str + " " + str(i)
	byte = json.dumps(input.prime_str)
	return byte
client = Client("localhost",7210)
'''
def append1(input,n):
	for i in range(3,n,2):
		if is_prime(i):
			input.prime_lists.append(i)
	print(input.prime_lists)
'''	

def rain():
	n = input("input n to output prime numbers in 2~n: ")
	n = int(n)
	with client.new_session() as  s:
		data = prime()
		#t = data.append(n)
		t = append(data,n)
		t.output.keep()
		s.submit()
		result=json.loads(t.output.fetch().get_bytes())
		print(result)

def main():
	rain()
		
	
		
	'''
	print("-------------vs function -------------")
	
	profile.run("append1(data,n)","""
	n = input("input n to output prime numbers in 2~n: ")
	n = int(n)
	data = prime()	
	"""
	,"result1")
	p = pstats.Stats("result1")
	p.strip_dirs().sort_stats(-1).print_stats()
	'''
		

if __name__ =='__main__':
	main()
'''	
	profile.run("main()","result.txt")
	p=pstats.Stats("result.txt")
	p.sort_stats("time").print_stats()
'''
