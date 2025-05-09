import random

def jogar(tentativas):
    numeroAleatorio = random.randint(0, 100)


    while tentativas > 0:   
        A = int(input("escolha um numero aleatorio de 1 a 100"))
        
        tentativas -= 1
        if A == numeroAleatorio:
            return True
        else:
            if A > numeroAleatorio:
                print("menor")
            else:
                print("maior")
            print("tente denovo")

    return False

    
def menu(dificuldade):

    if dificuldade == "1":
        tentativas_permitidas = 10
        return jogar(tentativas_permitidas)
    elif dificuldade == "2":
        tentativas_permitidas = 5
        return jogar(tentativas_permitidas)
    elif dificuldade == "3":
        tentativas_permitidas = 3
        return jogar(tentativas_permitidas)

if __name__ == "__main__":
    flag = True
    while flag:

        print('selecione a dificuldade , 1 2 3')

        dificuldade = input()
        
        if menu(dificuldade):
            print('vitoria')
        else:
            print('derrota')
        print('obrigado por jogar')
        print('so voce gostou jogue novamente e sempre bom ver voçe jogando e tambem indique esse jogo aos seus amigos')
        novamente = input('jogar novamente sim / nao')
       
        if novamente == 'nao':
            flag = False





    



    
    
        


