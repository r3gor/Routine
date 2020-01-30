from src.actividad import Actividad
from src.rutina import Rutina

__author__ = "Roger Ramos"
__email__ = "yihsic@gmail.com"


def main():
    lista_de_actividades = [Actividad("act A", 6, 4, 3), Actividad("act B", 7, 2, 4), Actividad("act C", 2, 6, 3)]
    print("")
    mi_rutina = Rutina("Mi objetivo!", 4, lista_de_actividades)
    print("cantidad de poms: ", mi_rutina.cant_poms)
    for i in mi_rutina.list_poms:
        print(f"pomodoro {i.ID}: ", i.act.nom)
        print("minutos de trabajo: ", i.MINUTOS_TRABAJO)
        print("minutos de descanso: ", i.MINUTOS_DESCANSO)


if __name__ == '__main__':
    main()
