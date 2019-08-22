
# coding: utf-8

# In[ ]:


def InteresSimple(C,i,t):
    return C+(C*(i/100)*t)

edad = int(input("Introduce tu edad: "))
#print("Tu edad es: ", edad)

edadmin = 18
edadmax = 60
depositomin = 100

if edad > edadmin and edad < edadmax:
    deposito = int(input("Adulto permitido, Introduce la cantidad a depositar: "))
    if deposito < depositomin:
        print('Deposito Minimo No permitido')
    elif deposito >= depositomin and deposito <= 999:
        print("Su deposito fue", deposito,"Aplica 1.0% interes")
        print("Recibirás por el interes en 1 año:",InteresSimple(deposito, 1,1))
    elif deposito >= 1000 and deposito <= 4999:
        print("Su deposito fue", deposito,"Aplica 1.3% interes")
        print("Recibirás por el interes en 1 año:",InteresSimple(deposito, 1.3,1))
    elif deposito >= 5000:
        print("Su deposito fue", deposito,"Aplica 1.5% interes")
        print("Recibirás por el interes en 1 año:",InteresSimple(deposito, 1.5,1))
elif edad >= edadmax:
    deposito = int(input("Adulto permitido, Introduce la cantidad a depositar: "))
    if deposito < depositomin:
        print('Deposito Minimo No permitido')
    elif deposito >= depositomin:
        print("Su deposito fue", deposito,"Aplica 2.0% interes")
        print("Recibirás por el interes en 1 año:",InteresSimple(deposito, 2.0,1))
else:
    print("Menor de edad")

