#coding: utf-8
import math
def Eq2grau(a,b,c):
    Delta = math.pow(b,2)-4*a*c
    if(Delta>0):
        #Há duas raízes reais distintas
        x1 = (-b-pow(Delta, 0.5))/(2*a)
        x2 = (-b+pow(Delta, 0.5))/(2*a)
        return x1,x2
    elif (Delta)



if __name__=="__main__":
    x1, x2 = Eq2grau(1,4,3)
    print(f"As raízes são {x1} e {x2}")