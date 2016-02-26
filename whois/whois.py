import sys
import requests
var=1
#site = raw_input('Enter a website name: ')
site = sys.argv[1]
print site
result=requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService?domainName=%s&outputFormat=json"%(site))
json_data=result.json()
def main():

	try:
			
		
		city1=json_data['WhoisRecord']['registrant']['city']
		state1=json_data['WhoisRecord']['registrant']['state']
		email1=json_data['WhoisRecord']['registrant']['email']
		print"""
	 	city1:%s
	 	state1:%s
	 	email1:%s
		"""%(city1,state1,email1)


		print "name:administrative contact"
		city2=json_data['WhoisRecord']['administrativeContact']['city']
		state2=json_data['WhoisRecord']['administrativeContact']['state']
		email2=json_data['WhoisRecord']['administrativeContact']['email']

		print"""
	 	city2:%s
	 	state2:%s
	 	email2:%s
		"""%(city2,state2,email2)

	except:
		  print json_data["ErrorMessage"]["msg"]

if __name__ == '__main__':
	main()	  