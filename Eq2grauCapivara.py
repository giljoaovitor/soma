#coding: utf-8
import math

def Eq2grauCapivara(a,b,c): #Como não fazer
    Delta = math.pow(b,2)-4*a*c
    x1 = None
    x2 = None
    if(Delta>0):
        #Há duas raízes reais distintas
        x1 = (-b-pow(Delta, 0.5))/(2*a)
        x2 = (-b+pow(Delta, 0.5))/(2*a)
        
    elif (Delta ==0):
        print ("Na raíz única, Delta = ", Delta)
        
    else:
        print("Raízes complexas, Delta = ", Delta)
        
    return x1, x2, Delta


if __name__=="__main__":
    saída = Eq2grauCapivara(1,4,4)
    print(saída)
    print("Quantidade de termos: ", len(saída))
    print("Primeiro termo", saída[0])
    print("Segundo termo", saída [1])
    print("Terceiro termo", saída[2])
    #print(f"As raízes são {x1} e {x2}")