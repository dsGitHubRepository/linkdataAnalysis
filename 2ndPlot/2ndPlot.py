# 2ndPlot.py


# NB: parameter variation L14, L65

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
plt.close()

pathin='../input/log.txt'
datainput=open(pathin,'r')

NolF2=44006  # 30 # 4400644

byteList=[]
rsrcList=[]

for line in range(NolF2):
    linetxt=datainput.readline()
    linetxtSplit=linetxt.split()
    if np.size(linetxtSplit)==10 :
        if linetxtSplit[9] != str('-'):
            rsrc=linetxtSplit[6]
            rsrcstr=str(rsrc)
            rsrcList.append(rsrcstr)
            q2byte=linetxtSplit[9]
            byteList.append(q2byte)


# bandwidth be calculated as sum of bytes/(Number of attempts); So each unique
# resources be identified to compare to count the average bytes transferred 
# during  

# Remove duplicate item from the list                        
rsrcNodupl=list(set(rsrcList))

lprog=np.size(rsrcNodupl)/10
bandwidthList=[]
for lsrc1 in range(np.size(rsrcNodupl)):
    if lsrc1%lprog == 0:  
        print "progress : ", lsrc1/lprog   
    srcitem1=rsrcNodupl[lsrc1]
    srcitem1str=str(srcitem1)  # to be sure
    nc=0
    sumbyte=0.0 
    for lsrc2 in range(np.size(rsrcList)):  
        srcitem2str=rsrcList[lsrc2] 
        if srcitem1str==srcitem2str:
             idxstr=str(lsrc2)
             sumbyte=sumbyte+int(byteList[lsrc2])
             nc=nc+1    # repeated resources count
    byteTotal=sumbyte
    nc2=nc
    byteAvg=byteTotal/nc
    bandwidthList.append(byteAvg)
             
bandwListint=list(map(int,bandwidthList))        
        
pathOband='../output/bandwidth.txt'
dataOband=open(pathOband,'wb')

import pandas as pd

Ntop=200

bandWList=[]
for irsrc in range(Ntop):
    RsrcMaxbw=max(bandwListint)
    idxMaxbw=pd.Series(bandwListint).idxmax()
    topMostRsrc=rsrcNodupl[idxMaxbw+irsrc]     # since the top resources was not dropped in loop iteration
    dataOband.write('%s \n' % topMostRsrc)
    #print "\n top", irsrc+1, ":", topMostRsrc, "bandwidth : ", RsrcMaxbw
    bandwListint.remove(max(bandwListint))     # max bandwidth was dropped during iteration
    bandWList.append(RsrcMaxbw)
    
datainput.close() 
                                             

fig = plt.figure()
width = .45
ind = np.arange(len(bandWList))
plt.subplot(2,1,1)
plt.bar(ind, bandWList, width=width)
plt.title('Resource bandwidth distribution ')
plt.show()

# print np.size(bandWList), bandWList

bandWListFl=[]
for i in range(np.size(bandWList)):
    bwfl=float(bandWList[i])
    bandWListFl.append(bwfl)

bandWListFlNorm=bandWListFl/np.max(bandWListFl)

plt.subplot(2,1,2)
plt.plot(ind,bandWListFlNorm,'r')

red_patch = mpatches.Patch(color='red', label='Normalized to unity')
plt.legend(handles=[red_patch])

plt.savefig("2ndplot.pdf")




