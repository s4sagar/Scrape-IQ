import requests
import dns.resolver
import socket
import smtplib
import unidecode
import psycopg2
import time
import thread
import sys


executive_first_names = ["Howard","Julie","Justin","Roger","Dan","Sara","Will","Mike","Jessica","Adam","Tony","Ken","Ben","Ed","Joseph","Tina","Abe","Erin","Michael","Mike","Tony","Rocky","Elia","Tom","Susan","Dave","Amy","Peter","Wendy","John","Eric","Olivia","mel","Rob","Cristina","Aalap","Bob","John","Nadine","Russell","Tim","Jeremy","Al","Mark","Patrick","Wojciech","Gregory","Dan","Dennie","Ben","Jim","Marty","Greg","Veronica","Kathleen","Chris","Alana","Tim","Jim","Kemper","Kimberton","Steve","Catherine","Edward","Kevin","Rochelle","Jerry","Hanna","Leslie","Heather","Jacob","Colm","Carol Baca","Jennifer","Nick","Dale","Ben","David","Jon D.","Brian","Andre","Joan","Joseph","Thomas","Laura","Kevin","Wayne","Matt","Ryan","Lon","Cindy","John","Nadim","Cynthia","RIC","Julie","Matt","Steven","Michelle","Rajindra","Rob","Sara","Max","Betsy","Matt","Michael","Tim","Mariano","Jack","Jeremy","Brandon","Andy","Abe","Gregory","Mike","Hank","Wes","Thomas","Bradford","William","Brandon","Anna","Elizabeth","Dave","Chaitan","Corey","Kirk","Aaron","Brian","Matt","Ron","Michael","Werner","Mario","JP","Joy","Will","Jeremy","Kevin","Mark","John","Gregory","Dane","Stephen","Saveena","Matthew","Jonathan","Tim","John","Jason","Jay","Lauren ","Augusto","Augusto","David","George","Chris","Jacob","Nick","Alec","Jeff","Schack von","Scott","Rodney","Leslie","Spencer","Brian","Jenna","Dean","Jerry","Flor","Gale","Jim","Kevin","Ryan","Otto","Jovana","Pete","Christopher","Robert","Andy","Stephen","Rodd","Hadi","Mike","John","Javier","TJ","Reena","David","Joseph","Steve","Vijay","Joe","Paul","Jon","Brett","Drew","Howard","Chaitan","Jonathan","Karen","Lisa","Craig","Tyler","Joe","Tabitha","Lawrence","Denis","Marc","Anita","Will","Dominic","Jason","Thomas","Steve","William","Hanno","Siddharth","Shannon","Lance","Kim","Jeff","Timothy","Beth","Chad","Marcie","Greg","Hillary","Brian","Alan","Paolo","Olivier","Kari","Brian","Jonathan","Gottfried","Steve","Amy","Stephanie","Jim","Jay","Scott","Eric","David","Randy","Marie","Piper","Kim","Yoseph","Jennifer","Kory","Erich","Jennifer","Christopher","Ed","Carolyn","Mohammad","Alex","Brandon","Amy","Brandi","Isabel","Paul","Rocky","Rick","Mark","Eddie","Michelle","Michael","Rose","Robert","Jack","Toby","Brook","Tom","Joel","Ryan","Mark","Paul","Eric","Kathy","Peter","David","Doug","Juan","Ryan","Dave","Stacie","Steven","Joe","Scott","Peter","Sourav","Daniel","Monroe","Dan","Ron","Jeffrey","James","Joel","Chris","Tom","Dominic","Mike","Daniel","Bruce","Erin","Claudia","Steve","Bill","David","Teri","Clarissa","Tom","Chris","Rene","Brian","Laura","Michael","Mark","Christine","Shane","Philippa","Steve","Jennifer","Charlie","Roberto","Miles","Jean Yves","Tammy","Clinton","Andrew","Jeffrey","Scott","Nate","Mario","Phil","Chris","Micah","Steve","Gary","Renee ","Scott","Farid","Joe","Carolyn","Michael","Mike","Nick","William","Jessica","Keith","Scott","Bruce","Brendan","Dan","Jamal","Rebecca","Alejandro","Aaron","David","Ed","Stephen","Jennifer","Sarah","Katherine","Troy","Matt","James","Stephen","Joel","Paul","Marco","David","Marco","Mark","Ryan","Richard","Kyle","Kevin","Guillermo","Dan","Jeffrey","Paul","Marjorie","Marjorie","James","Donna","Gregg","Mike","Tara","Mary","Julie","Robb","Michel","Dennis","Melissa","Raymond","Brad","Paul","Minazali","Andrew","Doug","Tony","Cheryl","Phillip","Danny","Nicky","Eric","Phil","Stephanie","Stacy","Anders","Carolyn","Roy","Nick","Adam","Matt","Joshua","Leo","Len","Jimmye","Scott","Jan","Rebecca","Kevin","Houston","Jim","Jeanette","Russell","Bryon","Norma","Kevin","Jessica","Wendy","Missy","Conner","Deb","AJ","Mason","Jason","Sonya","Gregg","Brandon","Albert","Chris","Karen","Hong","Jason","James","Tony","Kristena","Jolene","Brett","Tom","Linda","Joseph","Jim","Augusto","Paul","Craig","John","Bill","Arnie","Eric","Shlomit","Frank","Richard","Jill","Scott","Laarni","Guillermo","Michael","Alan","Robert","Joseph","Brendan","Jonathan","Scott","Lyssa","Christopher","Oswaldo","Aleksey","Christina","Christina","Sherry","Mark","Paul","Herve","Manuel","Michael","Richard","Cyndy","Ken","William","Bill","Tatiana","Amish","Chad","Kent","Jennifer","Bill","Kimberly ","Andrew","Tracy Shannon","Hamish","Jennifer","Scott","Matis","Mark","Thomas","Robert","David","Josh","Shiri","Carlos","Jason","Joel","Todd","Mike","Jayne","James","Albert","Mike","Heidi","Eric","Ted","Mohamed","Reneza","Mandy","Tom","Fernando","Hsin","Ning ","Jessie","Kelly","Kelly"]
executive_last_names = ["Klayman","Silver","Trout","Vivas","Vinh","Custer","Schoentrup","Linsenmayer","Foust","Louras","Bayer","McGovern","Hosseinzadeh","Yashinsky","Gozzi","McGeehen","Ruiz","Ward","Rodriguez","Dulceak","Mazzeo","Clark","Shehady","Saia","Alban","Packenham","Falbaum","Eck","Zalai","Williams","Siegel","Derr","landuyt","Felsch","DeVito","Patel","Wendel","Duffy","Serfass","Diez-Canseco","Zahner","Bergeron","Ryan","Bales","Slocum","Biszta","Donoghue","Braun","Sandefer","Cain","Rockwell","Lev","LaFauci","Chavarria","Neglia","Sluty","Carlton","Hartwig","Stelten","Messner","Messner","DuVall","Porter","Noe","Leggat","Anderson","Horan","L","W","Casey","Bloom","Conway","Kalata","Hotes","Davis","Smucker","Holman","Boyajian","Londeen","Kilker","Romero","Lee","Cristella IV","Preuml","Novak","Finlay","Berkowitz","Wojciechowski","Neubauer","Southerland","Herzog","Edelman","Shah","Yeung","THORNBURG","Silver","Greene","Rubin","Longo","Gunasekera","Viveros","Custer","Rudy","Betsy","Clifford","Gribben","Breen","Doble","Albanese","Marshall","Oldham","Rooney","Ruiz","Leinweber","Dulceak","Margolis","Freeman","Chang","Moose","Bunce","Gall","Duffy","Wild","Packenham","Fahnestock","Aronowitz","Taylor","Acevedo","Riewer","Crowell","Bidinost","Reilly","Schwock","Arena","Lachance","Rinaldi","Sun","Bergeron","Ponticelli","Bales","Carr","Donoghue","Douthit","Posey","Kohli","Preston","Peters","Hartwig","Walch","Borders","Stegall","Culver","Martinez","Orrantia","Vick","Chao","Radford","Bloom","Davis","Riveros","Vandeveer","Rumohr","Lauer","Bridgers","Dean","Taylor","Patterson","Williams","Willard","Estes","Palacios","Moore","Gordon","Finlay","Neubauer","Abad","Granzan","Caputa","Manning","Felder","Major","Lazar","Herron","Irvani","Snyder","Waldron","Flores","Nguyen","Patel","Hall","Horn","Keith","Goel","Willoughby","Leech","Robertson","Morris","Garverick","Hohman","Fahnestock","Wong","Leger","Starr","Hacklander","Duncan","Schechinger","Gonzales","Ciccarelli","Bouchard","Chapman","Kutlesa","Sun","Lewinsohn","Pristash","Healy","Calderone","William","Holm","Sitaram","McNiel","Herman","Rice","Vandeveer","Primus","Gantz","Ellis","Mills","Bublitz","Greene","Unger","Roark","Bonetti","LeRoy","Hunt","Patterson","Baker","Ernst","Sipprell","T","Dents","Gordon","Wetzel","Posnick","Gauvin","Msika","Hough","Washburn","Jones","Watts","Arsala","Schmaltz","Mickelson","J","Rey","Manning","Kam","Ferguson","Hasham","Sigman","Weeks","Supple","B","Sauerbrey","Bruns","McDonald","Henry","Donangelo","Sullivan","Reynolds","Jraisat","Guzman","Zivkovic","Kiggins","Cotton","Sloan","Scalese","Neikirk","Flickinger","C","Ruggiero","Greenwald","Cruz","Barrick","Mosberg","Brooks","Bustamante","Indovina","Orenstein","Harper","Hartenstein","Willoughby","Jeter","Wann","Ghosh","Myers","Karp","Coyle","Elody","Bingham","Brennan","Mellor","Kern","Hind","Lewinsohn","Outlaw","Ekstrom","Dodge","Borders","W","Calderone","Champs","Dunn","Martinez","Daniel","Santora","Gregg","Garrigue","Jansen","Simpson","Boyer","Carlson","Nigro","Sarlo","Green","Sipprell","Sampson","Dyer","Perico","Ellis","Charon","Valdes","Weaver","Kraemer","McClafferty","Murcray","Hjelseth","Lleverino","Rodrigues","Carroll","Derr","Goldenstein","Kraus","Marshall","Isaacs","Biglari","Dominijanni","Sullivan","Carlino","Muller","Sidorakis","N","Lewis","Purcell","Barter","Hungate","O'Connell","Murphy","Khan","Guzy","Castro","Langguth","Piontkowski","Schenkein","Glaser","Vumbaca","McGill","Janowski","Romero","Sunderland","Cella","Power","Neikirk","Ruggiero","Turano","Schreiber","Fanton","Rivera","Indovina","Thomas","Frederick","Kalstad","Florido","Bailey","Bingham","Nagy","Cepeda","McNamara","Brennan","Eskew","McDermott","Outlaw","Hutton","Marriott","Clouse","Greene","Notten","Garvey","Eary","Lubesky","Henning","Vertullo","Hudani","Kraemer","Rigoni","Elrod","Tyndall","DelMonti","Kirkendall","Barber","Salzer","Rodrigues","Bauer","Neal","Crabo","Sullivan","Sundermeyer","Sidorakis","Jurlin","Milcoff","Smith","Greenstein","Greenstein","Ahn","Barter","Wigington","Gustin","Altman","Striggow","Branch","Brick","Petak","Broich","Tyree","Murray","Sardelli","Dominguez","Knaub","Holt","Kaiser","Stockwell","Lee","Hudson","Williams","Santabarbara","Wall","Medoro","Gormsen","Lee","kim","Ramsey","Cella","Candales","Hart","Worthington","Hastings","Haralambos","Hoops","Notaro","Areklett","Rosero","Thibeault","Stoll","Rosatti","Luebke","Fleischman","Anderson","Levy","Rizzo","Pineda","Golder","Kelly","Niro","Florido","Mrlik","Berkel","Baxley","Polito","Clarke","Walter","McMartin","Krumholtz","Nixon","Salazar","Kernes","Van ","Stavern","Mardikian","Wilson","Hildreth","Levy","Fuentes","Sabisch","Cassara","Carr","Dolan","Lehman","Lehman","Bashlova","Patel","Sternard","Johnson","Driscoll","Mannina","Soviero","Christiansen","Levey","Walker","Brixius","Krueger","Soffer","Snyder","Kamowski","Steinberg","Coffman","Thomas","Avnery","Kudja","Hudson","Perez","Curtis","Duke","Buck","Messina","Vazquez","Conway","Wechsler","Knight","Suor","Awad","Corpuz","Kroker","Konopasek","Lyons","Ho","Ho","Ho","Johnson","Parker"]
domain_names = ["http://www.benjaminfoods.com/","http://www.fijiwater.com/","http://health-ade.com/","http://www.hotelcolonnade.com/","http://www.moblty.com/","http://www.imperfectproduce.com/","https://www.westwindaviation.ca/","http://www.singerlewak.com/","http://www.farmersfridge.com/","http://www.dirtylemon.com/","http://www.barriotequila.com/","http://www.onyxcentersource.com/","http://foodstirs.com/","http://www.troegs.com/","http://www.rolandfoods.com/about/careers/","http://www.onedatascan.com/","http://www.eathere.com/","http://www.brooklynbowl.com/","http://cadillacsf.com/","http://www.bunn.com/","http://eatatcore.com/","http://tacojohns.com/","https://nuts.com/","http://www.newks.com/","http://www.zume-com/","https://www.suncast.com/","http://www.amyfalbaum.com/","https://intelligentsiacoffee.com/","http://www.1800petmeds.com/","http://www.buddig.com/","http://www.dermaconcepts.com/","http://zerocater.com/","http://themaderagroup.com/","http://www.arraybiopharma.com/","http://www.collectiveretreats.com/","https://nuts.com/","http://www.siggisdairy.com/","https://www.drinkcoffee.com/","http://www.uptownnetwork.com/","http://www.vitalfarms.com/","http://www.sonomacounty.com/","http://www.bevi.co/","http://firopizza.com/","http://www.getconga.com/","https://c3iot.ai/","http://www.avendra.com/","http://www.cloverfoodlab.com/","http://taldepot.com/","http://www.zaxbysfranchising.com/","https://urbanremedy.com/","http://www.kongcompany.com/","http://www.fuchsna.com/","http://www.16handles.com/","http://www.baresnacks.com/","http://www.blackman.com/","http://www.floqast.com/","http://www.foodbuy.com/","http://www.hosthotels.com/","http://www.bergankdv.com/","http://www.bradsrawfoods.com/","http://www.bradsrawfoods.com/","http://www.alto-shaam.com/","http://www.greciandelight.com/","http://www.pizzasavor.com/","http://www.recursionpharma.com/","http://www.haralambos.com/","http://www.conferencedirect.com/","http://www.thepurplecarrot.com/","http://www.betterworks.com/","http://www.ehs.com/","http://www.rockstarenergy.com/","http://www.thompsoncigar.com/","https://www.nassaucandy.com/","http://captricity.com/","http://pearsonscandy.com/","http://www.auntieannes.com/","http://www.spyderco.com/","http://oathpizza.com/","http://www.lhw.com/","http://www.newportchintl.com/","http://www.campbellsoupcompany.com/","http://www.traveltripper.com/","https://www.cento.com/","http://www.houstonracquetclub.com/","http://www.compoundsolutions.com/","http://www.airpush.com/","http://www.berdonllp.com/","http://www.mavs.com/","http://www.generalatlantic.com/","http://www.illy.com/","http://www.smashotels.com/","http://www.dwr.com/","http://www.whg.com/","http://www.cafexapp.com/","http://www.backyardburgers.com/","http://www.fijiwater.com/","http://www.evolutionhospitality.com/","http://lodgiq.com/","http://www.mellowmushroom.com/","http://www.heartflow.com/","https://www.foodfirst.com/index.html","http://www.imperfectproduce.com/","http://www.happyfamilyorganics.com/","http://duckdonuts.com/","http://barnana.com/","http://www.philzcoffee.com/","http://www.piefivepizza.com/","http://www.davidsoninn.com/","http://www.terrapinbeer.com/","http://www.madgreens.com/","http://www.rpxcorp.com/","http://www.moes.com/","http://www.eathere.com/","http://www.monaco-dc.com/","http://www.bunn.com/","http://www.zevia.com/","http://ehsandwich.com/","http://www.plumorganics.com/","http://www.halenbrands.com/owyn.html","http://phoenixhospitalitygroup.com/","http://www.mgpingredients.com/","http://www.tazikiscafe.com/","http://www.lightstonegroup.com/","https://www.suncast.com/","http://www.riveronconsulting.com/","http://oneconcierge.com/","http://www.alamocement.com/","http://www.beyondmeat.com/","http://www.bmmlogistics.com/","https://cashbrewing.com/","http://www.bubbakoosburritos.com/","http://www.transitvalley.com/","http://www.hashicorp.com/","http://www.wontonfood.com/","http://www.equatorcoffees.com/","http://www.cpsrecruiter.com/","http://www.imperfectproduce.com/","http://www.bevi.co/","http://mizkan.com/Home.aspx","http://www.getconga.com/","http://www.ftsonline.com/","http://www.cloverfoodlab.com/","http://www.nothingbundtcakes.com/","http://www.pecandeluxe.com/","https://naturebox.com/sub/jobs","https://www.daily-harvest.com/","http://www.chbriggs.com/","http://www.hosthotels.com/","https://www.marcusinvestments.com/","http://tag-restaurant.com/","http://www.schlotzskys.com/","http://www.ccbss.com/","http://www.auifinefoods.com/","http://www.auifinefoods.com/","http://www.tchhome.com/","http://www.vosgeschocolate.com/","http://www.boxedwaterisbetter.com/","http://www.rockstarenergy.com/","http://pearsonscandy.com/","http://www.alpinerestaurantgroup.com/","http://www.shiftgig.com/","http://www.streamsongresort.com/","http://www.ashers.com/","http://www.strategicequipment.com/","http://www.togos.com/","http://www.owletcare.com/","http://www.goodfoods.com/","http://www.nextech.com/","http://www.nitta-gelatin.com/","http://www.gallikers.com/","http://www.blazepizza.com/","http://www.singerlewak.com/","http://www.hme.com/","http://www.airpush.com/","http://www.generalatlantic.com/","http://www.afesco.com/","http://abg-nyc.com/","http://www.wixon.com/","http://www.redjacketresorts.com/","http://www.capersdmc.com/","http://www.juice4u.com/","http://www.keyevents.com/","http://www.cendyn.com/","http://www.peachdish.com/","http://www.newks.com/","http://www.treehousefoods.com/","https://www.twistbioscience.com/","http://www.ccbss.com/","http://www.durachem.com/","http://www.ihgplc.com/","http://www.zola.com/","http://glencoemanagement.com/","http://www.goelinsights.com/","http://www.beckflavors.net/","https://perspicacityllc.com/","http://www.typsy.com/","http://www.poloclub.net/","http://www.greatwraps.com/","http://www.rmhfranchise.com/","http://www.riveronconsulting.com/","http://www.caliburgerintl.com/","http://www.carnegietechnologies.com/","http://www.motivaction.com/","http://www.jackmont.com/","http://www.rustyspizza.com/bakersfield/home","http://www.wqscc.com/","http://www.uship.com/?r&#61;5926603","http://www.townofstratford.com/","http://www.wendys.com/","http://www.beforebrands.com/","http://www.transifex.com/","http://www.imperfectproduce.com/","https://www.prospect33.com/","http://fifthgroup.com/","http://drhc.com/","http://www.perfectbar.com/","http://bevolutiongroup.com/","http://www.atkins.com/","https://www.adaptiveinsights.com/","http://www.tomsurban.com/","http://starhg.com/","http://www.rmc-chi.com/","http://www.shiftgig.com/","https://www.mightyswell.com/","http://www.gothamgreens.com/","https://www.oakhillcc.com/","http://www.mirabel.com/","http://www.sunevamedical.com/","https://www.brewbound.com/news/anheuser-busch-inbev-reorganizes-high-end-division","http://www.ljsilvers.com/","http://www.dairyqueen.com/","https://www.madeinnature.com/","http://www.sasademarle.com/","https://sasteelco.com/","http://www.goodfoods.com/","http://mondaynightbrewing.com/","http://www.greencourtepartners.com/","http://www.steviescatering.com/","http://www.rivian.com/","http://www.ronnoco.com/","http://www.hme.com/","http://www.virginhotels.com/","https://www.aafcpa.com/","http://www.wichcraft.com/","http://www.bentleymills.com/","https://www.lennys.com/index.cfm","http://www.generationbio.com/","https://www.kohanacoffee.com/","http://willys.com/","http://www.eatpre.com/","http://www.computype.com/","http://www.craftmarkbakery.com/","http://www.hosthotels.com/","http://www.littlepassports.com/","http://www.redjacketresorts.com/","http://www.equilar.com/","http://www.belleepicurean.com/","http://www.soaprojects.com/","http://www.foodsgalore.com/","http://tindrumasiankitchen.com/","http://www.theedgewater.com/","http://www.zpizza.com/","http://www.sandiego.org/","http://wtrmlnwtr.com/","http://www.clinicomp.com/","http://www.fosscare.org/","http://www.gingerpeople.com/","https://risckys.com/","https://mindtouch.com/","http://www.steakescape.com/","http://www.ilovelindsay.com/","http://www.dartagnan.com/","http://www.sleepyhollowcc.org/","http://www.whitleypenn.com/","http://goldenchick.com/","http://www.eastcoastwingsfranchise.com/","http://www.midamcorp.com/","https://wingsetc.com/","https://www.espresso.events/","http://www.nksdistributors.com/","http://www.nokidhungry.org/","https://www.papaginos.com/","http://www.smashmallow.com/","http://www.triumvirfinancial.com/","http://www.nexushospitality.com/","http://www.fiveguys.com/","http://provi.com/","https://fishcitygrill.com/","http://www.stayalfred.com/?utm_source&#61;linkedin&amp;utm_medium&#61;social&amp;utm_campaign&#61;companyprofile","http://www.stefanirestaurants.com/","http://www.beckflavors.net/","http://www.blackbeardiner.com/","http://www.conferencedirect.com/","http://www.hosthotels.com/","http://yumearth.com/","http://www.reloquest.com/","http://www.guenergy.com/","http://www.kahalabrands.com/","http://www.gallerycarts.com/","http://www.wegotsoccer.com/","https://www.organicvalley.coop/","http://saladandgo.com/","http://burgerfi.com/","https://www.prospect33.com/","http://www.limefreshmexicangrill.com/","http://liquid-consulting.com/","https://www.bandidosmecxicanrestaurantri.com/","http://www.tokyojoes.com/","http://www.onceuponafarmorganics.com/","http://www.perfectbar.com/","http://www.nexenta.com/","http://www.foodbuy.com/","http://www.tazikiscafe.com/","http://www.rockfish.com/","https://www.alhworld.com/","https://impossiblefoods.com/","http://www.dostoros.com/","http://www.celestialseasonings.com/","http://www.bluestonelane.com/","http://www.allianceresourcegroup.com/","http://www.downtownproject.com/","http://lapecorabianca.com/","http://jobs.sanctuaryoncamelback.com/","http://www.jetsetsports.com/","http://www.steviescatering.com/","http://www.onyxcentersource.com/","https://www.moes.com/","http://www.visitcatalinaisland.com/","https://www.juniorscheesecake.com/","http://galaxydesserts.com/","https://www.earlofsandwichusa.com/","https://www.hostway.com/","http://www.enginfotech.com/","http://www.dunnsriverbrands.com/","http://www.airxpanders.com/","http://www.dairyqueen.com/","http://www.urbanecafe.com/","http://www.simplemills.com/","http://www.floridafood.com/","https://www.alfalfas.com/","http://www.rockviewfarms.com/","http://www.magnoliabakery.com/","https://www.solutiontree.com/","http://tonyromas.com/","http://www.togos.com/","http://www.armada.net/","https://altaplanning.com/","http://www.findyourshaka.com/","http://www.bonedaddys.com/","https://www.southernhillscc.com/","http://www.factory-llc.com/","http://www.performancepeople.com/","http://www.dsfcpa.com/","http://www.fisherislandclub.com/","https://www.scheidfamilywines.com/","http://www.biolase.com/","http://www.pizzafire.com","https://www.fatbrands.com/","http://www.frickmeats.com/","http://www.oasiscollections.com/","http://epicburger.com/","http://ainsworthpets.com/","http://www.singerlewak.com/","http://www.mgpingredients.com/","https://www.wahlburgersrestaurant.com/","http://www.hillpartners.com/","http://www.mybenefits.me/","http://www.tabasco.com/","http://www.lacolombe.com/","http://www.cloverlanddairy.com/","http://slsbeverlyhillshotel.com/","http://www.midamcorp.com/","http://www.nksdistributors.com/","https://www.novelloboca.com/","http://www.clubgetaway.com/","http://www.meliahotelsinternational.com/","http://www.eatnoon.com/","http://provi.com/","http://www.bordendairy.com/","http://www.bellagreen.com/","http://www.geckohospitality.com/","http://www.parccorniche.com/","http://www.karsnuts.com/","http://www.gallerycarts.com/","http://www.woodlandfoods.com/","http://www.runa.org/","http://www.runa.org/","http://www.wegotsoccer.com/","http://arcop.co.in/","http://www.bluemoonpizza.com/","http://www.limefreshmexicangrill.com/","http://www.digiday.com/","https://rakutensl.com/","http://www.gallellire.com/","http://www.clustertruck.com/","http://www.virginhotels.com/","http://www.fancyfoodscom/","http://www.cinnabon.com/","http://tacojohns.com/","http://www.flavorproducers.com/","http://www.seviroli.com/","https://www.kriyahotels.com/","http://www.enginfotech.com/","http://www.coasthotels.com/","https://www.zaxbys.com/?gclid=CjwKCAjw5ZPcBRBkEiwA-avvk8vadoiIvS6imTq3CWsXguG5FcNoToP9655UmrqkWmr-SOMDWtY5KRoCA5sQAvD_BwE","http://www.serendipitylabs.com/","http://www.necco.com/","http://www.impossiblefoods.com/","http://www.invuity.com/","http://argconcepts.com/","http://www.simplemills.com/","http://www.whg.com/","http://www.3eyetech.com/","http://www.joyridecoffeedistributors.com/","https://altaplanning.com/","http://www.smoothieking.com/","http://southernhillscc.com","http://www.fabtex.com/","http://www.uniprofoodservice.com/","http://www.blackriflecoffee.com/","http://www.sppirx.com/","http://www.sppirx.com/","https://craftydelivers.com/","http://www.fisherislandclub.com/","http://www.entertainmentbenefits.com/","http://www.bhh.com/","https://franchise.yourpie.com/","http://www.susiecakes.com/","http://www.otonomy.com/","http://www.isinorthamerica.com/","http://www.gaffney-kroese.com/","http://www.lonelyplanet.com/","http://www.patriceandassociates.com/","https://www.ritasice.com/","http://www.avedro.com/","http://www.kfcoffee.com/","http://www.meridinet.com/","http://spreetail.com/","http://www3.hilton.com/en/hotels/arizona/hilton-phoenix-mesa-MESHPHF/index.html","https://www.tn.com/","http://www.7gdistributing.com/","http://www.gogosqueez.com/","http://www.califiafarms.com/","http://www.bendhsa.com/","http://www.joecoffeecompany.com","http://www.customprocessingservices.com/","http://www.rljlodgingtrust.com/","http://www.aeriepharma.com/","http://www.bonchon.com/","http://www.ljsilvers.com/","http://www.cloverlanddairy.com/","http://www.templetonsolutions.com/","http://www.rawjuce.com/","http://www.elicheesecake.com/","https://reliv.com/","http://www.haralambos.com/","http://mutualmobile.com/","http://pinehill.com/","https://www.marburylaw.com/","http://www.drinkneuro.com/","http://www.switchfly.com","http://delfinasf.com/","http://www.burgerfi.com/","https://perspecta.com/","http://www.hospitalitymatches.com/","http://www.skytap.com/","http://www.pandologic.com/","http://www.hospitalitymatches.com/","https://www.pieology.com/","http://www.barflyventures.com/","http://www.gattispizza.com/","http://www.aquahydrate.com/","http://www.parccorniche.com/","http://www.sarkujapan.com/","http://www.sonomabrands.com/","http://www.zaxbys.com/","http://thedewberrycharleston.com/","http://www.dmadelivers.com/","http://www.alto-shaam.com/","http://www.funcoffeeco.com/","http://santokugroup.com/","http://www.ashfordcom/","http://vpxsports.com/","http://www.hooch.co/","http://www.fiercecom/","http://www.fiercecom/","http://www.specformliners.com/","http://fifthgroup.com/","http://rljlodgingtrust.com/index.html","http://www.beverlyhillscc.com/","http://www.labelmaster.com/","http://www.usinger.com/","http://www.napleshotelgroup.com/","http://www.vmghealth.com/","http://www.whg.com/","http://www.drinkworks.com/","http://www.drinkworks.com/","http://www.halontax.com/","http://www.thisbarsaveslives.com/","http://www.stellaandchewys.com/","http://www.bcc1898.com/","http://www.mcneillhotels.com/","http://www.energous.com/","http://www.sakaralife.com/","http://www.cardlytics.com/","http://www.parkertaxpublishing.com/","http://www.seattlefish.com/","http://www.dairyqueen.com/","http://www.wndecpa.com/","http://www.qualityfrozenfoods.com/","http://www.fullsailbrewing.com/","http://www.wingstop.com/","http://www.nathansfamous.com/","http://www.doximity.com/","https://www.greenislandcc.org/","http://www.thistle.co/","http://www.quantumstorage.com/","http://www.gogosqueez.com/","http://www.mymomochi.com/","http://www.visterracom/","http://www.tropicalfoods.com/","http://www.visitdenver.com/","http://www.mountainridgecc.org/","http://www.deenmeat.com/","http://www.secondcity.com/","http://www.sunkist.com/","http://www.huhot.com/","http://tacojohns.com/","http://www.charliebrowns.com","https://getbase.com/","https://www.cityofaspen.com/","http://ezlinksgolf.com/","http://www.klements.com/","http://www.tapiocaexpress.com/","http://www.tapiocaexpress.com/","http://www.tapiocaexpress.com/","http://www.cascadecoffee.com/","http://www.lasvegaspaving.com/"]
company_names=[
"Benjamin Foods",
"Fiji Water",
"Health-Ade Kombucha",
"Hotel Colonnade Coral Gables, A Tribute Portfolio Hotel",
"Moblty ",
"Imperfect Produce",
"Westwind Aviation ",
"Singerlewak ",
"Farmer'S Fridge",
"Dirty Lemon",
"Barrio",
"Onyx Centersource",
"Foodstirs",
"Troegs Brewing Company",
"Roland Foods",
"Datascan",
"Eat Here Brands",
"Brooklyn Bowl",
"Cadillac Bar & Grill",
"Bunn",
"Corelife Eatery",
"Taco John'S International",
"Nuts.Com",
"Newk'S Eatery",
"Zume ",
"Suncast Corporation",
"Amy Falbaum & Associates",
"Intelligentsia Coffee ",
"Petmed Express",
"Carl Buddig And Company",
"Dermaconcepts / Environ Skin Care",
"Zerocater",
"The Madera Group",
"Array Biopharma ",
"Collective Retreats",
"Nuts.Com",
"Siggi'S Dairy",
"Corporate Essentails",
"Uptown Network",
"Vital Farms",
"Sonoma County Tourism",
"Bevi",
"Firo Fire Kissed Pizza",
"Conga",
"C3 Iot",
"Avendra ",
"Clover Food Lab",
"Tal Depot",
"Zaxby'S Franchising",
"Urban Remedy ",
"Kong Company",
"Fuchs North America",
"16 Handles",
"Bare Snacks",
"Blackman Plumbing Supply Co.",
"Floqast",
"Foodbuy Usa",
"Host Hotels & Resorts",
"Bergankdv",
"Brad'S Raw Foods",
"Brad'S Raw Foods",
"Alto-Shaam",
"Grecian Delight Foods",
"Pizza Savor",
"Recursion Pharmaceuticals",
"Haralambos Beverage Company",
"Conferencedirect",
"Purple Carrot",
"Betterworks",
"Velocityehs",
"Rockstar Energy Drink",
"Thompson & Co",
"Nassau Candy Distributors",
"Captricity",
"Pearson'S Candy Company",
"Auntie Anne'S",
"Spyderco",
"Oath Pizza",
"The Leading Hotels Of The World",
"Newport Ch International",
"Campbell Soup Company",
"Travel Tripper",
"Cento Fine Foods",
"Houston Racquet Club",
"Compound Solutions",
"Airpush, ",
"Berdon ",
"Dallas Mavericks",
"General Atlantic",
"Illy Caffe North America",
"Smashotels",
"Design Within Reach",
"Westmont Hospitality Group",
"Cafe X Technologies",
"Back Yard Burgers",
"Fiji Water",
"Evolution Hospitality",
"Lodgiq",
"Home-Grown Industries Of Ga Dba Mellow Mushroom",
"Heartflow, ",
"Food First Global Restaurants",
"Imperfect Produce",
"Happy Family Brands (Nurture )",
"Duck Donuts",
"Barnana",
"Philz Coffee",
"Pie Five Pizza Co",
"Davidson Village Inn ",
"",
"Terrapin Beer Co.",
"Mad Greens - Eat Better",
"Rpx Corporation",
"Moe'S Southwest Grill",
"Eat Here Brands",
"Monaco Washington Dc, A Kimpton Hotel",
"Bunn",
"Zevia",
"East Hampton Sandwich Co.",
"Plum Organics",
"Owyn",
"Phoenix Hospitality Group",
"Mgp Ingredients",
"Taziki'S Mediterranean Cafe",
"Lightstone Group",
"Suncast Corporation",
"Riveron",
"One Concierge",
"Alamo Concrete Products, Ltd.",
"Beyond Meat",
"Bmm Logistics",
"Cash Brewing Company",
"Bubbakoos Burritos",
"Transit Valley Country Club",
"Hashicorp",
"Wonton Food ",
"Equator Coffees & Teas",
"Cps Recruitment",
"Imperfect Produce",
"Bevi",
"Mizkan Group, R&B Foods And Mizkan Americas",
"Conga",
"Fortessa Tableware Solutions",
"Clover Food Lab",
"Nothing Bundt Cakes",
"Pecan Deluxe Candy Company",
"Naturebox",
"Daily Harvest",
"C.H. Briggs",
"Host Hotels & Resorts",
"Marcus Investments",
"Tag Restaurant Group",
"Schlotzsky's",
"Coca Cola Bottlers",
"Aui Fine Foods",
"Aui Fine Foods",
"Twinlab Consolidation Corporation",
"Vosges Haut-Chocolat",
"Boxed Water Is Better",
"Rockstar Energy Drink",
"Pearson'S Candy Company",
"Alpine Restaurant Group",
"Shiftgig",
"Streamsong Resort",
"Asher'S Chocolates",
"Trimark Strategic",
"Togo'S Eateries",
"Owlet Baby Care",
"Good Foods Group",
"Nextech Systems",
"Nitta Gelatin Na",
"Galliker Dairy Co",
"Blaze Pizza",
"Singerlewak ",
"Hme",
"Airpush, ",
"General Atlantic",
"Associated Food Equipment & Supplies",
"Authentic Brands Group",
"Wixon",
"Red Jacket Resorts",
"Capers Dmc",
"Country Pure Foods",
"Key Events",
"Cendyn",
"Peachdish",
"Newk'S Eatery",
"Treehouse Foods",
"Twist Bioscience",
"Coca Cola Bottlers",
"Dura Chemicals, ",
"Intercontinental Hotels Group",
"Zola.Com",
"Glencoe Management",
"Goel Insights",
"Beck Flavors",
"Perspicacity",
"Typsy",
"The Polo Club Of Boca Raton",
"Great Wraps",
"Rmh Franchise Corporation",
"Riveron",
"Caliburger",
"Carnegie Technologies",
"Motivaction",
"Jackmont Hospitality",
"Rusty'S Pizza Parlor ",
"Wendy'S Quality Supply Chain Cooperative",
"Uship",
"Town Of Stratford, Ct",
"The Wendy'S Company",
"Before Brands",
"Transifex",
"Imperfect Produce",
"Prospect 33",
"Fifth Group Restaurants",
"Diamondrock Hospitality",
"Perfect Bar",
"Bevolution Group",
"Atkins Nutritionals",
"Adaptive Insights",
"Tom'S Urban",
"Star Hospitality Group",
"R&M Consulting",
"Shiftgig",
"Mighty Swell",
"Gotham Greens",
"Oak Hill Country Club",
"Mirabel Golf Club",
"Suneva Medical",
"Anheuser-Busch - The Craftbu Division",
"Long John Silver'S",
"Dairy Queen",
"Madhava Natural Sweeteners",
"Sasa Demarle",
"San Antonio Steel Company",
"Good Foods Group",
"Monday Night Brewing",
"Green Courte Partners",
"Stevie'S Aviation Catering",
"Rivian",
"Ronnoco Coffee",
"Hme",
"Virgin Hotels",
"Aafcpas",
"Wichcraft",
"Bentley Mills",
"Lenny'S Sub Shop",
"Generation Bio",
"Kohana Coffee",
"Willy'S Mexicana Grill",
"Pre Brands",
"Computype",
"Craftmark Bakery",
"Host Hotels & Resorts",
"Little Passports",
"Red Jacket Resorts",
"Equilar",
"Belle Epicurean",
"Soaprojects",
"Foods Galore",
"Tin Drum Asiacafe",
"The Edgewater Madison",
"Zpizza International",
"San Diego Tourism Authority",
"Wtrmln Wtr",
"Clinicomp, Intl.",
"Foss Home And Village",
"Ginger People Group",
"Riscky'S Bbq",
"Mindtouch",
"Steak Escape",
"Bell-Carter Foods",
"D'Artagnan",
"Sleepy Hollow Country Club",
"Whitley Penn",
"Golden Chick",
"East Coast Wings + Grill",
"Midamerica Hotels Corporation",
"Wings Etc.",
"Espresso Events Las Vegas, Orlando, Washington, Dc",
"N.K.S. Distributor'S ",
"Share Our Strength",
"Papa Ginos ",
"Smashmallow",
"Triumvir Financial",
"Nexus Hospitality",
"Five Guys Enterprises",
"Provi",
"Fish City Grill",
"Stay Alfred",
"Navy Pier",
"Beck Flavors",
"Black Bear Diner ",
"Conferencedirect",
"Host Hotels & Resorts",
"Yumearth",
"Reloquest",
"Gu Energy Labs",
"Kahala Brands",
"Gallery: Carts.Kiosks.Portables.",
"Wegotsoccer",
"Organic Valley",
"Salad And Go",
"Burger Fi",
"Prospect 33",
"Lime Fresh Mexican Grill",
"Liquid Consulting",
"Bandidos Mexican Restaurant",
"Tokyo Joe'S",
"Once Upon A Farm",
"Perfect Bar",
"Nexenta Systems",
"Foodbuy Usa",
"Taziki'S Mediterranean Cafe",
"Rockfish Seafood Grill",
"Associated Luxury Hotels",
"Impossible Foods",
"Dos Toros Taqueria",
"Celestial Seasonings Tea",
"Bluestone Lane",
"Alliance Resource Group",
"Downtown Project",
"La Pecora Bianca",
"Sanctuary Camelback Mountain",
"Jet Set Sports",
"Stevie'S Aviation Catering",
"Onyx Centersource",
"Moe'S Southwest Grill",
"Catalina Island Company",
"Juniors Cheesecake ",
"Galaxy Desserts",
"Earl Of Sandwich",
"Hostway Services, ",
"Eng Infotech Corp.",
"Dunn'S River Brands",
"Airxpanders",
"Dairy Queen",
"Urbane Cafe",
"Simple Mills",
"Florida Food Products",
"Alfalfa'S Market",
"Rockview Farms",
"Magnolia Bakery",
"Solution Tree",
"Romacorp",
"Togo'S Eateries",
"Armada Supply Chain Solutions",
"Alta Planning + Design",
"Shaka Bowl",
"Bone Daddy'S House Of Smoke",
"Southern Hills Country Club",
"Factory ",
"Naumann Hobbs Material Handling",
"Downey,Sweeney, Fitzgerald & Co. Pc",
"Fisher Island Club",
"Scheid Family Wines",
"Biolase",
"Pizzafire",
"Fat Brands ",
"Frick'S Quality Meats",
"Oasis",
"Epic Burger",
"Ainsworth Pet Nutrition",
"Singerlewak ",
"Mgp Ingredients",
"Wahlburgers",
"Hill & Partners Branded Environments",
"My Benefits & First Party Administrator",
"Mcilhenny Company",
"La Colombe Coffee Roasters",
"Cloverland / Greenspring Dairy",
"Sls Hotel, A Luxury Collection Hotel, Beverly Hills",
"Midamerica Hotels Corporation",
"N.K.S. Distributor'S ",
"Novello Restaurant & Bar",
"Club Getaway",
"Melia Hotels International",
"Noon Mediterranean",
"Provi",
"Borden Dairy Company",
"Bellagreen",
"Gecko Hospitality (Corporate)",
"Parc Corniche Resort",
"Kar'S Nuts",
"Gallery: Carts.Kiosks.Portables.",
"Woodland Foods",
"Runa",
"Runa",
"Wegotsoccer",
"Arcop",
"Blue Moon Pizza",
"Lime Fresh Mexican Grill",
"Digiday",
"Rakuten Super Logistics",
"Gallelli Real Estate",
"Clustertruck",
"Virgin Hotels",
"Fancy Foods ",
"Cinnabon",
"Taco John'S International",
"Flavor Producers",
"Seviroli Foods",
"Kriya Hotels",
"Eng Infotech Corp.",
"Coast Hospitality",
"Zax, (Zaxbys)",
"Serendipity Labs",
"New England Confectionery Company (Necco)",
"Impossible Foods",
"Invuity",
"Apheleia Restaurant Group",
"Simple Mills",
"Westmont Hospitality Group",
"3Eye Technologies",
"Joyride",
"Alta Planning + Design",
"Smoothie King (Skfi)",
"Southern Hills Country Club",
"Fabtex",
"Unipro Foodservice",
"Black Rifle Coffee Company",
"Spectrum Pharmaceuticals",
"Spectrum Pharmaceuticals",
"Crafty",
"Fisher Island Club",
"Entertainment Benefits Group",
"Boston Harbor Hotel",
"Your Pie Franchising",
"Susiecakes Bakeries",
"Otonomy",
"Isi North America, ",
"Gaffney-Kroese Supply Co",
"Lonely Planet",
"Patrice And Associates Franchising ",
"Rita'S Italian Ice",
"Avedro",
"K&F Coffee Roasters",
"Meridian Enterprises Corporation",
"Spreetail",
"Hilton Phoenix/Mesa",
"Tuft & Needle",
"7G Distributing",
"Materne North America - Gogo Squeez",
"Califia Farms",
"Bend Financial",
"Joe Coffee Co.",
"Custom Processing Services",
"Rlj Lodging Trust",
"Aerie Pharmaceuticals",
"Bonchon Franchise ",
"Long John Silver'S",
"Cloverland / Greenspring Dairy",
"Templeton Solutions",
"Raw Juice",
"Eli'S Cheesecake",
"Reliv International",
"Haralambos Beverage Co",
"Mutual Mobile",
"Pine Hill Group",
"The Marbury Law Group, P",
"Neurobrands",
"Switchfly",
"Delfina Restaurant Group",
"Burgerfi",
"Perspecta",
"Hospitalitymatches.Com",
"Skytap",
"Pandologic",
"Hospitalitymatches.Com",
"Pieology",
"Barfly Ventures",
"Mr. Gatti'S Pizza",
"Aquahydrate, ",
"Parc Corniche Resort",
"Sarku Japan",
"Sonoma Brands",
"Zax ",
"The Dewberry Charleston",
"Dma (Distribution Market Advantage)",
"Alto-Shaam",
"Fundamental Coffee Company",
"Kc Pie",
"Ashford ",
"Vital Pharmaceuticals,  Vpx",
"Hooch",
"Fierce",
"Fierce",
"Spec Formliners",
"Fifth Group Restaurants",
"Rlj Lodging Trust",
"Beverly Hills Country Club",
"Labelmaster",
"Fred Usinger",
"Naples Hotel Group",
"Vmg Health",
"Westmont Hospitality Group",
"Drinkworks",
"Drinkworks",
"Halon Tax",
"This Bar Saves Lives",
"Stella & Chewy'S",
"Baltimore Country Club",
"Mcneill Hotel Company",
"Energous Corporation",
"Sakara Life",
"Cardlytics",
"Parker Tax Pro Library",
"Seattle Fish Company",
"Dairy Queen",
"White Nelson Diehl Evans ",
"Quality Frozen Foods ",
"Full Sail Brewing",
"Wingstop Restaurants",
"Nathan'S Famous",
"Doximity",
"Green Island Country Club",
"Thistle",
"Quantum Storage Systems",
"Materne North America - Gogo Squeez",
"The Mochi Ice Cream Company",
"Visterra ",
"Tropical Foods",
"Visit Denver, The Convention & Visitors Bureau",
"Mountain Ridge Country Club",
"Deen Meat And Cooked Foods",
"The Second City",
"Sunkist Growers",
"Huhot Mongolian Grill",
"Taco John'S International",
"Charlie Brown'S Steak House",
"Base Crm",
"City Of Aspen",
"Ezlinks Golf ",
"Klement Sausage Co",
"Tapioca Express",
"Tapioca Express",
"Tapioca Express",
"Cascade Coffee",
"Las Vegas Paving Corp"]

all_valid_emails = []
idx = 0
	
def validate_domain():
	global idx
	curr_idx = idx
	idx = idx + 1

	global all_valid_emails
	domain_name = domain_names[curr_idx]
	# domain_name=domain_name.split('//')[1].split('/')[0]
	if 'www.' in domain_name:
		domain_name=domain_name.split('www.')[1]

	if domain_name.count('.') > 1:
		#subdomain.domain.com
		domain_name = domain_name.split('.')[1]

	# Trailing /
	if domain_name.endswith('/'):
		domain_name = domain_name[:-1]

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
			first_name_exec = executive_first_names[curr_idx]+'@'+domain_name
			last_name_exec = executive_last_names[curr_idx]+'@'+domain_name
			first_last_name_exec = executive_first_names[curr_idx]+'.'+executive_last_names[curr_idx]+'@'+domain_name
			first_init_last_exec = str(executive_first_names[curr_idx][0])+executive_last_names[curr_idx]+'@'+domain_name

			# print '\nTrying '+first_name_exec
			for email in [first_name_exec, last_name_exec, first_last_name_exec, first_init_last_exec]:
				code, message = server.rcpt(str(email))
				if code == 250:
					valid_emails.append(email)
					break

			server.quit()
	except:
		print 'SMTP Failed for '+domain_name
	print '\n'+company_names[curr_idx]+' : '
	print valid_emails
	all_valid_emails.append(valid_emails)


def find_email_thread():
	while idx<len(domain_names):
		validate_domain()
		sys.stdout.flush()


# def find_emails():
# 	# Create two threads as follows
# 	try:
# 		while idx < len(domain_names):
# 		   # 95 to 700 tried
# 		   thread.start_new_thread( find_email_thread, () )
		   
	   
# 	except:
# 	   print "Error: unable to start thread"

if __name__=="__main__":
	try:
		thread.start_new_thread( find_email_thread, () )
		time.sleep(60)
		thread.start_new_thread( find_email_thread, () )
		time.sleep(60)
		thread.start_new_thread( find_email_thread, () )
		time.sleep(60)
		thread.start_new_thread( find_email_thread, () )
		time.sleep(60)
		thread.start_new_thread( find_email_thread, () )
		time.sleep(60)

		while idx < len(domain_names):
		   # 95 to 700 tried
		   thread.start_new_thread( find_email_thread, () )
		   time.sleep(1800)
	   
	except:
	   print "Error: unable to start thread"
