import numpy as np
#import matplotlib as plt
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D


def z_function(x,y):
    return np.sin(10*x) * np.cos(10*y)/10

def calculate_gradient(x,y):
    return np.cos(10*x)*np.cos(10*y), -np.sin(5*x)*np.sin(10*y)

x =np.arange(-1, 1, 0.05)
y =np.arange(-1, 1, 0.05)


X, Y = np.meshgrid(x,y)

Z= z_function(X,Y)

current_pos1 = (0.7,0.4,z_function(0.7, 0.4))
current_pos2 = (0.5,-0.1,z_function(0.5, -0.1))
current_pos3 = (-1,-1,z_function(-1, -1))
learning_rate = 0.001

 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d', computed_zorder=False)
for _ in range(1000):
    x_derivative, Y_derivative = calculate_gradient(current_pos1[0], current_pos1[1])
    X_new, Y_new = current_pos1[0]- learning_rate*x_derivative, current_pos1[1]*Y_derivative
    current_pos1 = (X_new, Y_new, z_function(X_new, Y_new))

    x_derivative, Y_derivative = calculate_gradient(current_pos2[0], current_pos2[1])
    X_new, Y_new = current_pos2[0]- learning_rate*x_derivative, current_pos2[1]*Y_derivative
    current_pos2 = (X_new, Y_new, z_function(X_new, Y_new))

    x_derivative, Y_derivative = calculate_gradient(current_pos3[0], current_pos3[1])
    X_new, Y_new = current_pos3[0]- learning_rate*x_derivative, current_pos3[1]*Y_derivative
    current_pos3 = (X_new, Y_new, z_function(X_new, Y_new))
   
    ax.plot_surface(X,Y,Z,cmap="viridis",zorder=0)
    ax.scatter(current_pos1[0], current_pos1[1], current_pos1[2], color= "magenta",zorder=1)
    ax.scatter(current_pos2[0], current_pos2[1], current_pos2[2], color= "green",zorder=1)
    ax.scatter(current_pos3[0], current_pos3[1], current_pos3[2], color= "cyan", zorder=1)
    plt.pause(0.0001)
    ax.clear()



