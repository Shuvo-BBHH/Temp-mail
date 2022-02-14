
# Use python3 bro
# Creater:- Bilal Haider [Own3r of t3am XD]
# Cake-mail [XD]
try:
	import requests as r, random, json, os , time
	from time import sleep
except ModuleNotFoundError:
	exit("[!] Module not installed")

list_mail = ["vintomaper.com","tovinit.com","mentonit.net"]
url = "https://cryptogmail.com/"
num = 0

def get_teks(accept, key):
	cek = r.get(url+"api/emails/"+key, headers={"accept": accept}).text
	if "error" in cek:
		return "-"
	else:
		return cek.strip()

def get_random(digit):
	lis = list("abcdefghijklmnopqrstuvwxyz0123456789")
	dig = [random.choice(lis) for _ in range(digit)]
	return "".join(dig), random.choice(list_mail)

def animate(teks):
	lis = list("\/")
	for cy in lis:
		print("\r["+cy+"] "+str(teks)+".. ", end="")
		sleep(0.5)

def run(email):
	while True:
		try:
			animate("\033[1;94mWAITING FOR INCOMING MESSAGE")
			raun = r.get(url+"api/emails?inbox="+email).text
			if "404" in raun:
				continue
			elif "data" in raun:
				z = json.loads(raun)
				for data in z["data"]:
					print("\r[•] ID: "+data["id"], end="\n")
					got = json.loads(r.get(url+"api/emails/"+data["id"]).text)
					pengirim = got["data"]["sender"]["display_name"]
					email_pe = got["data"]["sender"]["email"]
					subject  = got["data"]["subject"]
					print("\r[•] Sender Name: "+pengirim, end="\n")
					print("\r[•] Sender mail: "+email_pe, end="\n")
					print("\r[•] Subject    : "+subject, end="\n")
					print("\r[•] Message    : "+get_teks("text/html,text/plain",data["id"]), end="\n")
					atc = got["data"]["attachments"]
					if atc == []:
						print("\r[•] attachments: -", end="\n")
					else:
						print("[•] attachments: ")
						for atch in atc:
							id = atch["id"]
							name = atch["file_name"]
							name = name.split(".")[-1]
							svee = r.get("https://cryptogmail.com/api/emails/"+data["id"]+"/attachments/"+id)
							open(id+"."+name, "wb").write(svee.content)
							print("      ~ "+id+"."+name)
					print("-"*45)
					r.delete(url+"api/emails/"+data["id"])
				continue
			else:
				continue
		except (KeyboardInterrupt,EOFError):
				exit("\n[✓] Program finished, exiting...\n")

def main():
	os.system('clear')
	global num

	print("""\033[1;97m _____                          __  __       _ _
|_   _|__ _ __ ___  _ __       |  \/  | __ _(_) |
  | |/ _ \ '_ ` _ \| '_ \ _____| |\/| |/ _` | | |
  | |  __/ | | | | | |_) |_____| |  | | (_| | | |
  |_|\___|_| |_| |_| .__/      |_|  |_|\__,_|_|_|
                   |_|
____________________________________________________________
   \033[1;97mAUTHOR \033[1;94m: \033[1;97m [MAHDI HASAN] SHUVO
   \033[1;97mGITHUB \033[1;94m: \033[1;97mhttps://github.com/Shuvo-BBHH
   \033[1;97mTN \033[1;94m: \033[1;97mTemporary Mail
____________________________________________________________

\033[1;97m[\033[1;94m01\033[1;97m] SET EMAIL RANDOM 
\033[1;97m[\033[1;94m02\033[1;97m] SET EMAIL CUSTOM
\033[1;97m[\033[1;94m03\033[1;97m] CODEX-ID GITHUB
\033[1;97m[\033[1;94m04\033[1;97m] EXIT
""")

	pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")
	while pil == "" or not pil.isdigit():
		pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")
	if pil in ["01","1"]:
		set_name, set_email = get_random(10)
		print("\n\033[1;97m[\033[1;94m*\033[1;97m] YOUR EMAIL: "+set_name+"@"+set_email)
		print("\033[1;91m-"*45)
		run(set_name+"@"+set_email)
	elif pil in ["02","2"]:
		set_name = input("\033[1;97m[\033[1;94m+\033[1;97m] SET MAIL NAME: ")
		print()
		for cy in list_mail:
			num += 1
			print(" "*5,"["+str(num)+"] @"+cy)
		print()
		set_email = input("\033[1;97m[\033[1;94m!\033[1;97m] SELECT: ")
		while set_email == "" or not set_email.isdigit() or int(set_email) > len(list_mail):
			set_email = input("[?] Select: ")
		mail = list_mail[int(set_email)-1]
		print("\n\033[1;97m[\033[1;94m+\033[1;97m] YOUR EMAIL: "+set_name+"@"+mail)
		print("-"*45)
		run(set_name+"@"+mail)
	elif pil in ["03","3"]:
		os.system('xdg-open https://github.com/Shuvo-BBHH')
		time.sleep(2)
		print (" ")
		n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
		time.sleep(2)
		main()
		
if __name__ == "__main__":
	main()
