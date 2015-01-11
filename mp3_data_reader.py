import numpy as np
import matplotlib.pyplot as plt
import audioread
from utility import pcm2float
temp = bytearray()
f = audioread.audio_open("test.mp3")
framerate = f.samplerate
duration = f.duration
nchannels = f.channels
print("sampling rate = framerate Hz, duration = duration seconds, channels = nchannels".format(**locals()))
#data = np.random.rand(576)

data = []
# Reading in the data
for buf in f.read_data():
        sig = np.frombuffer(buf, dtype='<i2').reshape(-1, nchannels)
        normalized = pcm2float(sig, np.float32)
        for i in range(0,len(normalized)):
            data.append(normalized[i])
# Finding MDCT Coefficients
print len(data)
#print data

#print data
N = len(data)
X = np.zeros(N)
sub_band_len = 18
for i in range(1, N/sub_band_len):
    n = np.arange((i - 1) * sub_band_len + 1, (i + 1) * sub_band_len)
    for k in range(1, 18):
        isum = []
        for j in range((i-1)*sub_band_len + 1, (i+1)*sub_band_len):
            isum.append(data[j] * np.cos((np.pi / sub_band_len) * (j - 1 + 0.5 + sub_band_len / 2) * (k - 1 + 0.5)))
       #print isum
        X[(i-1)*sub_band_len + k] = sum(isum)
        #(data * np.cos((np.pi / sub_band_len) * (n - 1 + 0.5 + sub_band_len / 2) * (k - 1 + 0.5)))
#print len(X)
print len(X)
plt.plot(X)
plt.show()
plt.close()

#Finding Energy of the audio file.
E = np.zeros(np.floor(N / 576))
for i in range(0, int(np.floor(N/576))):
    a = X[i * 576 + 1:((i+1) * 576)]
    E[i] = sum(a*a)
#print E
plt.plot(E)
plt.show()
plt.close()

# To find parameter sequence
W = 30
delta = 30
F = np.append(np.zeros(delta), E)
j = np.arange(1, W)
S = np.zeros(len(E) + delta + W)
for i in range((1+delta), len(F) - W):
    num = sum(F(i + j) * F(i + j - delta))
    den = np.sqrt(sum(F(i + j)*F(i + j))) * np.sqrt(sum(F(i+j - delta) * F(i + j - delta)))
    S[i] = num/den
plt.plot(S)
plt.show()
plt.close()
"""
"""
#print sig
#print temp
