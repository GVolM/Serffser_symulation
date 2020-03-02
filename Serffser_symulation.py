# -*- coding: utf-8 -*-
"""
Serffser_symulation
software utility for optimysing surfboard shape for defined wave
Created on Fri Feb 28 19:03:34 2020

@author: GVolM
"""
import time
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

class Wave(object):
    def __init__(self):
        self.profile_X=np.arange(-5,6,1)
        self.profile_Y=np.array([0,1,1,2,3,5,8,13,21,34,55])
        self.type='Eisbach'
        self.length=10
        
    def plot_3D(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        X, Y = np.meshgrid(self.profile_X, np.arange(0,self.length,0.5))
        Z=[]
        for item in  np.arange(0,self.length,0.5):
            Z.append(self.profile_Y)
            
        Z=np.array(Z)
        
        ax.plot_surface(X, Y, Z, cmap='viridis',
                       linewidth=0, antialiased=False)
        
        
        alpha=0
        phi=np.pi/6
        X_plane=np.arange(-5,self.length-5,1)
        Y_plane=X_plane*np.tan(alpha)+5 #you can better
        X_plane,Y_plane=np.meshgrid(X_plane,Y_plane)
        Z_plane=[] #funktion
        for item in np.arange(0,self.length,1):
            Z_plane.append(np.arange(0,50,5)*np.cos(phi)+10)
        Z_plane=np.transpose(np.array(Z_plane))
        print(Y_plane)
        ax.plot_surface(X_plane, Y_plane, Z_plane, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
        plt.show()        
        
wave=Wave()
wave.plot_3D()