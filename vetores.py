#coding utf-8

def script0():
    vA = [] #vazio
    vB = [ None ] * 5 #vazio de tamanho 5
    vC = [1, 3.4, "A", "robin"] #tamanho 4 com tipos diff

    print(vA)
    print(vB)
    print(vC)
    print("robin aparece", vC.count("robin"), "vez")

if __name__=="__main__":
        script0()