import numpy as np

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
print(x,y)

def gradient_descent(x,y,lr= 0.01, epochs=1000):
    m = 0.0
    b = 0.0

    for epoch in range(epochs):
        y_pred = m*x + b
        error = y - y_pred
        cost = np.mean(error**2)

        dm = -2*np.mean((y-y_pred)*x)
        db = -2*np.mean((y-y_pred))

        m = m - dm*lr
        b = b - db*lr
        print(f" epoch : {epoch}, m = {m}, b = {b}, cost = {cost} ")
    

gradient_descent(x,y)