from random import randint
import getpass

arma = True
laco = True
jogo = True
contador = 0

#quant_jogadores = 3
#v=3
#vez=3
quant_jogadores=int(input("quantos jogadores vão jogar? "))
jogadores = [None] * quant_jogadores
boleana = [True] * quant_jogadores

for i in range(quant_jogadores):
    jogadores[i] = input(f"Digite o nome do jogador {i+1}: ").lower()

vez = randint(1, quant_jogadores)
#passador de vez
while jogo:
    while laco:
        vez = (vez % quant_jogadores) + 1  
        while not boleana[vez - 1]: 
            vez = (vez % quant_jogadores) + 1
        print(f"\nVez do {jogadores[vez-1].capitalize()}")
        laco = False
        contador = 1

    laco = True

    # decidir a arma
    arma = True
    sla = getpass.getpass("A arma está carregada, deseja esvaziá-la? (s/n) ").lower()
    if sla == "s":
        arma = False

    print("A quem deseja entregar a arma?")
    for i, nome in enumerate(jogadores, start=1):
        if i != vez and boleana[i - 1]:
            print(f"{i} - {nome.capitalize()}")

    escolha = input("Digite o número ou nome do jogador: ").lower()

    # escolher por numero
    if escolha.isdigit():
        v = int(escolha)
        if v < 1 or v > quant_jogadores or v == vez or not boleana[v-1]:
            print("Jogador inválido, tente novamente")
            continue
    else:
        # ecolher alvo por nome
        if escolha in jogadores:
            v = jogadores.index(escolha) + 1
            if v == vez or not boleana[v-1]:
                print("Jogador inválido, tente novamente")
                continue
        else:
            print("Jogador inválido, tente novamente")
            continue
#limpar tela (gambiarra)
    print("\n" * 10)  

    vdd = input(
        f"{jogadores[v-1].capitalize()}, você vai atirar no {jogadores[vez-1].capitalize()}? (s/n)\n"
        "Caso não queira, você irá atirar em si mesmo: "
    ).lower()

    if vdd == "s" and arma:
        print(f"{jogadores[vez-1].capitalize()} não descarregou a arma e morreu")
        boleana[vez - 1] = False
    elif vdd == "s" and not arma:
        print(f"{jogadores[vez-1].capitalize()} descarregou a arma, então {jogadores[v-1].capitalize()} perde por não confiar")
        boleana[v - 1] = False
    elif vdd == "n" and arma:
        print(f"{jogadores[v-1].capitalize()} atirou em si mesmo acreditando que {jogadores[vez-1].capitalize()} descarregou a arma e morreu")
        boleana[v - 1] = False
    else:
        print(f"{jogadores[v-1].capitalize()} confiou que {jogadores[vez-1].capitalize()} descarregou a arma e sobreviveu")

    # ganhador
    if boleana.count(True) == 1:
        vencedor = jogadores[boleana.index(True)]
        print(f"\n O vencedor é {vencedor.capitalize()}!")
        jogo = False
