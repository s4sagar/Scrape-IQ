# coding: utf-8

import socket
import smtplib
import unicodedata
import unidecode
import psycopg2
import time
import thread
import sys
import json
import requests
import dns.resolver

# New york Restaurants
import linkedin_nyc_restaurants


all_valid_emails = []
idx = 0
	
def validate_domain():
	global idx
	curr_idx = idx
	idx = idx + 1

	global all_valid_emails
	domain_name = linkedin_nyc_restaurants.domain_names[curr_idx]
	
	# Remove initial http://
	if '//' in domain_name:
		domain_name=domain_name.split('//')[1]
	
	if 'www.' in domain_name:
		domain_name=domain_name.split('www.')[1]

	if domain_name.count('.') > 1:
		#subdomain.domain.com
		domain_name = domain_name.split('.')[1]

	# Remove / paths
	if domain_name.count('/') > 0:
		domain_name = domain_name.split('/')[0]

	print 'validating curr_idx=', curr_idx, domain_name
	
	emails = [
		'owner@'+domain_name,
		'manager@'+domain_name,
		'operations@'+domain_name,
		'gm@'+domain_name,
		'team@'+domain_name,
		'staff@'+domain_name,
		'contact@'+domain_name,
		'info@'+domain_name,
		'contactus@'+domain_name,
		'comments@'+domain_name,
		'sales@'+domain_name,
		'hello@'+domain_name,
		'desk@'+domain_name,
		'general@'+domain_name,
		'office@'+domain_name,
		'hey@'+domain_name,
		'howdy@'+domain_name,
		'feedback@'+domain_name,
	]
	passall_email = 'askjdbsahflansdflgsadjklnahsdb123yt21uiy4t2i13yiu12@'+domain_name
	valid_emails = []

	try:
		#get the MX record for the domain
		records = dns.resolver.query(domain_name, 'MX')
		mxRecord = records[0].exchange
		mxRecord = str(mxRecord)
	except:
		print 'DNS Failed for '+domain_name
		try:
			records = dns.resolver.query('www.'+domain_name, 'MX')
			mxRecord = records[0].exchange
			mxRecord = str(mxRecord)

		except:
			print 'DNS Failed for '+domain_name

	try:
		#Step 3: ping email server
		#check if the email address exists

		# Get local server hostname
		host = socket.gethostname()
		# SMTP lib setup (use debug level for full output)
		server = smtplib.SMTP()
		server.set_debuglevel(0)

		# SMTP Conversation
		server.connect(mxRecord)
		server.helo(host)
		server.mail('me@domain.com')

		code, message = server.rcpt(str(passall_email))
		# print 'Rcpt success for : '+passall_email+' '+str(code)
		# 250 is Success
		if code == 250:
			print 'CATCHALL for + '+domain_name
			valid_emails.append('info@'+domain_name)
			# if catchall just check info@

		else:
			for email in emails:
				# print '\nTrying '+email
				code, message = server.rcpt(str(email))
				if code == 250:
					valid_emails.append(email)
					break

			# Try with exec names
			# Remove European Characters
			clean_first_name = unicodedata.normalize('NFD', linkedin_nyc_restaurants.executive_first_names[curr_idx]).encode('ascii', 'ignore')
			clean_last_name = unicodedata.normalize('NFD', linkedin_nyc_restaurants.executive_last_names[curr_idx]).encode('ascii', 'ignore')

			first_name_exec = clean_first_name+'@'+domain_name
			last_name_exec = clean_last_name+'@'+domain_name
			first_last_name_exec = clean_first_name+'.'+clean_last_name+'@'+domain_name
			first_init_last_exec = str(clean_first_name[0])+clean_last_name+'@'+domain_name
			first_last_init_exec = clean_first_name+str(clean_last_name[0])+'@'+domain_name

			# print '\nTrying '+first_name_exec
			for email in [first_name_exec, last_name_exec, first_last_name_exec, first_init_last_exec, first_last_init_exec]:
				code, message = server.rcpt(str(email))
				if code == 250:
					valid_emails.append(email)
					break

			server.quit()
	except:
		print 'SMTP Failed for '+domain_name
	print '\n'+linkedin_nyc_restaurants.company_names[curr_idx]+' : '
	print valid_emails
	all_valid_emails.append(valid_emails)


def find_email_thread():
	while idx<len(linkedin_nyc_restaurants.domain_names):
		validate_domain()
		sys.stdout.flush()


# def find_emails():
# 	# Create two threads as follows
# 	try:
# 		while idx < len(linkedin_nyc_restaurants.domain_names):
# 		   # 95 to 700 tried
# 		   thread.start_new_thread( find_email_thread, () )
		   
	   
# 	except:
# 	   print "Error: unable to start thread"

def print_as_csv():
	print '_________'
	print json.dumps(all_valid_emails)
	# print len(all_valid_emails)
	print '_________'

	for i in range(len(all_valid_emails)):
		# print 'i= '+str(i)
		if len(all_valid_emails[i]) > 0:
			for j in range(len(all_valid_emails[i])):
				# print 'j= '+str(j)
				print '"'+linkedin_nyc_restaurants.executive_first_names[i]+'",'+'"'+linkedin_nyc_restaurants.company_names[i],'",'+all_valid_emails[i][j]

if __name__=="__main__":
	find_email_thread()
	print_as_csv()
	# try:
		# thread.start_new_thread( find_email_thread, () )
		# time.sleep(60)
		# thread.start_new_thread( find_email_thread, () )
		# time.sleep(60)
		# thread.start_new_thread( find_email_thread, () )
		# time.sleep(60)
		# thread.start_new_thread( find_email_thread, () )
		# time.sleep(60)
		# thread.start_new_thread( find_email_thread, () )
		# time.sleep(60)

	# 	while idx < len(linkedin_nyc_restaurants.domain_names):
	# 	   # 95 to 700 tried
	# 	   thread.start_new_thread( find_email_thread, () )
	# 	   time.sleep(1800)
	   
	# except:
	#    print "Error: unable to start thread"

