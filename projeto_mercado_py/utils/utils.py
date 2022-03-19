import sys, time

def deleta_ultimas_linhas(qtde_linhas, espera: int):
    sobe_cursor = '\x1b[1A'
    apaga_linha = '\x1b[2K'

    time.sleep(espera)

    for _ in range(qtde_linhas):
        sys.stdout.write(sobe_cursor)
        sys.stdout.write(apaga_linha)
