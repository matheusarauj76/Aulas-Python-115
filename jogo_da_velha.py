def imprimir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

def verificar_vencedor(tabuleiro):
    # Verificar linhas, colunas e diagonais
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != ' ':
            return tabuleiro[i][0]
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != ' ':
            return tabuleiro[0][i]
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != ' ':
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != ' ':
        return tabuleiro[0][2]
    return None

def jogo_da_velha():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    jogador_atual = 'X'
    
    for _ in range(9):
        imprimir_tabuleiro(tabuleiro)
        print(f"Jogador {jogador_atual}, é a sua vez!")
        
        while True:
            try:
                linha = int(input("Escolha a linha (0, 1, 2): "))
                coluna = int(input("Escolha a coluna (0, 1, 2): "))
                if tabuleiro[linha][coluna] == ' ':
                    tabuleiro[linha][coluna] = jogador_atual
                    break
                else:
                    print("Esse espaço já está ocupado! Tente novamente.")
            except (IndexError, ValueError):
                print("Entrada inválida! Por favor, escolha números entre 0 e 2.")
        
        vencedor = verificar_vencedor(tabuleiro)
        if vencedor:
            imprimir_tabuleiro(tabuleiro)
            print(f"Parabéns! O jogador {vencedor} ganhou!")
            return
        
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'
    
    imprimir_tabuleiro(tabuleiro)
    print("Empate! Ninguém ganhou.")

if __name__ == "__main__":
    jogo_da_velha()
