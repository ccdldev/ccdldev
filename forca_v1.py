# -*- coding: utf-8 -*-

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:

    #Metodo Construtor
    def __init__(self, word):
        self.word = word
        letters = []
        letters[:0] = word
        self.lista = letters
        under_lines = []
        for i in letters:
            under_lines.append('_')
        self.under_list = under_lines
        self.letras_corretas = []
        self.letras_incorretas = []
        self.tentativas = 0

    #Método para adivinhar a letra
    def guess(self, letter):
        self.letter = letter
        verifica_letra = 0
        index = 0
        for i in self.lista:
            if str(letter) == str(i):
                if self.under_list[index] == str('_'):
                    self.under_list[index] = str(letter)
                verifica_letra += 1
            index += 1
        if verifica_letra > 0:
            self.letras_corretas.append(letter)
        else:
            self.letras_incorretas.append(letter)
            self.tentativas += 1

    #Método para verificar se o jogo terminou
    def hangman_over(self):
        if self.tentativas == 6:
            timebreak = 2
            return timebreak

    #Método para verificar se o jogador venceu
    def hangman_won(self):
        under_count = self.under_list.count('_')
        if int(under_count) == 0:
            timebreak = 1
            return timebreak

    #Método para nao mostrar a letra no board
    #def hide_word(self):


    #Metodo para checar o status do game e imprimir o board na tela
    def print_game_status(self, tentativas):
        print(board[tentativas])
        print('Palavra:')
        print(self.under_list)
        print('Letras corretas:')
        print(self.letras_corretas)
        print('Letras incorretas:')
        print(self.letras_incorretas)

#Funcao para ler uma palavra de forma aleatoria do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

#Funcao Main - Execucao do Programa
def main():
    # Objeto
    game = Hangman(rand_word())
    new_underlist = ''
    while game.tentativas <= 6:
    #Enquanto o jogo nao tiver terminado, print do status, solicita uma letra e faz a leitura do caractere
        game.print_game_status(game.tentativas)
        letter = input('\nInsira uma letra: ').lower()
        while game.letras_corretas.count(letter) > 0 or game.letras_incorretas.count(letter) > 0:
            print('Esta letra já foi inserida!')
            letter = input('Insira uma nova letra: ')
        new_underlist = game.guess(letter)
        timebreak = game.hangman_over()
        timebreak = game.hangman_won()
        if timebreak == 1:
            print('\nParabéns! Você venceu!')
            print('Você acertou a palavra:')
            print(game.under_list)
            break
        if  timebreak == 2:
            print('\nGame over! Você perdeu!')
            print('A palavra era ' + game.word)
            print('\nFoi bom jogar com você! Agora vá estudar!\n')
            break

#Executa o programa
if __name__ == "__main__":
    main()