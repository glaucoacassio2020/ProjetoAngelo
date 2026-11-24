import pygame

from controlador import ControladorJogo
from tela import TelaPygame


def main():
    pygame.init()
    controlador = ControladorJogo()
    tela = TelaPygame(controlador)
    tela.executar()
    pygame.quit()


if __name__ == "__main__":
    main()
