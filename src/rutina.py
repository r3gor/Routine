from src.actividad import Actividad
from src.pomodoro import Pomodoro

__author__ = "Roger Ramos"
__email__ = "yihsic@gmail.com"


def minu_tot_poms(n_poms: int) -> int:
    """
    Calcula la cantidad de minutos totales para
    realizar cierta cantidad de pomodoros (n_poms).

    :param n_poms: Número de pomodoros.
    :return: Cantidad de minutos totales en n_poms.
    """
    return int(30 * n_poms + (n_poms - n_poms % 4) * 10 / 4)


def n_poms(n_horas: int) -> int:
    """
    Calcula la cantidad de pomodoros cuyo tiempo total de
    duración es la mas aproximada a el tiempo especificado.

    :param n_horas: Cantidad de horas
    :return: Cantidad (int) de pomodoros
    """
    n_minu = n_horas * 60
    aprox = round(4 * n_horas * 60 / 130)
    for i in [-1, +1]:
        if abs(n_minu - minu_tot_poms(aprox)) > abs(n_minu - minu_tot_poms(aprox + i)):
            aprox = aprox + i
    return aprox


def gen_poms(cant_poms: int, list_act: list) -> list:
    """
    Retorna lista de objetos Pomodoro necesarios para cada actividad y en el orden que se deben realizar.

    Ordena las actividades según prioridad para el orden (peso orden: urgencia / dificultad),
    la materia con mayor peso orden serán los primeros pomodoros de la lista, por lo tanto, los
    pomodoros que se deben realizar primero.

    Calcula el número de pomodoros para cada actividad segun su prioridad para la cantidad de
    pomodoros (peso poms: dificultad * volumen), creando la cantidad de pomodoros que cada
    actividad debe requerir (de forma que los la suma de las cantidades de todos los pomodoros
    siempre debe ser igual a la cantidad de pomodoros especificada por parámetro)


    :param cant_poms: Cantidad de pomodoros
    :param list_act: Lista de objetos de clase Actividad
    :return: lista de objetos de clase Pomodoro creados
    """
    list_poms = list()
    peso_ord_de_ult_act_agreg = 1000
    for i in range(len(list_act)):
        sum_peso_poms, act_may_peso_ord = 0, Actividad("act_may_peso_ord", 1, 0, 1)
        for j in list_act:
            sum_peso_poms += j.peso_poms
            may_peso_ord = act_may_peso_ord.peso_ord
            act_peso_ord = j.peso_ord
            if may_peso_ord <= act_peso_ord < peso_ord_de_ult_act_agreg:
                act_may_peso_ord = j
        cant_poms_act = round(act_may_peso_ord.peso_poms * cant_poms / sum_peso_poms)
        for k in range(cant_poms_act):
            list_poms.append(Pomodoro(act_may_peso_ord))
        peso_ord_de_ult_act_agreg = act_may_peso_ord.peso_ord
    return list_poms


class Rutina:
    def __init__(self, obj="", hor_durac=1, list_act=None):
        if list_act is None:
            list_act = [Actividad()]
        self.obj = obj
        self.hor_durac = hor_durac
        self.list_act = list_act
        self.cant_poms = n_poms(self.hor_durac)
        self.list_poms = gen_poms(self.cant_poms, self.list_act)
