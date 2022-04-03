

#from scipy.stats import chisquare
import random;
import numpy as np;
from scipy.stats import chi2_contingency;
from scipy.stats import chi2;

def mult_constante(fl, cl, acpt):
    semilla=random.randint(2000,6000);
    const=random.randint(1000,4000);

    trans1 = str(const);
    sem = str(semilla);
    semi = int(semilla);
    const1 = int(const);
    nvAcp=int(acpt);
    fl1=int(fl);
    cl1=int(cl);
    rg = int(fl1*cl1);
    suma = 0;
    media = 0.0;
    resp = [];

    #print("semilla :"+str(semilla)+" const: "+str(const));

    if len(trans1) > 3 and len(sem) > 3:
        for i in range(rg):

            num = const1 * semi;
            snum2 = str(num);
            cant = len(snum2);
            if cant >= 9:
                n = snum2[2:8];
                n1 = int(n) / 10000;
            elif (cant == 8):
                n = snum2[2:6];
                n1 = int(n) / 10000;
            elif (cant == 6):
                n = snum2[1:5];
                n1 = int(n) / 10000;
            else:
                n = snum2[1:5];
                n1 = int(n) / 10000;

            resp.append(n1);
            suma = suma + n1;

            salida = resp;

            semi = int(n);
        #print(salida);
        chi_cuadrado(fl1, cl1, nvAcp, salida)
    else:
        print("error de semilla o constante tienen que ser mayor a 3");

def chi_cuadrado(fl1, cl1, acpt1, dat):
    my_array=np.array(dat).reshape(fl1,cl1);
    print(my_array);
    stat,p_val,dof,res= chi2_contingency(my_array)

    print('===== valor estadistico de la prueba =====');
    print('C=',stat);
    print('===== Grados de libertad =====');
    print('gl=',dof);
    print('===== Valor de Probabilidad =====');
    print('p=',p_val);
    print("===== Tabla contingencia =====")
    print(res)
    prob=1.0-(acpt1/100);
    #print(prob)
    v_critico=chi2.ppf(prob,dof);
    print("===== Valor critico =====")
    print('X2=',v_critico)
    if(abs(stat)>=v_critico):
        print('Rechaza la hipótesis nula H0');
    else:
        print('No se pudo rechazar la hipótesis nula H1');




if __name__ == '__main__':
    print('Algoritmo de Chi-cuadrado')

    fl = input("Escriba número de fila: ");
    cl = input("Escriba número de colunma: ");
    acpt = input("Escriba el alfa α: ");
    print("********************************************");
    mult_constante(fl, cl, acpt);





