import pygame
from visual import Visual


class TelaPygame:
    def __init__(self, controlador):
        self.controlador = controlador
        self.visual = Visual()

    def clicar(self, posicao):
        if self.visual.botao.collidepoint(posicao):
            self.controlador.reiniciar()
            return

        for linha, coluna, casa in self.visual.casas:
            if casa.collidepoint(posicao):
                self.controlador.jogar(linha, coluna)
                return

    def executar(self):
        relogio = pygame.time.Clock()
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    return
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    self.clicar(evento.pos)
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
                    self.controlador.reiniciar()

            self.visual.desenhar(self.controlador.partida)
            relogio.tick(30)