PYTHONDONTWRITEBYTECODE='python'

#x alguna razon esto no funk...
'''
import importlib
from typing import Dict

moduleName = input('Enter module name:')
importlib.import_module(moduleName)
'''
import Diccionario1
import random
'''
saludos_list = list((Diccionario1.preguntas.items())) #Convert each iterable of saludos to a list
#print(saludos_list) #cada saludo es un tupla
saludo_random = random.choice(saludos_list) #Choose a random entry from saludos_list (tuples)
#print(saludo_random)
print(saludo_random[1])
'''
'''
quejas=[]
for key, values in Diccionario1.quejas.items():
    quejas.append(values)
print(quejas)
'''
'''
a=input('ingreso')
if a in ((Diccionario1.quejas.values())):
    print('ok')
'''
'''
def send_welcome():
    saludos_list = list((Diccionario1.saludos.items())) #Convert saludos to a list of iterables (tuples)
    saludo_random = random.choice(saludos_list)[1] #Choose a random entry from saludos_list (tuple[1])
    return saludo_random
print(send_welcome())
'''
'''
def llorar2(msj):
    msj=msj.split()
    for palabra in msj:
        if palabra.lower() in Diccionario1.quejas.values(): # Esto es ineficiente
            AlguienLlora=True
    return AlguienLlora

msj=input('ingrese msj: ')
if llorar2:
    print(bool(llorar2))
    print('leyo llorar2')
'''
'''
def responde_cuando_te_llaman_bocon(message):
    msj = message.text.lower().split()
    primera_palabra = msj[0]
    if '@IgBotTest1Bot' in msj:
        return True
    if message.chat.id > 0:
        return True
    return False

msj=input('ingrese msj: ')
print(bool(responde_cuando_te_llaman_bocon))
'''