# -*- coding: utf-8 -*-
"""Copy of Plotting_iteration_roundoff.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MnVbt1YtpXneKQFqCKReE_JyVCECUI_Q

#**Lab 3 - Plotting, iteration, and roundoff error**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab3"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Nicholas"

last_name="Oxenden"

# Enter your Math 215 section number in between the quotation marks. 

section_number="001"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER! 

BYUNetID="noxenden"

"""**Import NumPy and PyPlot**"""

import numpy as np
from matplotlib import pyplot as plt

"""**Problem 1**"""

# Plot both functions from Problem 1 here.  Put all of your code to create the plot inside the function below.

def create_plots():

    x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

    y1 = np.sin(x)

    y2 = np.cos(4 * x)

    plt.plot(x,y1)
    plt.plot(x,y2)

    plt.show()

    return None

"""**Problem 2**"""

# Create the scatter plot from Problem 2 here.  Put all of your code to create the plot inside the function below.

def create_scatter_plot():

    x = np.random.normal(scale=1.5, size=500)
    y = np.random.normal(scale=1,size=500)

    plt.plot(x,y,'x',markersize=5,alpha=1)
    plt.show()

    return None

"""**Problem 3**"""

def fact(n):
  if n==0:
    return 0 
  
  else:
    lst = [x for x in range(n,0,-1)]

    result = 1
    for number in lst:
        result = result * number

    return result

"""**Problem 4**"""

def f(x):
   return pow(x,2) + x - 5

a = 0 # Choose a value where f(a)<0 or f(a)>0.
b = 2 # Choose a value where f(b)>0 or f(b)<0 depending on your choice
   # of a above.
n = 100 # Number of iterations you'd like to run the bisection method for.

for i in range(n):
   d = (a + b)/2
   if f(d) < 0:
      a = d
   else:
      b = d
root = d # Replace the value -1 with your approximation to the root of f(x), correct to 12 decimal places.

"""**Problem 5**"""

def g(x):
  return pow(x,4) +- (2 * pow(x,3)) - (17 * pow(x,2)) + 4 * x + 30# Put your return value, i.e. the value of g(x), here.

def g_prime(x):
  return (4 * (pow(x,3)) - (6 * pow(x,2)) - 34 * x + 4) # Put your return value, i.e. the value of the derivative g'(x), here.

"""**Problem 6**"""

def newtons_method(starting_guess,n):
  x_j = starting_guess
  for i in range(n):
      x_j = x_j - (g(x_j) / g_prime(x_j)) 
  return x_j # Put your return value here.

"""**Problem 7**"""

def integration(m):

  E = 1 - (1 / np.exp(1))

  for j in range(1,m+1):
    E = 1 - (j * (E))

  return E

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file. In the "File" menu select "Download .py". The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""