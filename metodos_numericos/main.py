import numpy

from metodos_numericos.zero_de_funcoes import Bissecao

print("Zero da função de cos(x) no intervalo de 0 a 4")
print("x =", Bissecao.calcula(numpy.cos, 0, 4))
