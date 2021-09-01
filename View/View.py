class View:
    def __init__(self):
        pass

    def printConsole(self: str):
        return print(self)

    def captureInt(self, message: str):
        res = input(message)
        while not res.isnumeric():
            res = input(message)
        return res

    def printMenu(self):
        print("\n" +
              "1. ORDENAMIENTO BURBUJA.\n" +
              "2. ORDENAMIENTO SELECCION.\n" +
              "3. ORDENAMIENTO RADIX.\n" +
              "4. ORDENAMIENTO QUICKSORT.\n" +
              "5. ORDENAMIENTO MERGESORT\n" +
              "________________________________________________________________________________________________________________")
        return self.captureInt(self, "SELECCIONE UNA OPCION: ")

    def prinSecondMenu(self):
        print(
            "________________________________________________________________________________________________________________")
        print("\n" +
              "1. 4000 DATOS\n" +
              "2. 40000 DATOS.\n" +
              "3. 400000 DATOS.\n" +
              "4. 4000000 DATOS.\n" +
              "5. 40000000 DATOS.\n" +
              "________________________________________________________________________________________________________________")
        return self.captureInt(self, "SELECCIONE UNA OPCION: ")

    def printTime(self, time: int):
        print("EL PROGRAMA SE DEMORO:", str(time) + " segundos.")
