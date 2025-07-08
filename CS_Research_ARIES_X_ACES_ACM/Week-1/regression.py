def linearRegression(X: np.array, Y: np.array, lr: float, lambda_: float):
    b1 = 0.0
    b0 = 0.0
    n = len(X)
    for _ in range(10000):
        y_pred = b0 + b1 * X
        error = Y - y_pred
        b0-= -2*lr*np.sum(error)/n
        b1 -= -2*lr*np.sum(X * error)/n+2 *lr* lambda_*b1
    return b0,b1