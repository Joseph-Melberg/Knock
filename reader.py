#!/usr/bin/python
import mysql.connector
import re

import datetime 

f = open("/var/log/auth.log", "r")

reg = "(\S* \d* \S*) (\S*) .*Failed password for (?:(?:invalid user )?((?:\S*)|(?:root))) from ([\d\.]*) port (\d*) (\S*)"

mydb = mysql.connector.connect(host="10.0.0.3",user="user",passwd="pass",database="Home_Data")
mycursor = mydb.cursor()
def record(value):
    command = "INSERT INTO Home_Data.failed_access (date,target_ip,username,source_ip,port,method) VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(command,value)
    mydb.commit()
  
    print "done"
# Function to covert string to datetime 
def convert(date_time): 
    format = '%b %d  %I:%M:%S' # The format 
    now = datetime.datetime.now()
    datetime_str = datetime.datetime.strptime(date_time, '%b %d %H:%M:%S').replace(year=now.year)
    return datetime_str 
   
def find():
	line = f.readline();
	if line is None:
		exit()
#"(\S* \d* \S*) (\\S*)"
	res = re.findall(reg,line)
	for i in res:
		print res
	if(len(res)!=0):
		print line
		#print(res[0])
		result = list(res[0])

		#print(str(result[0]))
		result[0] = convert(str(result[0]))
		record(result)
while True:
	find()