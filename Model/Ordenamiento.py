import random



class Ordenamiento:
    def __init__(self):
        pass

    def fillList(self, size: int, arreglo):
        cont = size
        for i in range(size):
            ##arreglo.append(i) ##mejor
            ##arreglo.append(random.randint(0, size)) ##promedio
            arreglo.append(cont-1) ##peor
            cont = cont - 1
        return arreglo

    def fillListRadix(self, size: int, arreglo):
        cont = size
        for i in range(size):
            arreglo.append(str(i)) ##mejor
            ##arreglo.append(str(random.randint(0,size))) ##promedio
            ##arreglo.append(str(cont-1)) ##peor
            cont = cont - 1
        return arreglo

    def quicksort(self, L, first, last):
        # definimos los índices y calculamos el pivote
        i = first
        j = last
        pivote = (L[i] + L[j]) / 2

        # iteramos hasta que i no sea menor que j
        while i < j:
            # iteramos mientras que el valor de L[i] sea menor que pivote
            while L[i] < pivote:
                # Incrementamos el índice
                i += 1
            # iteramos mientras que el valor de L[j] sea mayor que pivote
            while L[j] > pivote:
                # decrementamos el índice
                j -= 1
            # si i es menor o igual que j significa que los índices se han cruzado
            if i <= j:
                # creamos una variable temporal para guardar el valor de L[j]
                x = L[j]
                # intercambiamos los valores de L[j] y L[i]
                L[j] = L[i]
                L[i] = x
                # incrementamos y decrementamos i y j respectivamente
                i += 1
                j -= 1

        # si first es menor que j mantenemos la recursividad
        if first < j:
            L = self.quicksort(self,L, first, j)
        # si last es mayor que i mantenemos la recursividad
        if last > i:
            L = self.quicksort(self,L, i, last)

        # devolvemos la lista ordenada
        return L

    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        # create temp arrays
        L = [0] * (n1)
        R = [0] * (n2)

        # Copy data to temp arrays L[] and R[]
        for i in range(0, n1):
            L[i] = arr[l + i]

        for j in range(0, n2):
            R[j] = arr[m + 1 + j]

        # Merge the temp arrays back into arr[l..r]
        i = 0  # Initial index of first subarray
        j = 0  # Initial index of second subarray
        k = l  # Initial index of merged subarray

        while i < n1 and j < n2:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[], if there
        # are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[], if there
        # are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    # l is for left index and r is right index of the
    # sub-array of arr to be sorted

    def mergeSort(selft, arr, l, r):
        if l < r:
            # Same as (l+r)//2, but avoids overflow for
            # large l and h
            m = l + (r - l) // 2

            # Sort first and second halves
            selft.mergeSort(selft,arr, l, m)
            selft.mergeSort(selft,arr, m + 1, r)
            selft.merge(selft,arr, l, m, r)

    def radixSort(self, array):
        n = 0
        for e in array:
            if len(e) > n:
                n = len(e)

        for i in range(0, len(array)):
            while len(array[i]) < n:
                array[i] = "0" + array[i]

        for j in range(n - 1, -1, -1):
            groups = [[] for i in range(10)]

            for i in range(len(array)):
                groups[int(array[i][j])].append(array[i])

            array = []
            for g in groups:
                array += g

        return [int(i) for i in array]
