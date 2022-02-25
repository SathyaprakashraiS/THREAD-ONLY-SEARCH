import threading
import sys
import time
import os
from datetime import datetime

flag=False
cflag=False
now = datetime.now()
#start=now.strftime("%H:%M:%S")
start = time.time()
def ttime():
	te=0
	global cflag,start
	while(cflag==False):
		te+=1
	#finish=now.strftime("%H:%M:%S")
	#print("END TIME  :",finish)
	finish = time.time()
	elapsedTime = finish - start
	print("Elapsed Time = %s" % elapsedTime)
	#time.sleep(2)
	os._exit(1)
#start=now.strftime("%H:%M:%S")
t0=threading.Thread(target=ttime)
t0.start()

maxtime=0
def endprog():
	#print("START TIME:",start)
	global maxtime,flag,cflag
	time.sleep(5)
	if(cflag==False and flag==False):
		maxtime+=1
		#finish=now.strftime("%H:%M:%S")
		print("node not found")
		finish = time.time()
		elapsedTime = finish - start
		print("Elapsed Time = %s" % elapsedTime)
		time.sleep(1)
		os._exit(1)

ep=threading.Thread(target=endprog)
ep.start()

tree={1:[2,3,4,1],2:[5,6,7],3:[8,9,10],4:[11,12,13],5:[14,15],6:[16,17,18],7:[20],8:[21,22],9:[23,24],10:[25],11:[26],12:[27,28,29,30],13:[31,32,33],14:[34,35],16:[36,37],37:[38,39],17:[40],18:[41,42],42:[43],20:[44,45]}
m=[]
for i in range(2*len(tree)):
	m.append(0)
mflag=0
q=1

ans=444
#ans=int(input("Enter the node to find:"))
# t0=threading.Thread(target=ttime)
# t0.start()
print("Searching...")

tpath=""
tpath=tpath+str(q)

w=tree[q]
def dfs(z,mflag,tpath):
	global cflag,flag,maxtime
	mflag+=1
	if(flag!=True and maxtime==0):
		try:
			a=tree[z]
			tpath=tpath+" "+str(z)
			for i in range(len(a)):
				if(a[i]==ans):
					print("Found",a[i])
					tpath=tpath+" "+str(a[i])
					print("TPATH",tpath)
					flag=True
					cflag=True
					maxtime=1
				else:
					m[mflag]=threading.Thread(target=dfs,args=(a[i],mflag,tpath,))
					m[mflag].start()
		except:
			pass
	else:
		return 0
if(q==ans):
	flag=True
	cflag=True
	print("FOUND AS TREE BASE",q)
	sys.exit()
for i in range(len(w)):
	if(w[i]==ans):
		flag=True
		cflag=True
		print("FOUND HERE AS LEVEL 2 ROOT",w[i])
	else:
		m[mflag]=threading.Thread(target=dfs,args=(w[i],mflag,tpath,))
		m[mflag].start()
		mflag+=1
tl=0
while(tl<len(m) and maxtime==0):
	if(m[tl]!=0):
		if(m[tl].is_alive()):
			pass
		else:
			tl+=1
	else:
		tl+=1
if(cflag==False and flag==False and maxtime!=0):
	print("node not found")