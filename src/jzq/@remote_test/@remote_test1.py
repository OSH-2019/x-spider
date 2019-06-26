from rain.client import Client,remote
import operator
import json
import profile
import pstats
def is_prime(n):
	if n <= 1 or isinstance(n,int)==False:
		return False
	if n % 2 == 0:
		return False
	for i in range(3, n//2 + 1,2):
		if n % i == 0:
			return False
	return True 
'''
class prime():

	def __init__(self):
		self.prime_lists=[2]

	@remote()
	def append(self,ctx,n):
		for i in range(3,n,2):
			if is_prime(i):
				self.prime_lists.append(i)
		byte = json.dumps(self.prime_lists)
		return byte
'''

@remote(auto_encode="json")
def append(ctx,n):
	prime=[];
	for i in range(n,n+100,2):
		if is_prime(i):
			prime.append(i)
	#byte = json.dumps(input.prime_lists)
	#return byte
	return prime
	
	
	
client = Client("localhost",7210)
'''
def append1(input,n):
	for i in range(3,n,2):
		if is_prime(i):
			input.prime_lists.append(i)
	print(input.prime_lists)
'''	

def rain():
	n=100000
	session = client.new_session("test", default=True)
	
	#t = data.append(n)
	tasks = [
		append(x,name="test={}".format(x))
		for x in range(1,n,100)
	]
	for task in tasks:
		task.output.keep()
	session.submit()
	#result=json.loads(t.output.fetch().get_bytes())
	result= []
	 
	for task in tasks:
		result.extend(task.output.fetch().load())
		
	print(result)

def main():
	profile.run("rain()","result.txt")
	p=pstats.Stats("result.txt")
	p.sort_stats("time").print_stats()
		
	
		
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
	rain()
