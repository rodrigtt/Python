from random import randint
from math import fsum, degrees
import numpy as np

"Função: Produto interno Max das Matrizez(Procedural)"
def p_i_max_proce(x,y):
    pass



'Função: Produto interno Usual de Matrizes (Procedural)'
def produto_interno_usual_procedural(x, y):
    resultado = 0
    for n in range(len(x)):
        resultado_linha = fsum(x[n][k] * y[n][k] for k in range(len(x[0])))
        resultado += resultado_linha
    return resultado

'Função: Produto interno Usual de Matrizes OO'
def produto_interno_usual(x, y):
    resultado = 0
    for n in range(len(x.matrix)):
        resultado_linha = fsum(x.matrix[n][k] * y.matrix[n][k] for k in range(len(x.matrix[0])))
        resultado += resultado_linha
    return resultado

'Função Imprime Matriz Estrutura'
def i_matriz_qualquer(self):
    print("\n\t\t\tMatriz({0}x{1}):".format(len(self.matrix), len(self.matrix[0])))
    for i in range(len(self.matrix)):
        print('\tlinha {0}'.format(i + 1), self.matrix[i])
    print('')

'Função Imprime Matriz Sem Estrutura'
def i_matriz_qual_SemEst(self):
    print("\n\t\t\tMatriz({0}x{1}):".format(len(self), len(self[0])))
    for i in range(len(self)):
        print('\tlinha {0}'.format(i + 1), self[i])
    print('')



'Classe de Matrizes'
class Matrix:
    def __init__(self, linha, coluna):
        self.matrix = np.array([[0 for i in range(coluna)] for i in range(linha)])

    @property
    def linha(self):
        print("A quantidade de linhas da matriz é: {}".format(len(self.matrix)))

    @property
    def coluna(self):
        print("A quantidade de colunas da matriz é: {}".format(len(self.matrix[0])))

    '''Função que Imprime a Matriz'''
    @property
    def imprime(self):
        i_matriz_qualquer(self)

    @property
    def transposta(self):
        z = np.array([[0 for i in range(len(self.matrix))] for i in range(len(self.matrix[0]))])
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                z[j][i] = self.matrix[i][j]
        print('\n\t A transposta da Matriz:')
        i_matriz_qual_SemEst(z)

    'Norma de Uma Matriz induzida pelo produto interno Usual'
    @property
    def norma(self):
        norma_ao_quadrado = produto_interno_usual(self, self)
        norma = np.sqrt(norma_ao_quadrado)
        print('\n\t A norma da matriz é: {}'.format(norma))
        print('')

    @property
    def inversa(self):
        z = np.linalg.inv(self.matrix)
        i_matriz_qual_SemEst(z)

    '''Função que soma duas Matrizes'''
    def soma(self, y):
        if (len(self.matrix)) == (len(y.matrix)) and (len(self.matrix[0])) == (len(y.matrix[0])):
            z = self.matrix + y.matrix
            print('\n\t A Soma das Matrizes:')
            i_matriz_qual_SemEst(z)
        else:
            print('\n\tAs matrizes não são iguais. Não podem ser somadas!!')

    def subtrai(self, y):
        if (len(self.matrix)) == (len(y.matrix)) and (len(self.matrix[0])) == (len(y.matrix[0])):
            z = self.matrix - y.matrix
            print('\n\t A Subtração das Matrizes:')
            i_matriz_qual_SemEst(z)
        else:
            print('\n\tAs matrizes não são iguais. Não podem ser subtraidas!!')

    def multiplica_numero(self, y):
        z = y*self.matrix
        print('\n\t A Multiplicação da Matriz pelo escolar {}:'.format(y))
        i_matriz_qual_SemEst(z)

    '''Função que multiplica duas matrizes'''
    def multiplicacao_matriz(self, y):
        if len(self.matrix[0]) == len(y.matrix):
            z = np.array([[ 0 for i in range (len(y.matrix[0]))]for i in range (len(self.matrix))])
            for n in range(len(self.matrix)):
                for p in range(len(y.matrix[0])):
                    z[n][p] = fsum ((self.matrix[n][k])*(y.matrix[k][p])for k in range(len(self.matrix[0])))
            print('\n\nA Multiplicação das Matrizes:')
            i_matriz_qual_SemEst(z)
        else:
                print('\n\tNão é possível multiplicar as matrizes! Não são compatíveis.')

    "Produto interno usual entre duas Matrizes"
    def produto_interno(self, y):
        if len(self.matrix) == len(y.matrix) and len(self.matrix[0]) == len(y.matrix[0]):
            resultado = produto_interno_usual(self, y)
            print('\n\t O produto interno usual entre as duas matrizes é: {}\n'.format(resultado))

        else:
            print("\n\t As matrizes não pertencem ao mesmo espaço vetorial.")
            print("\n\t Logo não podem ser operadas pelo produto interno.\n")

    "Função Angulo entre Matrizes"
    def angulo(self, y):
        if len(self.matrix) == len(y.matrix) and len(self.matrix[0]) == len(y.matrix[0]):
            a = np.sqrt(produto_interno_usual(self,self))
            b = np.sqrt(produto_interno_usual(y,y))
            c = produto_interno_usual(self,y)
            angulo = np.arccos(c /(a*b))
            print('\n\t O ângulo entre as matrizes é: {} graus \n'.format(degrees(angulo)))

    "Função Distancia entre Matrizes"
    def dist(self, y):
        if len(self.matrix) == len(y.matrix) and len(self.matrix[0]) == len(y.matrix[0]):
            z = self.matrix - y.matrix
            resultado = np.sqrt(produto_interno_usual_procedural(z, z))
            print("\n\t A distância entre as matrizes é: {}".format(resultado))
        else:
            print("\n \t Impossível calcular as distâncias entre as matrizes. Não são do"
                  "mesmo espaço vetorial")


"Gera uma matriz com coeficientes aleatórios."
class Matriz_Aleatoria(Matrix):
    def __init__(self, linha, coluna):
        super().__init__(linha, coluna)
        self.matrix = np.array([[ randint(-100,100) for i in range (coluna)]for i in range (linha)])
        i_matriz_qualquer(self)

"Gera uma matriz com coeficientes nulos."
class Matriz_Nula(Matrix):
    def __init__(self, linha, coluna):
        super().__init__(linha, coluna)
        i_matriz_qualquer(self)

"Cria sua matrix"
class Entra_Matriz(Matrix):
    def __init__(self, linha, coluna):
        super().__init__(linha, coluna)
        for n in range(len(self.matrix)):
            for k in range(len(self.matrix[0])):
                self.matrix[n][k] = input("\t Digite o coeficiente {}x{} da Matrix({}x{}): ".format(n + 1, k+1, len(self.matrix), len(self.matrix[0])))
        print("\n\t Matriz inserida com sucesso: ")
        i_matriz_qualquer(self)
        print('')