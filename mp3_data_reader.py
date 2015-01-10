import numpy as np
import audioread
from utility import pcm2float
temp = bytearray()
f = audioread.audio_open("test.mp3")
framerate = f.samplerate
duration = f.duration
nchannels = f.channels
print("sampling rate = framerate Hz, duration = duration seconds, channels = nchannels".format(**locals()))
fp = open('content.txt', 'w')
for buf in f.read_data():
        sig = np.frombuffer(buf, dtype='<i2').reshape(-1, nchannels)
        normalized = pcm2float(sig, np.float32)  
        print normalized
#print sig
#print temp
