import sys
from timeit import default_timer

from Model.Ordenamiento import *
from View.View import *


class Controller:
    def __init__(self):
        self.view = View
        self.ordenamiento = Ordenamiento
        self.menuPrincipal()

    def menuPrincipal(self):
        self.view.printConsole("...:::  Bienvenido    :::...")
        option = int(self.view.printMenu(self.view))

        if option == 1:
            secondOption = self.view.prinSecondMenu(self.view)
            print(secondOption)

        elif option == 2:
            secondOption = int(self.view.prinSecondMenu(self.view))


        elif option == 3:
            secondOption = int(self.view.prinSecondMenu(self.view))
            if secondOption == 1:

                array = []
                array = self.ordenamiento.fillListRadix(self.ordenamiento, 4000, array)
                timer = default_timer()
                self.ordenamiento.radixSort(self.ordenamiento, array)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 2:

                array = []
                array = self.ordenamiento.fillListRadix(self.ordenamiento, 40000, array)

                timer = default_timer()
                self.ordenamiento.radixSort(self.ordenamiento, array)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))


            elif secondOption == 3:

                array = []
                array = self.ordenamiento.fillListRadix(self.ordenamiento, 400000, array)
                timer = default_timer()
                self.ordenamiento.radixSort(self.ordenamiento, array)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 4:

                array = []
                array = self.ordenamiento.fillListRadix(self.ordenamiento, 4000000, array)
                timer = default_timer()
                self.ordenamiento.radixSort(self.ordenamiento, array)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 5:

                array = []
                array = self.ordenamiento.fillListRadix(self.ordenamiento, 40000000, array)
                timer = default_timer()
                self.ordenamiento.radixSort(self.ordenamiento, array)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

        elif option == 4:
            secondOption = int(self.view.prinSecondMenu(self.view))
            sys.setrecursionlimit(2000)
            if secondOption == 1:
                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 4000, array)
                timer = default_timer()
                self.ordenamiento.quicksort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 2:

                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 40000, array)
                timer = default_timer()
                self.ordenamiento.quicksort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 3:

                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 400000, array)
                timer = default_timer()
                self.ordenamiento.quicksort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 4:

                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 4000000, array)
                timer = default_timer()
                self.ordenamiento.quicksort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 5:

                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 40000000, array)
                timer = default_timer()
                self.ordenamiento.quicksort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

        elif option == 5:
            secondOption = int(self.view.prinSecondMenu(self.view))

            if secondOption == 1:
                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 4000, array)
                timer = default_timer()
                self.ordenamiento.mergeSort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 2:
                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 40000, array)
                timer = default_timer()
                self.ordenamiento.mergeSort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 3:
                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 400000, array)
                timer = default_timer()
                self.ordenamiento.mergeSort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 4:
                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 400000, array)
                timer = default_timer()
                self.ordenamiento.mergeSort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))

            elif secondOption == 5:
                array = []
                array = self.ordenamiento.fillList(self.ordenamiento, 400000, array)
                timer = default_timer()
                self.ordenamiento.mergeSort(self.ordenamiento, array, 0, len(array) - 1)
                time_final = default_timer()
                self.view.printTime(self.view, (time_final - timer))