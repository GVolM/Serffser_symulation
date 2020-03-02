# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 10:18:35 2019

@author: vgrigore
surf model
"""
import matplotlib.pyplot as plt
from scipy import optimize
from scipy.interpolate import interp1d as inter
import numpy as np
class surfboard_shape(object):
    def __init__(self):
        self.width=420
        self.length=1600
        self.tail_width=0.85
        self.nose_width=0.62
        self.nose=0
        self.tail=200
        self.mid_shift=-60
        self.L_grid=np.array(range(0,self.length+1))
        self.W_points=[]
    
    def short_board(self):
        x=np.array([0,300,self.length/2+self.mid_shift,self.length-300,self.length])
        
        y=np.array([self.tail/2,self.width*self.tail_width/2,self.width/2,self.width*self.nose_width/2,self.nose])
        f=inter(x,y,kind='cubic')
        self.W_points=f(self.L_grid)
    
    def plot_shape(self):
        fig,ax=plt.subplots(figsize=(10,10))
        ax.plot(self.W_points,self.L_grid)
        ax.plot(-self.W_points,self.L_grid)
        ax.axis('equal')
        ax.grid()
    
    def nose_shape(self,cut_from_nose=200, offset=20):
        self.L_grid=self.L_grid[:-cut_from_nose]
        self.W_points=self.W_points[:-cut_from_nose]
        
        
        
board=surfboard_shape()
board.short_board()

#board.nose_shape()
board.plot_shape()
        
    
    
        
