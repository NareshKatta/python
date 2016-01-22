#!/usr/bin/python

import MySQLdb
import datetime
db = MySQLdb.connect("localhost","root","sama1011","test" )

cursor = db.cursor();
cursor.execute("CREATE TABLE IF NOT EXISTS mailing (addr VARCHAR(255) NOT NULL)")

# Create a table which stores the count of email address by domain name
cursor.execute("create table if not exists addresses_count (domain varchar(255) NOT NULL, date DATE, count INT)")

sql = "select * from mailing";
cursor.execute(sql);
result = cursor.fetchall()
data = {}
for row in result:
	mail = row[0]
	array = mail.split('@')
	array[1] = array[1].replace('.', '_')
	if(data.has_key(array[1])):
		data[array[1]] = data[array[1]]+ 1;
	else:
		data[array[1]] = 1;
for key in data.keys():
	cursor = db.cursor()
	cursor.execute("insert into addresses_count values(%s, %s, %s)", (key, datetime.datetime.now().date(), data[key]));
	db.commit()


