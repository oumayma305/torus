import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy.plotting import plot3d_parametric_surface
from sympy import sin, cos
from sympy.abc import k, h
def f(x,y):
    return x**2 + y**2 + x*y
X = np.arange(-1, 1, 0.01)
Y = np.arange(-1, 1, 0.01)
X, Y = np.meshgrid(X, Y)
Z = f(X, Y)