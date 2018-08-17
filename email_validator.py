import requests
import dns.resolver
import socket
import smtplib
import unidecode
import psycopg2


def check_emails(names, emails):
	valid_emails = []
	valid_names = []

	for i in range(0,len(emails)):
		email=emails[i]
		name=names[i]
		domain_name=email.split('@')[1]
		print '\nDomain name: '+domain_name
		passall_email = 'askjdbsahflansdflgsadjklnahsdb123yt21uiy4t2i13yiu12@'+domain_name

		try:
			#get the MX record for the domain
			records = dns.resolver.query(domain_name, 'MX')
			mxRecord = records[0].exchange
			mxRecord = str(mxRecord)
		except:
			print '\nMX Failed for '+email
			try:
				records = dns.resolver.query('www.'+domain_name, 'MX')
				mxRecord = records[0].exchange
				mxRecord = str(mxRecord)

			except:
				print '\nDNS Failed for '+email

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

			# 250 is Success
			if code == 250:
				print '\nCATCHALL for'+email

			else:
				print '\nTrying '+email
				code, message = server.rcpt(str(email))
				if code == 250:
					valid_emails.append(email)
					valid_names.append(name)
			server.quit()
		except:
			print '\nSMTP Failed for '+email

	for name in valid_names:
		print '\n'+name
	for email in valid_emails:
		print '\n'+email

	return valid_emails

if __name__=="__main__":
	names=["Ben & Jerry's","La Iguana Restaurant","Nardelli's Grinder Shoppe","El Artesano Restaurant","Le Crave","Kosher Deluxe","Bruno's Restaurant","The Mean Fiddler","Fresh Brothers","Rustic Table","Kabuki Steakhouse & Sushi","Mitchell's Restaurant","Tonys Asian Fusion Restaraunt","Coffeelands","Seven Oaks Clubhouse","Cull & Pistol","The Modern","Baci Pizza & Subs","Gotham Bar & Grill","Pure Thai Cookhouse","Toni Patisserie & Cafe","Rusty Bucket Corner Tavern","On A Roll Media","Small Town Sandwich Shop","BellaCakes","Paddy Reilly's Music Bar","Dublin Village Tavern","Louies Grill Fusion","8 Fresh","Arboreal Inn","old towne restaurant","Rita's Willingboro","Jack's Waterfront Restaurant & Lounge","J.W.'s Food & Spirits","Gemys","The Monocle","Pat O'Brien's","The Savoy Tavern","Franco Gianni's Pizza","Old Boys' Brewhouse","Beer Barrel Pizza and Grill","Muncheez","Paddy Power","Ten Asian Bistro","Nohea Cafe","Astro Doughnuts and Fried Chicken","Nasty's Sports Bar","Murray's","The Creekside Grille","Pilita Grill","Brent's Delicatessen & Restaurant","J&J's Gourmet","Christines Italian","YUME Bistro","Baum's Fine Pastries","Rappahannock Oyster Bar","Rafele","Slater's Deli and Caterers","Via Della Pace","R & R Taproom","San Remo Fine Italian Cuisine","Cha Cha's Tacos & Tequila","Rubirosa","Buns Burgers","Caliente Cantina","The Griddle Cafe","AQUAGRILL","Alchemy Restaurant & Tavern","Water Grill","One Steep at a Thyme","Osaka Japanese Restaurant","Moe's Original Bar B Que","Buca di Beppo","Patsy's Italian Restaurant","Top Butcher Shoppe and BBQ","Growler USA, America's Microbrew Pub","The Bazaar by Jose Andres","Asian Fusion","El Centro","Cora's Coffee Shoppe","Izakaya Mew","Nando's","Piezzetta","Taqueria Vista Hermosa","Johnny Rad's","Bop Brick Oven Pizza","Mr. David's","Michelle's Country Diner","Basil Thai Bistro","Chad's BBQ","Chaparral Mexican Grill","Robert","Ginger & Garlic","Italianissimo Trattoria","La Grande Orange Cafe","Gallagher's Steak House","Bacaro LA","Lazy Bean Coffee Company","Breakfast Republic","Cantina Diablo's","Basso56","Bareburger","Aliki's Greek Taverna","Patzeria Family & Friends","SUGARFISH by sushi nozawa","The Wine Market","Ernie's","Porsena","The Dead Rabbit","Southfield Pancake House","Native Grill & Wings","Pulp Juice And Smoothie Bar","Bucky's Bar-Bq-Donaldson Center","Perilla","Map of Thailand","Papa Locos Tacos and Burgers","The Blind Lion","New Wave Cafe","Frederick's Wine and Dine","Rosie's Trattoria","MidiCi The Neapolitan Pizza Company","EscoGelato","Kay's Real Pit Bar-B-Q","Bullfrog Brewery","Whits Frozen Custard","Arabica Coffee House","Casavana Cuban Cuisine","Orange Blossom Restaurant","Johnson's Cafe","Stax's Original","Greenfield's Bagels & Deli","Himmareshee Public House","Chelsea Ristorante","Cuzi Fresh Cafe","Brothers Family Restaurant","Mugsy's Hideout LLC","Curry Kitchen","Buca di Beppo","Orleans Restaurant and Bar","iBangkok Thai Restaurant","Fat Goose","Kannika's Thai Kitchen","King Donuts","Sotto le Stelle","Hibernia Bar & Grill","Siam Restaurant & Bar","Smiling Chameleon Draft House","The Corner Cafe and Restaurant","Ed's Lobster Bar","Sunny Side Up Cafe","Hala in","Morgan's Cat Cafe","Great American Health Bar","Traghaven","Joe's Pizza - Carmine St","Epicerie Boulud","Steak 'n Shake","Riegelsville Tavern","SILVIA","Gallery Bar Chicago","RosaMia Ristorante Italiano","Civano Coffee House","Anthony's Italian Coffee House"]
	emails=['benjerrylocations@gmail.com','la.iguana1@gmail.com','nardellismeriden@gmail.com','staff@ElArtesanoRestaurant.com','info@lecravecafe.com','kosher_deluxe@hotmail.com','info@brunoristoranteitaliano.com','michael@themeanfiddlernyc.com','debbie@freshbrothers.com','rustictablenyc@gmail.com','kabukisushi19@gmail.com','waffles@mitchellscocoa.com','tanyc614@aol.com','mmiller@poluscenter.org','sevenoaksclubhouse@gmail.com','candp@lobsterplace.com','info@themodernnyc.com','bacievents@gmail.com','brandon@gothambarandgrill.com','purethaicookhouse@gmail.com','info@tonipatisserie.com','keith@rdadvisors.net','onarollmedia@yahoo.com','smalltownsandwichshop@hotmail.com','kristen@bellacakes.net','paddyreillys@gmail.com','timp@columbus.rr.com','efmijangos@hotmail.com','8fresh315@gmail.com','thearborealinn@hotmail.com','oldtownerestaurant@att.net','info@ritaswillingboro.com','restaurant@higrandhaven.com','jwsghm@att.net','ffhealthyfoods@gmail.com','monocleinfo@aol.com','pobtavern@gmail.com','SavoyTavern@optonline.net','francogiannispizza@gmail.com','anni@oldboysbrewhouse.com','marketing@goodfoodrestaurants.com','nycspace.inc@gmail.com','paddypower@gmail.com','tenasianbistro5065@gmail.com','Noheacafe@yahoo.com','info@astrodoughnuts.com','frankprofeta96@gmail.com','info@murraystivoli.com','Thecreeksidegrille@gmail.com','contact@pilitagrill.com','marketing@brentsdeli.com','Julianne@jandjgourmet.com','christinesitalian@gmail.com','yumebistro@gmail.com','baums@bellsouth.net','rappoysterbar@rroysters.com','hospitality@rafele.com','roemar006@comcast.net','giovanni.bartocci@me.com','megan@rrtaproom.com','sanremocuisine@gmail.com','banyans@palouseridge.com','info@rubirosanyc.com','bunsrhinebeck@gmail.com','calientecantinasm@gmail.com','griddle@thegriddlecafe.com','aquagrill@aol.com','alchemyrest@gmail.com','BMarie@kingsseafood.com','TeaLady@OneSteepTroom.comcastbiz.net','osakasushi_tivoli@yahoo.com','lorrie@moesoriginalbbq.com','encino@bucainc.com','anne@patsys.com','topbutcherbbq@gmail.com','pranay.srivastava@growlerusa.com','sls.bazaar@luxurycollection.com','restmgr@collegeparkinn.com','ec@chowdowninc.com','foodcowest@gmail.com','izakayamew@gmail.com','7th@nandosperiperi.com','piezzetta@gmail.com','rmorales@taqueriavistahermosa.com','pizza@johnnyrads.com','mike@boppizza.com','mr.davidsspecialtymeats@cox.net','mcd.bhcp@gmail.com','nattakik@gmail.com','chad@chadsbbq.com','mike@elleoncito.com','apascal@arkrestaurants.com','gingergarlicrockledge@gmail.com','cszaino@att.net','media@lgohospitality.com','gallagherssteakhousenyc@gmail.com','barcarola@valk.com','lazybeancc@hotmail.com','johanengman@gmail.com','Bkramer@cantinadiablo.com','basso56@verizon.net','cnj@bareburger.com','aeddy@elikioliveoil.com','pffriends@gmail.com','eat@sugarfishsushi.com','winemarket921@aol.com','ernie@erniesmi.com','info@porsena.com','hanna@hannaleecommunications.com','southfieldpancakehouse@gmail.com','getsocial@nativegrillandwings.com','pulphilliard@gmail.com','BuckysBBQ@BellSouth.net','mes@perillanyc.com','mapofthailand@yahoo.com','eat@papalocos.com','pubamericana@gmail.com','newwavecafe85@gmail.com','sbschef@aol.com','rosie@rosiestrattoria.com','john@ajjrestaurants.com','suzanne@escogelato.com','kaysbbq@cfl.rr.com','pubclub2010@gmail.com','whitshilliard@yahoo.com','chesterlandarabica@gmail.com','Gletlaz@aol.com','orangeblossommiami@gmail.com','johnsonscafe@comcast.net','staxs77@aol.com','robin@greenfieldsbagelsanddeli.com','info@publichouseftl.com','chelsea108@hotmail.com','cuzicafe@bellsouth.net','brothersfamilyrestaurant@gmail.com','topdog@murray-ky.net','curry@currykitchen.net','arrowhead@bucainc.com','margie@orleansrestaurant.com','ibangkok.thai.restaurant@gmail.com','fatgoosebk@gmail.com','kannikasthaikitchen@outlook.com','pinkness401@gmail.com','valerio80marchi@gmail.com','hiberniabar@gmail.com','poy@siamlewisburg.com','draft@smilingchameleon.com','pauldimino@cornercafe-bakery.com','lobsterbar@lobsterbarnyc.com','SunnySideUpCafe@Bellsouth.net','halainrestaurant@yahoo.com','morganscatcafe@gmail.com','greatamericantogo@yahoo.com','rathsalla@yahoo.com','joe@joespizzanyc.com','ebinquiry@danielnyc.com','steak.nshake@yahoo.com','riegelsvilletavern@yahoo.com','silvia.woodstockny@gmail.com','jacoba@GalleryBarChicago.com','rosamiaitalian@gmail.com','mario@civano.com','anthony@italiancoffeehouse.com']
	check_emails(names,emails)
