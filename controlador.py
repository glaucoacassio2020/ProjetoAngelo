from partida import Partida


class ControladorJogo:
    """Controlador GRASP. Recebe as ações da tela e coordena a partida."""

    def __init__(self):
        self.partida = Partida()

    def jogar(self, linha, coluna):
        self.partida.jogar(linha, coluna)

    def reiniciar(self):
        self.partida = Partida()
