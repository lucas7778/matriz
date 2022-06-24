class Matriz:
    def __init__(self, l1, l2):
        self.__l1 = l1
        self.__l2 = l2

    @property
    def l1(self):
        return self.__l1

    @property
    def l2(self):
        return self.__l2

    @property


    def trafo(self):

        trafo = self.__l1[0] + self.__l2[1]
        return print(f'O valor do trafo é {trafo}')

    def det(self):
        dete = self.__l1[0] * self.__l2[1] - self.__l2[0] * self.__l1[1]
        return print(f'O determinante encontrado foi {dete}')

    def inv(self):
        dete = self.__l1[0] * self.__l2[1] - self.__l2[0] * self.__l1[1]
        if dete != 0:
            inv = [[self.__l2[1]/dete,(-1)*self.__l2[0]/dete],[(-1)*self.__l1[1]/dete,self.__l1[0]/dete]]
            return print(f' A matriz inversa é {inv}')
        else:
            return print('Essa matriz não tem inversa')


if __name__ == "__main__":
    l1 = [1,2]
    l2 = [3,4]
    matriz = Matriz(l1,l2)
    matriz.det()
