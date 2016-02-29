
import os
import sys

def main():
	{
				

	}
 
facebook_domains = ["www.static.ak.connect.facebook.com","www.facebook.com","facebook.com", "static.ak.fbcdn.net", "www.static.ak.fbcdn.net", "login.facebook.com", "www.login.facebook.com", "fbcdn.net", "www.fbcdn.net", "fbcdn.com", "www.fbcdn.com", "static.ak.connect.facebook.com"]
aftonbladet_domains = ["www.aftonbladet.se", "aftonbladet.se"]
banned_websites=[]



def ban_choice(ban_facebook,ban_aftonbladet,banned_websites):
	if ban_facebook == "Y":
		banned_websites.extend(facebook_domains)
	if ban_aftonbladet == "Y":
		banned_websites.extend(aftonbladet_domains)
	return banned_websites

def ban_or_removeban():
	ban_or_release=input("\n"+"Write BAN to ban websites or FREE to remove bans"+"\n")
	return ban_or_release

def remove_bans():
	f0 = open("hosts_backup","r")
	original_hostfile = f0.read()
	f1 = open('C:\\WINDOWS\\system32\\drivers\\etc\\hosts', 'w')
	f1.write(original_hostfile)
	f1.close()
	f3 = open('C:\\WINDOWS\\system32\\drivers\\etc\\hosts', 'r')
	data3 = f3.read()
	print(data3)
	f3.close()




def edit_hosts(quant_domains):
	f1 = open('C:\\WINDOWS\\system32\\drivers\\etc\\hosts', 'r')
	data1 = f1.read()
	print(data1)
	f1.close()
	f2 = open('C:\\WINDOWS\\system32\\drivers\\etc\\hosts', 'a')
	i=0
	while (i < quant_domains):
		f2.write("\n" + "0.0.0.0 " + banned_websites[i])
		i+=1
	f2.close()
	f3 = open('C:\\WINDOWS\\system32\\drivers\\etc\\hosts', 'r')
	data3 = f3.read()
	print(data3)
	f3.close()
	return True

main()
choice1=ban_or_removeban()
if choice1 == "BAN":
	ban_facebook = input("Ban facebook for one hour?")
	ban_aftonbladet = input("Ban aftonbladet for one hour?")
else:
	remove_bans()
	sys.exit()
banned_websites_complete=ban_choice(ban_facebook, ban_aftonbladet, banned_websites)
quant_domains=len(banned_websites_complete)
edit_hosts(quant_domains)

sys.exit()