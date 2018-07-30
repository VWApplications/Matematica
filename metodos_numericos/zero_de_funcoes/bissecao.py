class Bissecao(object):
    """
    Método da Bisseçao
    """

    @classmethod
    def calcula(cls, g, x0, x1, x_tolerance=1e-6, y_tolerance=1e-6):
        """
        Calcula o zero da função de g(x) dentro do intervalo (x0, y0)

        :param g: Uma função de um única variável
        :param x0: Intervalo inicial para a busca do zero da função g(x) (x0, x1)
        :param x1: Intervalo inicial para a busca do zero da função g(x) (x0, x1)
        :param x_tolerance: Tolerância em x (retorna quando o intervalo for
                            menor que x_tolerance)
        :param y_tolerance: Tolerância em y (retorna quando |g(x)| é menor que y_tolerance)

        :return: Retorna o zero da função g(x) (valor de x em que g(x) = 0)
        """

        # Calcula xa/ya e xb/yb
        # xa = Valores de x para que g(x) seja positivo -> g(xa) = ya
        # xb = Valores de x para que g(x) seja negativo -> g(xb) = yb
        if g(x0) < g(x1):
            # Função crescente
            xa, xb = x0, x1
            ya, yb = g(x0), g(x1)
        else:
            # Função é decrescente
            xa, xb = x1, x0
            ya, yb = g(x1), g(x0)

        # Atualiza o intervalo até atingir o critério de parada
        iterations = 0
        while True:
            iterations += 1
            x_average = (xa + xb) / 2
            g_average = g(x_average)

            # Se o ponto médio de y (g_average) for negativo substituimos o xa/ya caso
            # contrario xb/yb
            # Deste modo, sabemos que o zero de g(x) deve estar entre os novos xa e xb.
            if g_average < 0:
                xa, ya = x_average, g_average
            elif g_average > 0:
                xb, yb = x_average, g_average
            else:
                return x_average

            # Critério de parada: |xb - xa| < tolerancia em x ou |g(x)| < tolerancia em y
            if abs(xb - xa) < x_tolerance or abs(g_average) < y_tolerance:
                break

        # Retorna o ponto em que g(x) é praticamente zero
        if abs(ya) < abs(yb):
            return xa
        else:
            return xb
