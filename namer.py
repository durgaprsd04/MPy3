import os
os.system("ls noise+voice/sampletest_possible/ > list.txt")
fp=open("list.txt")
i=0
for line in fp.readlines():
        i=i+1;
        os.system("mv noise+voice/sampletest_possible/"+line.split('\n')[0]+" "+"noise+voice/sampletest_possible/noise_voice"+str(i)+".mp3")
        
        
