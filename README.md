# Jogo da velha

Jogo para duas pessoas no mesmo computador, feito em Python com Pygame. X começa. Clique em uma casa livre para jogar. Vence quem alinhar três peças na horizontal, na vertical ou na diagonal.

## Como abrir

Extraia o ZIP e abra um terminal na pasta que contém `main.py`. Os comandos abaixo usam Python 3.12.

**macOS ou Linux**

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

**Windows**

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe main.py
```

Para jogar novamente, clique em **Nova partida** ou pressione **R**. Nas próximas vezes, basta repetir o último comando para abrir o jogo.

## Onde está o padrão GRASP Controller?

| Arquivo | Responsabilidade |
| --- | --- |
| `main.py` | Inicializa o Pygame, cria o controlador e abre a tela. |
| `tela.py` | A classe `TelaPygame` desenha a interface e converte o clique em uma linha e uma coluna. |
| `controlador.py` | A classe `ControladorJogo` recebe os pedidos de jogar e reiniciar. Ela encaminha a jogada à partida ou cria uma nova partida. |
| `partida.py` | A classe `Partida` guarda o tabuleiro e o jogador da vez. Ela valida a jogada e verifica se alguém venceu ou se deu velha. |

**Fala para a apresentação**

> “Usei o padrão GRASP Controller. Quando clico na casa do meio, a tela chama `controlador.jogar(1, 1)`. O controlador entrega o pedido à partida, que verifica se a casa está livre, marca a peça e confere o resultado. Se eu clicar em Nova partida, o mesmo controlador cria uma partida vazia. Desse jeito, consigo testar as regras sem abrir a janela do Pygame.”

**Uma demonstração em cinco cliques**

1. X joga no canto superior esquerdo.
2. O joga no canto superior direito.
3. X joga no centro.
4. O joga no meio da coluna da esquerda.
5. X joga no canto inferior direito e ganha na diagonal.

Clique em uma casa vazia depois da vitória para mostrar que a partida terminou. Pressione **R** e mostre o tabuleiro vazio com X na vez.

Os ícones de X, O, reinício e janela ficam em `assets/`. As licenças das fontes Young Serif e DM Sans estão em `assets/licencas/`.
