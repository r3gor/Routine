from gui.model.model import Model
from gui.view.view_one import PageOne
from gui.view.view_three import PageThree
from gui.view.view_two import PageTwo
from src.actividad import Actividad

__author__ = "Roger Ramos"
__email__ = "yihsic@gmail.com"


class Controller:
    def __init__(self, page_one: PageOne, page_two: PageTwo, page_three: PageThree, model: Model):
        self.page_one = page_one
        self.page_two = page_two
        self.page_three = page_three
        self.model = model
        self.page_one.boton_siguiente.clicked.connect(self.act_boton_continue_page_one)
        self.page_one.show()
        self.lista_actividades = []

    def act_boton_continue_page_one(self):
        try:
            obj = self.page_one.entry_obj.text()
            num_act = int(self.page_one.entry_num_act.text())
            num_hor = int(self.page_one.entry_num_hor.text())
            self.model.set_objetivo(obj)
            self.model.set_num_hor(num_hor)

            self.page_one.close()
            self.page_two = PageTwo(num_act)
            self.page_two.boton_continue.clicked.connect(self.act_boton_continue_page_two)
            self.page_two.show()
        except ValueError:
            self.page_one.show_info("El numero de actividades y horas debe ser un entero mayor a 1.",
                                    "Introduzca los datos correctos.",
                                    "Entrada Invalida")

    def act_boton_continue_page_two(self):
        def is_numeric(n):
            try:
                int(n)
                return True
            except ValueError:
                return False

        try:
            for i in self.page_two.campos_por_materia:

                nom = i["nom"].text()
                urg = i["urg"].text()
                dif = i["dif"].text()
                vol = i["vol"].text()

                if nom == "" or vol == "" or urg == "" or dif == "":
                    raise ValueError("Debe llenar todos los campos (nombre, urgencia, dificultad y volumen) de cada "
                                     "actividad.")

                if not (is_numeric(urg) and is_numeric(dif) and is_numeric(vol)):
                    raise TypeError("Urgencia, dificultad o volumen no puede contener caracteres no numéricos.")

                self.lista_actividades.append(Actividad(nom, int(dif), int(urg), int(vol)))

            self.model.set_lista_actividades(self.lista_actividades)
            self.model.crea_rutina()
            self.page_two.close()

            self.page_three = PageThree(self.model.rutina.list_poms, self.model.rutina.obj)
            self.page_three.show()
        except TypeError as err:
            self.page_two.show_info("Error de Tipo",
                                    "Ingreso un tipo de dato incorrecto.",
                                    err.__str__().capitalize())
        except ValueError as err:
            self.page_two.show_info("Error de Valor",
                                    "Ingreso un valor incorrecto.",
                                    err.__str__().capitalize())
        except Exception as err:
            print("¡Ha ocurrido un error!")
            self.page_two.show_info("Error Inesperado",
                                    "Ocurrio un error.",
                                    err.__str__().capitalize())
