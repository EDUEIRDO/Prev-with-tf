import random

class CampoMinado:
    def __init__(self, linhas, colunas, num_minas):
        self.linhas = linhas
        self.colunas = colunas
        self.num_minas = num_minas
        self.grid = [[0 for _ in range(colunas)] for _ in range(linhas)]
        self.criar_minas()
        self.calcular_numeros()

    def criar_minas(self):
        minas_plantadas = 0
        while minas_plantadas < self.num_minas:
            x = random.randint(0, self.linhas - 1)
            y = random.randint(0, self.colunas - 1)
            if self.grid[x][y] != -1:
                self.grid[x][y] = -1
                minas_plantadas += 1

    def calcular_numeros(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.grid[i][j] == -1:
                    continue
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= i + dx < self.linhas and 0 <= j + dy < self.colunas:
                            if self.grid[i + dx][j + dy] == -1:
                                self.grid[i][j] += 1

    def mostrar_tabuleiro(self, mostrar_minas=False):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.grid[i][j] == -1 and not mostrar_minas:
                    print('*', end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print()

# Exemplo de uso:
if __name__ == "__main__":
    campo = CampoMinado(5, 5, 5)
    campo.mostrar_tabuleiro(mostrar_minas=True)
