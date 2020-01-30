from src.actividad import Actividad

__author__ = "Roger Ramos"
__email__ = "yihsic@gmail.com"


class Pomodoro:
    """
    Crea objetos Pomodoro siguiendo la lógica pomodoro, con
    minutos para trabajo (MINUTOS_TRABAJO) y minutos para descanso (
    MINUTOS_DESCANSO).

    Note:
        Los minutos de descanso MINUTOS_DESCANSO es 5 pero cada 4
        pomodoros creados MINUTOS_TRABAJO es 15.

        Los minutos de trabajo MINUTOS_TRABAJO siempre es 25.

    Attributes:
        MINUTOS_TRABAJO (int): Tiempo de trabajo del pomodoro.
        MINUTOS_DESCANSO (int): Tiempo de descanso del pomodoro.
        act (Actividad): Actividad a realizar en el pomodoro.

    Args:
        act (Actividad): Nombre de la actividad
    """
    cant_pom_creados = 0  # member static

    def __init__(self, act):
        self.act = act
        self.MINUTOS_TRABAJO = 25
        self.ID = Pomodoro.cant_pom_creados
        self.MINUTOS_DESCANSO = 15 if ((self.ID + 1) % 4 == 0) else 5
        Pomodoro.cant_pom_creados += 1

    def __eq__(self, pom):
        return self.act == pom.act

    @property
    def act(self):
        return self.__act

    @act.setter
    def act(self, value):
        if not isinstance(value, Actividad):
            raise TypeError(f"Actividad de pomodoro {self.ID} debe contener un objeto de Actividad")
        self.__act = value
