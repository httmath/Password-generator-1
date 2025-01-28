def gerar_senha(base):
    """
    Gera uma senha personalizada com base na string fornecida.
    :param base: A base da senha fornecida pelo usuário.
    :return: Uma string contendo a senha gerada.
    """
    # Mapeamento de caracteres para a geração da senha
    mapeamento = {
        "A": "Nk", "a": "qR", "B": "fx", "b": "8", "C": "8G", "c": "-",
        "D": "Wv", "d": "%", "E": "-", "e": "!3", "F": "Av", "f": "Sd",
        "G": "Wz", "g": "Eq", "H": "Bk", "h": "0c", "I": "zP", "i": "K6",
        "J": "dB", "j": "h-", "K": "Ii", "k": "5S", "L": "Lv", "l": "rz",
        "M": "U0", "m": "lk", "N": "Az", "n": "9f", "O": "rW", "o": "U8",
        "P": "lG", "p": "BK", "Q": "IR", "q": "5U", "R": "9K", "r": "@r",
        "S": "U", "s": "1l", "T": "Al", "t": "9J", "U": "rQ", "u": "Q.",
        "V": "l@", "v": "Zz", "W": "xm", "w": "9Z", "X": "qT", "x": "hT",
        "Y": "pF", "y": "Fh", "Z": "xj", "z": "Zk", "0": "-5", "1": "l9",
        "2": "kk", "3": "2T", "4": "@9", "5": "Cw", "6": "xr", "7": "vq",
        "8": "2R", "9": "0x"
    }

    # Gerar a senha com base no mapeamento
    senha = ""
    for letra in base:
        senha += mapeamento.get(letra, letra)  # Usa o caractere original se não estiver no mapeamento
    
    return senha


def main():
    print("=== Gerador de Senha Personalizada ===")
    base = input("Digite a base da sua senha: ").strip()
    
    # Verifica se a base está vazia
    if not base:
        print("Erro: A base da senha não pode estar vazia!")
        return
    
    # Gera e exibe a senha
    senha_gerada = gerar_senha(base)
    print(f"Sua senha gerada é: {senha_gerada}")


if __name__ == "__main__":
    main()
