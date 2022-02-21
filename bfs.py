import threading
from datetime import datetime

flag=False
cflag=False
bb=0
now = datetime.now()
start=now.strftime("%H:%M:%S")
def ttime():
	te=0
	global bb,cflag,start
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

tree={1:[2,3,4],2:[5,6,7],3:[8,9,10],4:[11,12,13],5:[14,15],6:[16,17,18],7:[20],8:[21,22],9:[23,24],10:[25],11:[26],12:[27,28,29,30],13:[31,32,33],14:[34,35],16:[36,37],37:[38,39],17:[40],18:[41,42],42:[43],20:[44,45]}
q=1
ans=43
#ans=int(input("Enter the node to find:"))

tpath=[]
tpath.append(q)
#tpath=tpath+str(q)
tocheck=[]
def bfs(z,tpath):
	global flag,cflag
	if(flag==False):
		try:
			a=tree[z]
			for i in range(len(a)):
				tpath.append(a[i])
				#tpath=tpath+" "+str(a[i])
				if(a[i]==ans):
					flag=True
					cflag=True
					print("Found",a[i])
					print("TPATH",tpath)
					return 0
				else:
					tocheck.append(a[i])
			#for i in range(len(a)):
			#	bfs(a[i],tpath)
		except:
			return 0

if(q==ans):
	flag=True
	cflag=True
	print("FOUND AS TREE BASE",q)
w=tree[q]
for i in range(len(w)):
	tpath.append(w[i])
	#tpath=tpath+" "+str(w[i])
	if(w[i]==ans):
		flag=True
		#tpath=tpath+" "+str(w[i])
		print("FOUND HERE AS LEVEL 2 ROOT",w[i])
for i in range(len(w)):
	bfs(w[i],tpath)

while(len(tocheck)>0):
	i=0
	bfs(tocheck[i],tpath)
	tocheck.pop(i)

cflag=True
t0.join()
if(flag!=True):
    print(ans,"not found")