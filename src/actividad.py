# @Author : Roger Ramos (yihsic@gmail.com)

class Actividad:
    """
    Estructura con atributos controlados para representar una Actividad.

    Note:
        El nombre (nom) de tener mas de 50 caracteres sera solo se tomara
        los 50 primeros.

        Dificultad (dif) no debe ser menor que 0, Urgencia (urg) y Volumen (vol)
        no deben ser menor que 1, caso contrario se lanzará un TypeException

    Args:
        nom (str): Nombre de la actividad.
        dif (int): Dificultad.
        urg (int): Urgencia.
        vol (int): Volumen.

    """

    def __init__(self, nom="(Sin Nombre)", dif=0, urg=1, vol=0):

        self.nom = nom
        self.dif = dif
        self.urg = urg
        self.vol = vol

    def __eq__(self, act):
        return self.nom == act.nom and self.dif == act.dif and self.urg == act.urg and self.vol == act.vol

    @property
    def nom(self):
        return self.__nom.title()

    @nom.setter
    def nom(self, n):
        if not (isinstance(n, str)):
            raise ValueError(f"Nombre: {x} debe ser un string")

        if len(n) > 50:
            self.__nom = n[:50]
            print(f"[!](Nombre supera 50 caracteres): {n} se recortó a 50 caracteres")
        self.__nom = n

    @property
    def dif(self):
        return self.__dif

    @dif.setter
    def dif(self, x):
        if not isinstance(x, int):
            raise TypeError(f"Dificultad de {self.nom}: {x} debe ser un entero")
        if x < 1:
            raise ValueError(f"Dificultad de {self.nom}: {x} debe ser mayor a 1")
        self.__dif = x

    @property
    def urg(self):
        return self.__urg

    @urg.setter
    def urg(self, x):
        if not isinstance(x, int):
            raise TypeError(f"Urgencia de {self.nom}: {x} debe ser un entero")
        if x < 0:
            raise ValueError(f"Urgencia de {self.nom}: {x} debe ser mayor a 1")
        self.__urg = x

    @property
    def vol(self):
        return self.__vol

    @vol.setter
    def vol(self, x):
        if not isinstance(x, int):
            raise TypeError(f"Volumen de {self.nom}: {x} debe ser un entero")
        if x < 0:
            raise ValueError(f"Volumen de {self.nom}: {x} debe ser mayor a 1")
        self.__vol = x
