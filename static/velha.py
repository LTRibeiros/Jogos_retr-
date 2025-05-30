import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        self.master.title("Jogo da Velha")
        self.jogador = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        self.botoes = [[None for _ in range(3)] for _ in range(3)]
        self.criar_interface()

    def criar_interface(self):
        for i in range(3):
            for j in range(3):
                botao = tk.Button(self.master, text="", font=('Arial', 40), width=5, height=2,
                                  command=lambda i=i, j=j: self.jogada(i, j))
                botao.grid(row=i, column=j)
                self.botoes[i][j] = botao

    def jogada(self, i, j):
        if self.tabuleiro[i][j] == "":
            self.tabuleiro[i][j] = self.jogador
            self.botoes[i][j].config(text=self.jogador)

            if self.verificar_vitoria():
                messagebox.showinfo("Fim de Jogo", f"Jogador {self.jogador} venceu!")
                self.resetar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Fim de Jogo", "Empate!")
                self.resetar_jogo()
            else:
                self.jogador = "O" if self.jogador == "X" else "X"

    def verificar_vitoria(self):
        for linha in self.tabuleiro:
            if linha[0] == linha[1] == linha[2] != "":
                return True

        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] != "":
                return True

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != "":
            return True

        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != "":
            return True

        return False

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if "" in linha:
                return False
        return True

    def resetar_jogo(self):
        self.jogador = "X"
        self.tabuleiro = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botoes[i][j].config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()
