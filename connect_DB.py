#!/usr/bin/python
import psycopg2
import sys
 
def main():
	#Define our connection string
	conn_string = "host='localhost' dbname='restaurants' user='postgres' password='LockIt'"
 
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	# execute our Query
	cursor.execute("INSERT INTO restaurants (name, email, phone, address) VALUES (%s, %s, %s, %s)",("abc'def", "abc'def","abc'def","abc'def"))
	
	conn.commit()
	cursor.close()
	conn.close()
	print "Connected!\n"
 
if __name__ == "__main__":
	main()