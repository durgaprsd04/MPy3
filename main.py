import numpy as np
# import scipy as sp
import matplotlib.pyplot as plt
y = np.random.rand(108)
N = len(y)
sub_band_len = 18
X = np.zeros(108)
# Finding the MDCT Coefficients
for i in range(1, N/sub_band_len):
    n = np.arange((i - 1) * sub_band_len + 1, (i + 1) * sub_band_len)
    for k in range(1, 18):
        X[(i-1)*sub_band_len + k] = sum(y * np.cos(np.pi / sub_band_len * (n - 1 + 0.5 + sub_band_len / 2) * (k - 1 + 0.5)))

# To find Energy
E = np.zeros(np.floor(N / 576))
for i in range(1, np.floor(len(X) / 576)):
    a = X[(i-1) * 576 + 1:(i * 576)]
    E[i] = sum(a*a)

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

# To cluster the parameter sequence
W2 = 30
delta2 = 30
H = []
for i in range(delta2 + 1, len(S) - W2):
    Pn = S[i:W2 - 1]
    Pn_de = S[(i - delta2): (i-delta2) + W2 - 1]
    Z = np.zeros(W2)
    # Whatever I am typing below is wrong
    [v,U] = fcm([Pn;pn_de;Z],2)
    A = ((ones(2,1)*max(U))==U)
    b=0
    b = find(A(:,1));
    if(find(A(:,3))==b):
        H=[H,1]
    else:
       H=[H,0]
# Have a nice day Following is the test code.z

x = np.arange(-1, 1, .01)
y1 = np.sin(x * 2 * np.pi)
plt.plot(y1)
plt.show()
