from abc import ABC, abstractmethod


class TexFigure(ABC):
    
    
    def __init__(self):
        self.contain = []
        
        
    def include(self, *obj):
        for o in obj:
            self.contain.append(o)
            
    
    @abstractmethod    
    def make(self):
        pass