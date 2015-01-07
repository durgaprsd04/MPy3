import numpy as np


class clustering:


    def fuzzy_c_means_clustering(data, C):
        N = len(data)
        f = 2
        e = .00001
        limit = 100
        U0 = np.random.rand(C, N)
        for i in range(0, C):
            U0[i] = U0[i] / sum(U0[0, :])
        for i in range(0, limit):
            mf = np.power(U0, f)
            s = sum(np.transpose(U0))
            # for calculating the cluster center
            v = (mf*np.transpose(data))/(np.transpose(s))
            dist = np.zeros(C, N)
            for k in range(0, C):
                dist[k, :] = np.transpose(abs(v[k] - data))
            tmp = np.power(dist, (-2/(f-1)))
            # Using new center to calculate the memebership matrix.
            U1 = tmp/(np.ones(C, 1)*sum(tmp))
            if (abs(U1 - U0) < e):
                break
            U0 = U1

    # A lot of things are in doubt. I will check this later on.
    def k_means_clustering(data, k):
        km = []
        dats = data
        dats.sort()
        a0 = dats[0]
        dats.remove(a0)
        datq = abs(dats - dats.append(a0))
        datq = datq[1:len(datq) - 1]
        km.append(dats[1])
        for i in range(0, k-1):
            km.append(dats[min(datq.index(max(datq)))+1])
            datq[min(dats.index(max(datq)))] = 0
        k0 = np.zeros(1, len(km))
        U = np.zeros(k, len(data))
        # To check number of iteration required
        m = 0
        while sum(km != k0):
            k0 = km
            for i in range(0, len(data)):
                # To find minimum distant entries
                temp = max( data.index(min(abs(km-data[i]))))
                U[:,i]=np.zeros(k, 1)
                U[temp, i] = data[i]

                if (len(

        pass

    def expectation_maximization_clustering():
        pass

    def hierarcichal_clustering():
        pass
