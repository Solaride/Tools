import scipy.optimize as opt

def fit(f, X, Y):
    optimized_parameters, pcov = opt.curve_fit(
        f,
        X,
        Y
    )

    a = optimized_parameters[0]
    b = optimized_parameters[1]
    c = optimized_parameters[2]

    print("Optimized parameters:")
    print("  a = " + str(a))
    print("  b = " + str(b))
    print("  c = " + str(c))

    return a, b, c
