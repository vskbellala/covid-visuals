from scipy.integrate import odeint
import numpy as np


# solve is the main function
# params: (b-constant, k-constant, [s(0), i(0), r(0)], # of days, # of datapoints)
# return: [t values, s datapoints, i datapoints, r datapoints]
def solve(b, k, x0, days, datapoints):
    def model(n, m):

        s = n[0]
        i = n[1]
        r = n[2]

        dsdt = -b * s * i
        didt = (b * s * i) - (k * i)
        drdt = k * i

        return [dsdt, didt, drdt]

    t = np.linspace(0, days, datapoints)
    x = odeint(model, x0, t)
    return [t, x[:, 0], x[:, 1], x[:, 2]]
