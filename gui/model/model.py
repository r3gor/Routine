# @Author : Roger Ramos (yihsic@gmail.com)

from src.rutina import Rutina


class Model:
    def __init__(self):
        self.lista_de_actividades = []
        self.objetivo = ""
        self.rutina = None
        self.num_hor = 0

    def set_lista_actividades(self, lista_de_actividades):
        self.lista_de_actividades = lista_de_actividades

    def set_objetivo(self, obj):
        self.objetivo = obj

    def set_num_hor(self, num_hor):
        self.num_hor = num_hor

    def crea_rutina(self):
        self.rutina = Rutina(self.objetivo, self.num_hor, self.lista_de_actividades)
