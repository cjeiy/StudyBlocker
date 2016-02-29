from tkinter import *
from tkinter import ttk
import time
import math


"""

facebook_domains = ["www.static.ak.connect.facebook.com","www.facebook.com","facebook.com", "static.ak.fbcdn.net", "www.static.ak.fbcdn.net", "login.facebook.com", "www.login.facebook.com", "fbcdn.net", "www.fbcdn.net", "fbcdn.com", "www.fbcdn.com", "static.ak.connect.facebook.com"]
aftonbladet_domains = ["www.aftonbladet.se", "aftonbladet.se"]
banned_websites=[]



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

banned_websites_complete=ban_choice(ban_facebook, ban_aftonbladet, banned_websites)
quant_domains=len(banned_websites_complete)
edit_hosts(quant_domains)

sys.exit() 
"""
class App():
	def __init__(self, root, content):
		self.starttime=3600
		self.passedtime=0
		self.root = root
		self.content = content
		self.label = ttk.Label(content, text="Time Left: ")
		self.label.grid(column=5, row=5)
		self.update_clock()
		self.root.mainloop()

	def update_clock(self):
		hours_int = (math.floor((self.starttime-self.passedtime)/3600))
		hours = str(hours_int).zfill(2)
		minutes_int = math.floor(((self.starttime-self.passedtime)/60)-hours_int*60)
		minutes = str(minutes_int).zfill(2)
		seconds_int=math.floor((self.starttime-self.passedtime-hours_int*3600-minutes_int*60))
		seconds = str(seconds_int).zfill(2)
		now = (hours + ":" + minutes + ":" + seconds)
		self.label.configure(text=now)
		self.passedtime+=1
		self.root.after(1000, self.update_clock)


root = Tk()
Style(root).theme_use("clam")

content = ttk.Frame(root)
namelbl = ttk.Label(content, text="STUDYBLOCKER")
name = ttk.Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(False)
twovar.set(False)
threevar.set(False)

#t1 = threading.Thread()


one = ttk.Checkbutton(content, text="Block Facebock", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Block Aftonbladet", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Block 9Gag", variable=threevar, onvalue=True)
go = ttk.Button(content, text="Go", command=lambda: App(root,content))
free = ttk.Button(content, text="FREE",command=lambda: time.sleep(5))
cancel = ttk.Button(content, text="Cancel")



content.grid(column=0, row=0)
namelbl.grid(column=0, row=0, columnspan=3)

one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
go.grid(column=5, row=3)
free.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.mainloop()
