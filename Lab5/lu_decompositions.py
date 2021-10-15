# -*- coding: utf-8 -*-
"""LU_decompositions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vwxasFwyOY5QJifnM6H9JWLTIMk6Mkvs

#**Lab 5 - LU decompositions and Gaussian elimination**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab5"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Nicholas"

last_name="Oxenden"

# Enter your Math 215 section number in between the quotation marks. 

section_number="001"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER! 

BYUNetID="noxenden"

"""**Import NumPy**"""

import numpy as np

"""**Problem 1**"""

def augment(A,b): 
  return np.column_stack([A,b])

"""**Problem 2**"""

def first_column_zeros(A):
  mat=np.copy(A)

  for row in range(1,len(mat)):

    mat[row] = mat[row] - (mat[row,0] / mat[0,0]) * mat[0]

  return mat # Put your return value here.

"""**Problem 3**"""

def row_echelon(A,b): 
  
  A=np.column_stack((A,b))
  B=np.copy(A)  

  for i in range(len(B[0])):
    for j in range(i+1,len(B)):
      m=B[j][i]/B[i][i]
      B[j]=[B[j][k]-m*B[i][k] for k in range(len(B[0]))]
  
  return B # Put your return value here.


A = np.array([[3.,1.,-2.],
              [1.,2.,-5.],
              [2.,-4.,1.]])
b = np.array([1.1,2.,-3.])

row_echelon(A,b)

##################
### Needs Work ###
##################

### i can't equal j

"""**Problem 4**"""

def LU_decomposition(A):

  U=np.copy(A)
  L=np.identity(len(A))
  m,n = U.shape

  for j in range(0,n):
    for i in range(j+1,m):
      L[i][j] = U[i,j] / U[j,j]
      U[i,:] = U[i,:] - L[i,j] * U[j,:]

  return L,U # We've included the return values for you, though your function needs to define them correctly.

"""**Problem 5**"""

def forward_substitution(L,b): # Accepts a lower triangular square matrix L and a vector b, solves Ly=b for y.

  L = L.copy()

  n = len(b)
  y = np.zeros(n, dtype=float)
  
  for i in range(0,n):
    y[i] = ((b[i] - np.dot(y,L[i,:])) / L[i,i])

  return y 

"""**Problem 6**"""

def back_substitution(U,y):    # Accepts an upper triangular square matrix U and a vector b, solves Ux=b for x.
  U = U.copy()
  n = len(y)

  z = np.zeros(n, dtype = float)

  for i in range(n-1,-1,-1):
    z[i] = (y[i] - np.dot(z,U[i,:])) / U[i,i]
    
  return np.array(z)

"""**Problem 7**"""

def LU_solver(A,b): 

  Mat = A.copy()
  
  L,U = LU_decomposition(Mat)

  y = forward_substitution(L,b)

  sol = back_substitution(U,y)

  return sol

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""