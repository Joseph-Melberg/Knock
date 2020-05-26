#!/usr/bin/python
import mysql.connector
import re

import datetime 

f = open("/var/log/auth.log", "r")

reg = "(\S* \d* \S*) (\S*) .*Failed password for (?:(?:invalid user )?((?:\S*)|(?:root))) from ([\d\.]*) port (\d*) (\S*)"

mydb = mysql.connector.connect(host="10.0.0.3",user="user",passwd="pass",database="Home_Data")
mycursor = mydb.cursor()

mycursor.execute("SELECT date FROM Home_Data.failed_access ORDER BY date desc LIMIT 1")
latest_str = str(mycursor.fetchall()[0][0])
print(latest_str)
latest = datetime.datetime.strptime(latest_str,'%Y-%m-%d %H:%M:%S')


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
done = False
def find():
	line = f.readline();
	if line is '':
		done = True
		exit()
		return
	res = re.findall(reg,line)
	for i in res:
		print(i)
	if(len(res)!=0):
	#	print line
		result = list(res[0])
		result[0] = convert(str(result[0]))
		if(result[0] > latest):
			record(result)
while not done:
	find()
print("I am finished")
