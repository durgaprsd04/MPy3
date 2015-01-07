import os
os.system("mkdir music+speech/sampleset");
for i in range(1,7):
        for j in range(1,60):
                sec=j*5
                minutes=sec/60;
                second=sec%60;
                minutesnext=minutes;
                secondnext=second+5;
                if(second>55):
                        secondnext=0;
                        minutesnext=minutes+1;
                os.system("cutmp3 -i music+speech/song"+str(i)+".mp3 -O music+speech/sampleset/music_speech"+str(j)+str(i)+".mp3 -a "+str(minutes)+":"+str(second)+" -b"+ str(minutesnext)+":"+str(secondnext))


