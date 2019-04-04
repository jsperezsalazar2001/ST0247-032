
class Taller10:

    def lcs(self, x, y):
        laTabla = [[0] * (len(y))] * (len(x))

        for i in range(len(x)):
            laTabla[i][0] = 0

        for i in range(len(y)):
            laTabla[0][i] = 0

        for j in range(1, len(y)):
            for i in range(1, len(x)):
                if x[i-1] == y[j-1]:
                    laTabla[i][j] = laTabla[i - 1][j - 1] + 1
                else:
                    laTabla[i][j] = max(laTabla[i - 1][j], laTabla[i][j - 1])
        return laTabla[len(x)-1][len(y)-1]


prueba = Taller10()
print(prueba.lcs("laa", "queholaacque"))