from abc import ABC, abstractmethod

class PersonaModelo(ABC):

    def __init__(self,nombre,telefono,direccion):
        self._nombre=nombre
        self._telefono=telefono
        self._direccion=direccion

    @property
    def nombre(self):
        return self._nombre
    
    @abstractmethod
    def mostrar_info(self):
        pass
