from lxml import html  
import json
import requests
from exceptions import ValueError
from time import sleep
import re,urllib
import argparse
import dns.resolver
import socket
import smtplib
import unidecode
import psycopg2
from time import sleep
import random

def parse_yelp_list_page(url):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	response = requests.get(url, headers=headers, verify=False).text
	parser = html.fromstring(response)
	# print "Parsing the page"
	restaurant_links = parser.xpath("//span[contains(@class,'biz-name')]/a/@href")
	return restaurant_links

def parse_page(url):
	# url = "https://www.yelp.com/biz/frances-san-francisco"
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	response = requests.get(url, headers=headers, verify=False).text
	parser = html.fromstring(response)
	# print "Parsing the page"
	raw_name = parser.xpath("//h1[contains(@class,'page-title')]//text()")
	raw_wbsite_link = parser.xpath("//span[contains(@class,'biz-website')]/a/@href")
	raw_phone = parser.xpath(".//span[@class='biz-phone']//text()")
	raw_address = parser.xpath('//div[@class="mapbox-text"]//div[contains(@class,"map-box-address")]//text()')
	
	
	name = u''.join(raw_name).encode('utf-8').strip()
	phone = ''.join(raw_phone).strip()
	address = ' '.join(' '.join(raw_address).split())
	#name = unidecode.unidecode(name)
	valid_emails = []

	if raw_wbsite_link:
		decoded_raw_website_link = urllib.unquote(raw_wbsite_link[0])
		website = re.findall("biz_redir\?url=(.*)&website_link",decoded_raw_website_link)[0]
		valid_emails = find_emails(website)
	else:
		website = ''
	
	data={'name':name,
		'valid_emails':valid_emails,
		'phone':phone,
		'address':address,
		'website':website
	}
	return data
	
def find_emails(domain_name):
	domain_name=domain_name.split('//')[1].split('/')[0]
	if 'www.' in domain_name:
		domain_name=domain_name.split('www.')[1]
	emails = [
		'info@'+domain_name,
		'contact@'+domain_name,
		'manager@'+domain_name,
		'sales@'+domain_name,
		'operations@'+domain_name,
		'hello@'+domain_name,
		'desk@'+domain_name
	]
	passall_email = 'askjdbsahflansdflgsadjklnahsdb123yt21uiy4t2i13yiu12@'+domain_name
	valid_emails = []

	try:
		#get the MX record for the domain
		records = dns.resolver.query(domain_name, 'MX')
		mxRecord = records[0].exchange
		mxRecord = str(mxRecord)
	except:
		print 'MX Failed'
		try:
			records = dns.resolver.query('www.'+domain_name, 'MX')
			mxRecord = records[0].exchange
			mxRecord = str(mxRecord)

		except:
			print 'DNS Failed'
			return valid_emails

	try:
		#Step 3: ping email server
		#check if the email address exists

		# Get local server hostname
		host = socket.gethostname()
		print 1
		# SMTP lib setup (use debug level for full output)
		server = smtplib.SMTP()
		server.set_debuglevel(0)
		print 2
		# SMTP Conversation
		server.connect(mxRecord)
		print 3
		server.helo(host)
		print 4
		server.mail('me@domain.com')
		print 5
		code, message = server.rcpt(str(passall_email))
		print 6
		# 250 is Success
		if code == 250:
			print 'CATCHALL'
			return valid_emails
		else:
			for i in range(0,7):
				print '\nTrying '+emails[i]
				code, message = server.rcpt(str(emails[i]))
				if code == 250:
					valid_emails.append(emails[i])
		server.quit()
	except:
		print 'SMTP Failed'
		return valid_emails	

	print valid_emails
	return valid_emails

if __name__=="__main__":
	requests.packages.urllib3.disable_warnings()

	# conn_string = "host='localhost' dbname='restaurants' user='postgres' password='LockIt'"
	# conn = psycopg2.connect(conn_string)
	# cursor = conn.cursor()

	argparser = argparse.ArgumentParser()
	argparser.add_argument('url','start','end',help = 'yelp bussiness url')
	args = argparser.parse_args()
	url = args.url
	start = args.start
	end = args.end

	print 'URL = '+url

	# for start in range (1230,3330,30): for Seattle
	for start in range (start,end,30):
		restaurant_links = parse_yelp_list_page(url+'&start='+str(start))
		print restaurant_links
	
		scraped_email_data = []
		scraped_phone_data = []

		for restaurant_link in restaurant_links:
			sleep(random.randint(20,200))
			restaurant_result = parse_page('https://yelp.com'+restaurant_link)
			# cursor.execute("INSERT INTO restaurants (name, email, phone, address, city, state, website) VALUES (%s, %s, %s, %s, 'seattle', 'WA', %s)",
			# 	(restaurant_result['name'],restaurant_result['email'],restaurant_result['phone'],restaurant_result['address'], restaurant_result['website']))
			print '\n Restaurant data: '+json.dumps(restaurant_result)
			if len(restaurant_result['valid_emails']) > 0:
				scraped_email_data.append(restaurant_result)
				print '\nEmails:  '+json.dumps(restaurant_result['valid_emails'])
			else:
				scraped_phone_data.append(restaurant_result)

	# scraped_data = parse_page(url)
	yelp_id = url.split('/')[-1]
	print 'Yelp ID: '+yelp_id
	
	with open("scraped_email_data-%s.json"%(yelp_id),'w') as fp:
		json.dump(scraped_email_data,fp,indent=4)
		# for email_obj in scraped_email_data:
		# 	fp.write(email_obj['name']+'", "'+email_obj['phone']+'", "'+email_obj['address']+'", "'+email_obj['website'])
		# 	json.dump(valid_emails,fp,indent=4)
		# 	# for valid_email in scraped_email_data['valid_emails']:
		# 	# 	fp.write(', '+valid_email)
		# 	fp.write('\n')

	with open("scraped_phone_data-%s.html"%(yelp_id),'w') as fp:
		# fp.write('<html><body><ol>')
		json.dump(scraped_phone_data,fp,indent=4)
		# for phone_obj in scraped_phone_data:
		# 	fp.write('<li>'+phone_obj['name']+' , <a href="tel:'+phone_obj['phone']+'">'+phone_obj['phone']+' , '+phone_obj['address']+' , '+phone_obj['website']+'</li>\n')
		# fp.write('</ol></body></html>')

	# conn.commit()
	# cursor.close()
	# conn.close()
	print 'Done!'