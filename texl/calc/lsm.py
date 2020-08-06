

from typing import *

import numpy as np
import matplotlib.pyplot as plt


class LSM:
    """Calulating and visualizing LSM for data
    
    """

    def __init__(self, 
                 x:Optional[np.ndarray]=None, 
                 y:Optional[np.ndarray]=None,
                 path:Optional[str]=None, 
                 delimiter:str=",",
                 lsm:bool=False,
                 autoplot:bool=True):

        self.data:Optional[np.ndarray] = None
        self.fig:plt.Figure = plt.figure()
        self.axes = self.fig.add_subplot()
        self._autoplot:bool = autoplot
        
        self._x_raw:Optional[np.ndarray] = x
        self._y_raw:Optional[np.ndarray] = y
        self._a:Optional[float] = None
        self._b:Optional[float] = None

        if path:
            self.data = np.loadtxt(path, delimiter=delimiter).T
            
        if lsm:
            self.lsm()
            
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    #   Utility Methods
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -    
        
    @property
    def a(self):
        return self._a
    
    
    @property
    def b(self):
        return self._b
    
    
    @property
    def params(self):
        return (self._a, self._b)
            

    def get_Y(self, X:np.ndarray) -> np.ndarray:
        # TODO
        if self._a and self._b:
            return self._a + self._b * X
        
        
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    #   LSM Calculation Methods
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
        
    def lsm_xy(self, x, y) -> tuple:
        x:np.ndarray = np.array(x)
        y:np.ndarray = np.array(y)
        n = x.size
        
        self._x_raw = x
        self._y_raw = y
        
        # models Y = a + bX
        sum_x = x.sum()
        sum_y = y.sum()
        sum_xx = (x ** 2).sum()
        dot_xy = np.dot(x, y)
        
        C = n * sum_xx - sum_x ** 2
        a = (sum_xx * sum_y - dot_xy * sum_x) / C
        b = (n * dot_xy - sum_x * sum_y) / C
        
        self._a = a
        self._b = b
        
        if self._autoplot:
            self.plot()
        
        return a, b
          
        
    def lsm_index(self, i_x, i_y) -> tuple:
        
        # TODO
        if self.data is not None:
            return self.lsm_xy(self.data[i_x], self.data[i_y])
        
        
    def lsm(self) -> tuple:
        return self.lsm_xy(self._x_raw, self._y_raw)
    
    
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    #   Visualization Methods
    #   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -
    
    def plot(self, cmp=True) -> None:
        # TODO
        if self._a is None or self._b is None:
            self.lsm()
            
        self.clear_fig()
        x = self._x_raw
        y = self._y_raw
            
        X:np.ndarray = np.linspace(x.min() - 1, x.max() + 1, num=int(x.max() - x.min()) * 10)
        Y:np.ndarray = self._a + self._b * X
        
        self.clear_fig()
        self.axes.scatter(x, y, s=7)
        self.axes.plot(X, Y, color="black", linestyle="dashed")
    
    
    def show(self):
        plt.show()


    #   reset a fig and an axes
    def clear_fig(self) -> None:
        plt.close()
        self.fig:plt.Figure = plt.figure()
        self.axes = self.fig.add_subplot()