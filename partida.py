# As oito maneiras de fazer três em linha. Cada casa é (linha, coluna).
VELHA = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
)


class Partida:
    def __init__(self):
        self.tabuleiro = [[""] * 3 for x_ in range(3)]
        self.vez = "X"
        self.encerrada = False
        self.velha = ()

    def jogar(self, linha, coluna):
        if not (0 <= linha < 3 and 0 <= coluna < 3):
            return

        # Se acabou o jogo ou nao tem nenhum espaco vazio, o jogo terminou...
        if self.encerrada or self.tabuleiro[linha][coluna] != "":
            return

        self.tabuleiro[linha][coluna] = self.vez
        self.jogadas += 1

        # Conta as peças do jogador em cada linha, coluna ou diagonal.
        for trio in VELHA:
            pontos = 0

            for lin, col in trio:
                if self.tabuleiro[lin][col] == self.vez:
                    pontos += 1

            if pontos == 3:
                self.velha = trio
                self.encerrada = True
                return

        # Se ninguém venceu após 9 jogadas, deu empate.
        if self.jogadas == 9:
            self.encerrada = True
            return

        # A partida continua. Passa a vez para o outro jogador.
        if self.vez == "X":
            self.vez = "O"
        else:
            self.vez = "X"
