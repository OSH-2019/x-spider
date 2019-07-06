from rain.client import Client,remote,blob
import operator
import json
import profile
import random
import pstats

def random1():
	fo = open("data.txt","w+")
	for i in range(0,20):
		data = round(random.uniform(0,100),3)
		str_list = str(data)+","
		fo.write(str_list)
	data = round(random.uniform(0,100),3)
	str_list = str(data)
	fo.write(str_list)
	fo.close()

@remote() 
def get_average(ctx,data):
	#data = data.load()
	number = data.split(",")
	__sum  = 0.0
	__length = len(number)
	for i in range(0,__length):
		__num = float(number[i])
		__sum = __sum + __num
	__average =round(__sum / __length,3)
	bytes=json.dumps(str(__average))
	return bytes

client = Client("localhost",7210)
		
		
def rain():
	
	
	random1()
	fo = open("data.txt","r")
	with client.new_session() as  s:
		
		data = fo.read()
		print(data.replace(",","\n"))
		#data = blob(data)
		t2= get_average(data)
		t2.output.keep()
		s.submit()
		bytes=t2.output.fetch().get_bytes()
		result=json.loads(bytes)		
		print("average is %s"%result)
	fo.close()

def main():
	profile.run("rain()","pro.txt")
	option =input("check the runtime? y/n? ")
	if operator.eq(option,"y"):
		p=pstats.Stats("pro.txt")
		p.sort_stats(-1).print_stats()
		


if __name__ =='__main__':
	main()
