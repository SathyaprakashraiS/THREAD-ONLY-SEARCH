import threading
import sys
import time
from datetime import datetime

flag=False
cflag=False
now = datetime.now()
start=now.strftime("%H:%M:%S")
def ttime():
	te=0
	global cflag,start
	while(cflag==False):
		te+=1
	finish=now.strftime("%H:%M:%S")
	print("START TIME:",start)
	print("END TIME  :",finish)
	'''
	while(bb>=0 and cflag==False):
		bb+=1
	print("PROGRAM TERMINATED @",bb,"iterations")
	'''
start=now.strftime("%H:%M:%S")
t0=threading.Thread(target=ttime)
t0.start()

maxtime=0
def endprog():
	global maxtime
	time.sleep(10)
	maxtime=1
	return 0
ep=threading.Thread(target=ttime)
ep.start()

tree={1:[2,3,4,1],2:[5,6,7],3:[8,9,10],4:[11,12,13],5:[14,15],6:[16,17,18],7:[20],8:[21,22],9:[23,24],10:[25],11:[26],12:[27,28,29,30],13:[31,32,33],14:[34,35],16:[36,37],37:[38,39],17:[40],18:[41,42],42:[43],20:[44,45]}
m=[]
for i in range(2*len(tree)):
	m.append(0)
mflag=0
q=1

ans=13
#ans=int(input("Enter the node to find:"))
# t0=threading.Thread(target=ttime)
# t0.start()

path=[]
tpath=""
tpath=tpath+str(q)
l=["","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",]
lf=0
w=tree[q]
def dfs(z,mflag,tpath):
	global cflag,flag,maxtime
	mflag+=1
	#print(threading.currentThread().getName())
	if(flag!=True and maxtime==0):
		try:
			a=tree[z]
			tpath=tpath+" "+str(z)
			for i in range(len(a)):
				if(a[i]==ans):
					#t0.terminate()
					flag=True
					cflag=True
					maxtime=1
					print("Found",a[i])
					#print("number loc A:",threading.currentThread().getName(),a[i],lf,mflag)
					#tpath.append(z)
					tpath=tpath+" "+str(a[i])
					print("TPATH",tpath)
					#path.append(a[i])
					# l[lf]=str(l[lf])+","+str(a[i])
					# lf+=1
					#sys.exit()
					#print("All path:",path)
					#print("HERE L")
					#print("LF",l)
					
					#print(threading.currentThread().getName())
					
				else:
					#print("visited ",a[i])
					#flag=dfs(a[i],tree,ans)
					#tpath.append(z)
					m[mflag]=threading.Thread(target=dfs,args=(a[i],mflag,tpath,))
					#print("number loc A:",a[i],lf,mflag,threading.currentThread().getName())
					#print("the lf ",lf)
					# l[lf]=str(l[lf])+","+str(a[i])
					# lf+=1
					m[mflag].start()
					#mflag+=1
					# if(flag==True):
					# 	path.append(a[i])
					# 	return True
		except:
			pass
	else:
		return 0
		#print("empty",z)
if(q==ans):
	flag=True
	cflag=True
	print("FOUND AS TREE BASE",q)
	sys.exit()
for i in range(len(w)):
	#print("visited ",w[i])
	if(w[i]==ans):
		flag=True
		cflag=True
		#path.append(w[i])
		print("FOUND HERE AS LEVEL 2 ROOT",w[i])
	else:
		m[mflag]=threading.Thread(target=dfs,args=(w[i],mflag,tpath,))
		#print("number loc W:",w[i],lf,mflag,threading.currentThread().getName())
		# l[lf]=str(l[lf])+","+str(w[i])
		# lf+=1
		m[mflag].start()
		mflag+=1
		#mflag+=1
		#flag=dfs(w[i],tree,ans)
		# if(flag==True):
		# 	path.append(w[i])
#path.append(q)
#print(l)
#print("mflag",m)
tl=0
#print(m)
#close=0

'''
endit=1
while(endit==1):
	while(tl<len(m)):
		if(m[tl]!=0):
			if(m[tl].is_alive()):
				pass
				#print(m[tl],"alive")
				#close+=1
				#if(close>10000):
				#	pass
			else:
				tl+=1
				#close=0
		else:
			tl+=1
	if(cflag==False and flag==False):
		endit=0
		print(ans,"Not in the tree")
		#print(m)
'''

while(tl<len(m) and maxtime==0):
	if(m[tl]!=0):
		if(m[tl].is_alive()):
			pass
		else:
			tl+=1
	else:
		tl+=1

'''
def bfs(z,tree):
	print(z,tree)
for i in range(len(w)):
	bfs(w[i],tree)
'''