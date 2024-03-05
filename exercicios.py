#Exercicio IMC
# comentario imc = peso / altura^2
# para diminuir o número de casas decimais ex:  {variavel:.2f}  que significa no final ter 2 casas decimais só

peso = float(input('digite seu peso em Kg: '))
altura = float(input('digite sua altura em metros: '))

IMC = float(peso/altura**2)

print(f'o seu IMC é {IMC:.2f}')

#Exercicio Lista 5 numeros

lista_numeros = []

for i in range(5):
    numero = int(input('digite 5 numeros inteiros: '))
    lista_numeros.append(numero)

print(lista_numeros)

#Exercicio lista strings

nomes = input('digite uma lista de nomes separados por virgula: ')

#split vai dividir a entrada em uma lista de strings separadas por virgula. ','

lista_de_nomes = nomes.split(',')

lista_de_nomes = [nomes.strip() for nomes in lista_de_nomes]

print(lista_de_nomes)


#!pip install plyer - Desafio Notificação
from plyer import notification 
notification.notify(
     title='Título da notificação',
     message='Mensagem da notificação',
     app_name='Nome do aplicativo',
     timeout=10 )

from plyer import notification
from datetime import datetime

def alerta(nivel, base, etapa):
    
    # Mapear níveis para títulos
    if nivel == 1:
        titulo = "Alerta Baixo"
    elif nivel == 2:
        titulo = "Alerta Médio"
    elif nivel == 3:
        titulo = "Alerta Alto"
    else:
        print("Nivel",nivel,"não disponível!")

    # Mensagem do alerta
    mensagem = f"Falha no carregamento da base {base} na etapa {etapa}\nData: {datetime.now()}"

    # Exibir notificação
    notification.notify(
            title=titulo,
            message=mensagem,
            app_name='alerta',
            timeout=10
        )

alerta(nivel = 2,
        base = "CLIENTES", 
        etapa = "EXTRACAO")