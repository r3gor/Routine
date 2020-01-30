import unittest

from src.actividad import Actividad
from src.pomodoro import Pomodoro
from src.rutina import gen_poms
from src.rutina import minu_tot_poms
from src.rutina import n_poms

__author__ = "Roger Ramos"
__email__ = "yihsic@gmail.com"


class TestRutina(unittest.TestCase):

    def test_n_poms_aprox_mejorado(self):
        self.assertEqual(n_poms(1), 2)
        self.assertEqual(n_poms(2), 4)
        self.assertEqual(n_poms(3), 6)
        self.assertEqual(n_poms(4), 7)
        self.assertEqual(n_poms(5), 9)
        self.assertEqual(n_poms(6), 11)
        self.assertEqual(n_poms(7), 13)
        self.assertEqual(n_poms(8), 15)

    def test_minu_tot_poms(self):
        self.assertEqual(minu_tot_poms(1), 30)
        self.assertEqual(minu_tot_poms(4), 130)
        self.assertEqual(minu_tot_poms(8), 260)
        self.assertEqual(minu_tot_poms(9), 290)
        self.assertEqual(minu_tot_poms(10), 320)
        self.assertEqual(minu_tot_poms(11), 350)
        self.assertEqual(minu_tot_poms(12), 390)
        self.assertEqual(minu_tot_poms(24), 780)

    def test_gen_poms(self):
        list_act = [Actividad("mi actividad A", 6, 4, 3), Actividad("mi AcTividad b", 7, 2, 4),
                    Actividad("mI actiVidad c", 2, 6, 3)]
        cant_poms = 7
        list_poms = gen_poms(cant_poms, list_act)

        # check cantidad exacta de pomodoros creados
        self.assertEqual(len(list_poms), cant_poms)

        # check cantidad de pomodoros creados para cada actividad
        indx = [2, 4, 1]
        for i in range(len(list_act)):
            self.assertEqual(list_poms.count(Pomodoro(list_act[i])), indx[i])

        # check orden de pomodoros creados para cada actividad
        self.assertTrue(
            list_poms.index(Pomodoro(list_act[2])) < list_poms.index(Pomodoro(list_act[0])) < list_poms.index(
                Pomodoro(list_act[1])))


if __name__ == '__main__':
    unittest.main()
