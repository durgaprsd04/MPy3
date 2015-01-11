import numpy as np
import scipy as sp
def CenterofGravity(data = []):
    n = np.floor(len(data)/576)
    G = np.zeros(n)
    a = 0
    b = 0
    # for finding energy
    E = []
    for i in range(0, n):
        x = data[(i)*576 : (i+1)*576-1]
        E.append(sum(x*x))
    m = np.mean(E)
    var =  np.var(E)

    # finding the center of gravity
    G = []
    for i in range(0, n):
        for j in range(0, 18):
            a = a + j*pow(data[(i)*576 + j + 1], 2)
            b = b + pow(data[(i)*576 + j], 2)
        G.append(a/b)
    u = np.mean(G)
    v1 = np.var(G)

    # finding zero ratio

    f = 10 * np.log10((data)*(data))
    for i in range(0,n-1):
        f[(i*576):(i+1)*576-1] = np.cumsum(f[(i*576):((i+1)*576)-1])
    z = []
    locs1 = []
    locs2 = []
    pks1 = []
    pks2 = []

    for i in range(0,n-3):
        locs1.append(sp.signal.find_cwt_peaks(f[i*576:(i+1)*576-1]))
        locs2.append(sp.signal.find_cwt_peaks(f[(i+1)*576:(i+2)*576-1]))
        pks1.append(f[locs1])
        pks2.append(f[locs2])
        zero = np.zeros(abs( len(locs2) - len(locs1) ))
        if (len(locs1) < len(locs2)):
            locs1.append(zero)
        else:
            locs2.append(zero)
        # I don't know how to change that line
    zr = sum(z[1:len(z)]/len(z))
