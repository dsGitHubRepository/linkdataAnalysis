# 1stPlot.py


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
plt.close()

pathin='../input/log.txt'
datainput=open(pathin,'r')

Nol=4400644   # 4400644
iplist=[]
for i in range(Nol):
    line=datainput.readline()
    linesplit=line.split()
    host=linesplit[0]
    iplist.append(host)
datainput.close()

from collections import Counter
iplistcounter=Counter(iplist)

ipTop=200

ip_mostcommon=iplistcounter.most_common(ipTop)

pathout='../output/hosts.txt'
dataout=open(pathout,'wb')

freqList=[]
ipList=[]


for i in range(ipTop):
    a=ip_mostcommon[i]
    ipa=a[0]; freqa=int(a[1])
    dataout.write('%s,%d' % (ipa,freqa))
    freqList.append(freqa)
    ipList.append(ipa)
    
dataout.close() 

fig = plt.figure()
width = .45
ind = np.arange(len(freqList))
plt.subplot(2,1,1)
plt.bar(ind, freqList, width=width)

plt.title('Distribution of host activity')
#plt.xticks(ind + width / 2, ipList)
#fig.autofmt_xdate()
plt.show()
plt.savefig("1stplot.pdf")


ipListF=[]
for i in range(np.size(freqList)):
    ipF=float(freqList[i])
    ipListF.append(ipF)
    

plt.subplot(2,1,2)
plt.plot(ind,ipListF/np.max(ipListF),'b')
red_patch = mpatches.Patch(color='blue', label='Normalized to unity')
plt.legend(handles=[red_patch])
plt.show()
plt.savefig("1stplot.pdf")





