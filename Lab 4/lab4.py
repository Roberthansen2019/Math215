import numpy as np

x_val=1 
y_val=1  

### Problem 1
a = np.mat([[7,-1],[1,-5]])
b = np.mat([6,-4]).T

sol = np.linalg.solve(a,b)

### Problem 2
def jacobi1_iteration(x,y):
    new_x = (1/7) * (6 + y)
    new_y = (1/5) * (x + 4)
    return new_x , new_y

### Problem 3
def jacobi1_method(n):
    x,y = 0,0 
    for i in range(0,n):
        x,y = jacobi1_iteration(x,y)
    return x,y

### Problem 4
print(jacobi1_method(1))
print(jacobi1_method(6))

### Problem 5
def gs1_iteration(x,y):

    new_x = (1/7) * (6 + y)
    new_y = (1/5) * (new_x + 4)

    return new_x , new_y

### Problem 6
def gs1_method(n):
    x,y = 0,0 
    for i in range(0,n):
        x,y = gs1_iteration(x,y)
    return x,y

### Problem 7
for i in range(6):
    print(f"N: {i} {gs1_method(i)}")

### Problem 8
def gs1_error(n):

    a = np.array([x_val,y_val])
    b = np.array(gs1_method(n))

    return np.linalg.norm(a-b)

### Problem 9
def gs2_iteration(x,y):

    new_x = y + 1
    new_y = 5 - (2 * new_x)

    return new_x , new_y

def gs2_method(n):
    x,y = 0,0 
    for i in range(0,n):
        x,y = gs2_iteration(x,y)
    return x,y


a = np.mat([[1,-1],[2,1]])
b = np.mat([1,5]).T
sol = np.linalg.solve(a,b)
x_guess, y_guess = 2, 1

def gs2_error(n):

    a = np.array([x_guess,y_guess])
    b = np.array(gs2_method(n))

    return np.linalg.norm(a-b)


### Problem 10
def gs3_iteration(x,y,z):

    new_x = (-8/5) - ((3 * z) / 5) + ((2 * y) / 5)
    new_y = (102/4) + z - (new_x / 4)
    new_z = (-90 / 4) + ((2 * new_y) / 4) + ((2 * new_x) / 4)

    return new_x, new_y, new_z

def gs3_method(n):
    x,y,z = 0,0,0 
    for i in range(0,n):
        x,y,z = gs3_iteration(x,y,z)
    return x,y,z

print(gs3_method(4))

a = np.mat([[1,-1],[2,1]])
b = np.mat([1,5]).T
sol = np.linalg.solve(a,b)