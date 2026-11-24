from pathlib import Path

import pygame


ASSETS = Path(__file__).with_name("assets")
TINTA = "#202B42"
PAPEL = "#FFFDF5"
FUNDO = "#F7F1E2"
LINHA = "#B6AE99"
CORES = {"X": "#EC733E", "O": "#248B75"}
CASA = 150
GRADE = pygame.Rect(386, 50, 3 * CASA, 3 * CASA)


def imagem(nome):
    return pygame.image.load(ASSETS / nome).convert_alpha()


def escrever(superficie, frase, fonte, posicao, cor=TINTA):
    texto = fonte.render(frase, True, cor)
    superficie.blit(texto, posicao)


class Visual:
    def __init__(self):
        self.janela = pygame.display.set_mode((888, 556))
        pygame.display.set_caption("Jogo da velha")
        pygame.display.set_icon(imagem("icone.png"))

        self.titulo = pygame.font.Font(ASSETS / "YoungSerif.ttf", 68)
        self.aviso = pygame.font.Font(ASSETS / "DMSans.ttf", 30)
        self.texto = pygame.font.Font(ASSETS / "DMSans.ttf", 19)
        self.pequena = pygame.font.Font(ASSETS / "DMSans.ttf", 14)

        self.botao = pygame.Rect(44, 444, 274, 56)
        self.seta = imagem("reiniciar.png")
        self.pecas = {}
        self.miniaturas = {}
        for simbolo in ("X", "O"):
            original = imagem(simbolo.lower() + ".png")
            self.pecas[simbolo] = pygame.transform.smoothscale(original, (104, 104))
            self.miniaturas[simbolo] = pygame.transform.smoothscale(original, (44, 44))

        self.casas = []
        for linha in range(3):
            for coluna in range(3):
                x = GRADE.x + coluna * CASA
                y = GRADE.y + linha * CASA
                casa = pygame.Rect(x, y, CASA, CASA)
                self.casas.append((linha, coluna, casa))

        self.fundo = self.criar_fundo()

    def criar_fundo(self):
        fundo = pygame.Surface(self.janela.get_size())
        fundo.fill(FUNDO)
        fundo.blit(self.miniaturas["X"], (44, 52))
        fundo.blit(self.miniaturas["O"], (93, 52))
        escrever(fundo, "2 JOGADORES", self.pequena, (154, 64))
        escrever(fundo, "Jogo da", self.titulo, (42, 108))
        escrever(fundo, "velha.", self.titulo, (42, 177))
        escrever(fundo, "Alinhe três peças para vencer.", self.texto, (45, 276))
        pygame.draw.line(fundo, LINHA, (44, 329), (318, 329))

        pygame.draw.rect(fundo, TINTA, GRADE.move(5, 6), border_radius=18)
        pygame.draw.rect(fundo, PAPEL, GRADE, border_radius=18)
        pygame.draw.rect(fundo, TINTA, GRADE, 3, 18)
        for i in (1, 2):
            x = GRADE.left + i * CASA
            y = GRADE.top + i * CASA
            pygame.draw.line(fundo, LINHA, (x, GRADE.top + 12), (x, GRADE.bottom - 12), 2)
            pygame.draw.line(fundo, LINHA, (GRADE.left + 12, y), (GRADE.right - 12, y), 2)
        return fundo

    def desenhar_aviso(self, partida):
        cor = CORES[partida.vez]
        if partida.trinca:
            frase = f"{partida.vez} venceu!"
        elif partida.encerrada:
            frase = "Deu velha!"
            cor = "#DAAC3C"
        else:
            frase = f"Vez de {partida.vez}"

        pygame.draw.rect(self.janela, cor, (44, 363, 8, 29), border_radius=4)
        escrever(self.janela, frase, self.aviso, (65, 353))

    def desenhar_botao(self, mouse):
        cor = TINTA
        if self.botao.collidepoint(mouse):
            cor = "#384661"
        pygame.draw.rect(self.janela, cor, self.botao, border_radius=12)
        self.janela.blit(self.seta, (62, 460))
        escrever(self.janela, "Nova partida", self.texto, (98, 458), PAPEL)
        pygame.draw.rect(self.janela, "#8490A4", (273, 458, 28, 28), 1, 6)
        escrever(self.janela, "R", self.pequena, (282, 462), PAPEL)

    def desenhar(self, partida):
        mouse = pygame.mouse.get_pos()
        self.janela.blit(self.fundo, (0, 0))
        self.desenhar_aviso(partida)
        self.desenhar_botao(mouse)

        for linha, coluna, casa in self.casas:
            simbolo = partida.tabuleiro[linha][coluna]
            interior = casa.inflate(-14, -14)
            if (linha, coluna) in partida.trinca:
                pygame.draw.rect(self.janela, "#FAE5A3", interior, border_radius=14)
            elif not partida.encerrada and not simbolo and casa.collidepoint(mouse):
                pygame.draw.rect(self.janela, FUNDO, interior, border_radius=14)

            if simbolo:
                peca = self.pecas[simbolo]
                self.janela.blit(peca, peca.get_rect(center=casa.center))

        pygame.display.flip()