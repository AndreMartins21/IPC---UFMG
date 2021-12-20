# ALUNO: André Augusto Moreira Martins 
# N° DE MATRÍCULA: 2021035144

"""
# Informações: 
Para esse programa, usufruí de três bibliotecas do Python: 
- random: Gerar valor aleatório para os 2 jogadores. (método estático: _escolhe_player())
- os: Limpar a tela do prompt de comando a cada rodada. (método estático: limpa_tela())
- time: Gerar um pequeno delay no começo da jogatina, pra simular carregamento dos dados. (método estático: limpa_tela())
"""

from random import randint
from os import name, system
from time import sleep


class JogoDaVelha:
    def __init__(self):
        self.board = []
        self.player = ""  # Representa qual jogador irá jogar na respectiva rodada
        self.result = ""  # Conterá como foi a vitória: LINHA, COLUNA ou DIAGONAL

    def _monta_board(self) -> None:
        # Montar o tabuleiro
        self.board = [["_-_" for c in range(3)] for l in range(3)]

    def _mostra_board(self, intro:bool = False) -> print:
        """
        intro = Variável booleana para demonstar a introdução do jogo caso seja True.
        """
        print()
        if intro:
            texto = f'{"=" * 26}\n'
            texto += "  JOGO DA VELHA DO ANDRÉ\n"
            texto += f'{"=" * 26}\n\n'
            texto += "Para escolher sua jogada, basta informar espaçadamente a posição x (posição horizontal) e y (posição vertical) em que você queira jogar. \n\n"
            texto += "- Exemplo de posições: 0 1\nPreencherá na linha 0 e na coluna 1 com 'X' ou 'O', a depender de quem for a vez.\n"
            print(texto)
            print("     [0]   [1]   [2]  (Y)\n")
        else:
            print("     [0]   [1]   [2]\n")
        for i, linha in enumerate(self.board):
            print(f"[{i}]  ", end="")
            for ind, valor in enumerate(linha):
                if ind == 2:
                    print(valor, end=" ")
                else:
                    print(valor, end=" | ")
            print("\n")
            if i == 2 and intro:
                print("(X)")
        print()

    @staticmethod
    def _escolhe_player() -> tuple:
        """Escolher aleatoriamente os valores pro player 1 e player 2"""
        itens = ["X", "O"]
        p = randint(0, 1)
        p1, p2 = itens.pop(p), itens[0]
        return p1, p2

    def _troca_player(self) -> None:
        self.player = "X" if self.player == "O" else "O"

    def _player_vence(self) -> bool:
        # Condições de vitória:
        b = self.board  # Variável 'b' pra facilitar a digitação
        v1 = [" X ", " X ", " X "]
        v2 = [" O ", " O ", " O "]

        # LINHAS
        if any([True if b[i] in [v1, v2] else False for i in range(3)]):
            self.result = "LINHA"
            return True

        # COLUNAS
        c = [[b[y][x] for y in range(3)] for x in range(3)]  # Lista contendo as listas das colunas
        if any([True if c[i] in [v1, v2] else False for i in range(3)]):
            self.result = "COLUNA"
            return True

        # DIAGONAL
        d1 = b[0][0] == b[1][1] == b[2][2]
        d2 = b[0][2] == b[1][1] == b[2][0]
        if b[1][1] != "_-_" and (d1 or d2):
            self.result = "DIAGONAL"
            return True
        return False

    def _velha(self) -> bool:
        list_board = [self.board[x][y] for x in range(3) for y in range(3)]  # Lista contendo todos elementos das linhas

        if set(list_board) == {' O ', ' X '}:  # Se o board conter somente X e O, implicará em velha.
            return True
        return False

    @staticmethod
    def _obter_coordenadas() -> tuple:
        try: 
            x, y = input("Informe as coordenadas (X Y): ").split() 
            x, y = int(x), int(y)
        except ValueError:
            print("\n<ERRO> Digite as coordenadas espaçadamente. Como exemplo: 2 2\n")
            return 3, 3 # Forçar um erro para voltar no laço While
        else:
            return x, y

    def _preencher(self, x: int, y: int) -> bool:
        try:
            if self.board[x][y] != "_-_":
                return False
            self.board[x][y] = f" {self.player} "
        except IndexError:
            return False
        else:
            return True

    @staticmethod
    def limpa_tela(intro=False):
        if intro:
            print("\n\nINICIANDO O JOGO DA VELHA...")
            sleep(1.0)
        if name == 'nt': system('cls')
        if name == "posix": system('clear')

    def iniciar(self):
        self._monta_board()
        self._mostra_board(intro=True)
        _ = input("Digite a tecla ENTER para iniciar: ")
        self.limpa_tela(intro=True)

        p1, p2 = self._escolhe_player()
        self.player = p1
        print(f"<> VALORES: \n- Player 1 = ({p1})\n- Player 2 = ({p2})")

        while True:
            self.limpa_tela()
            if self._player_vence():
                print(f"<> O PLAYER '{self.player}' VENCEU POR {self.result}")
                self._mostra_board()
                break
            if self._velha():
                print("\n", "-" * 20, "\n       DEU VELHA\n", "-" * 20)
                self._mostra_board()
                break

            print(f"\n/> Jogada do player {self.player}")
            self._mostra_board()

            x, y = self._obter_coordenadas()

            while not self._preencher(x, y):
                x, y = self._obter_coordenadas()

            if not self._player_vence():
                self._troca_player()


# JOGO
jogo = JogoDaVelha()
jogo.iniciar()