import unittest

from src.actividad import Actividad

__author__ = "Roger Ramos"
__email__ = "yihsic@gmail.com"


class TestActividad(unittest.TestCase):

    def setUp(self):
        self.list_act = [Actividad("mi actividad A", 6, 4, 3), Actividad("mi AcTividad b", 7, 2, 4),
                         Actividad("mI actiVidad c", 2, 6, 3)]

    def test_autoformato_nombre(self):
        """" check correcto auto formato en el nombre de las actividades """
        noms = ["Mi Actividad A", "Mi Actividad B", "Mi Actividad C"]
        for i in range(len(self.list_act)):
            self.assertEqual(self.list_act[i].nom, noms[i])


if __name__ == '__main__':
    unittest.main()
