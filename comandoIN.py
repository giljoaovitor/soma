def Comando_in():
    frutas = ['maçã', 'abacate', 'açaí', 'pêra']
    print('maçã' in frutas)
    print('cajá' in frutas) #mesmo que print('cajá not in frutas)
    print('cajá' not in frutas)
    fruta_teste = "laranja"
    if(fruta_teste not in frutas):
        frutas.append(fruta_teste)
        print(f"{fruta_teste} adicionado ao vetor")
    else:
            print(f"{fruta_teste} já está no vetor")
    print(frutas)
if __name__=="__main__":
    Comando_in()