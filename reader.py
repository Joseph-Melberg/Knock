#open file
import re

import datetime 

f = open("auth.log", "r")
class entry(object):
	def __init__(self, arg):
		super(entry, self).__init__()
		self.arg = arg
reg = "(\S* \d* \S*) (\S*) .*Failed password for (?:(?:invalid user )?((?:\S*)|(?:root))) from ([\d\.]*) port (\d*) (\S*)"


   
# Function to covert string to datetime 
def convert(date_time): 
    format = '%b %d  %I:%M:%S' # The format 
    now = datetime.datetime.now()
    datetime_str = datetime.datetime.strptime(date_time, '%b %d %H:%M:%S').replace(year=now.year)
    return datetime_str 
   
def find():
	line = f.readline();
	print line
#"(\S* \d* \S*) (\\S*)"
	res = re.findall(reg,line)
	for i in res:
		print res
	if(len(res)!=0):
		print(res[0])
		print(convert(res[0][0]))
	raw_input()
while True:

	find()