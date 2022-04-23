from random import random, randrange
from socket import *
import time

serverPort = 27000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('26.97.210.21',serverPort))
serverSocket.listen(1)

listaDeClientes = []
listaDeConexoes = []
listaDePalavras = ['vaso','pia', 'box','torneira', 'chuveiro', 'tapete', 'banheira','armário', 'espelho', 'shampoo', 
'condicionador','toalha', 'janela', 'pente',  'sabonete', 'escova','creme', 'porta','saboneteira', 'lâmpada'
]
PalavrasDaRodada = []
Esperando = int(input("quantos jogadores jogarão? "))
jogadorJogando = randrange(Esperando)
for i in range(Esperando):
  conn, client = serverSocket.accept()
  listaDeClientes.append(client)
  listaDeConexoes.append(conn)
  conn.send(('/hear Você está conectado!\n').encode())
  if i != Esperando:  conn.send('/hear Espere os outros jogadores!\n'.encode())
  print("jogador "+ client[0] + ' conectou')
print('Todos jogadores conectaram!')
for i in listaDeConexoes:
  i.send(('/hear A partida vai começar!\nJogador ' + str(jogadorJogando) + ' começa jogando!').encode())

partidaRodando = 1
while partidaRodando ==1:
  PalavrasDaRodada.append( listaDePalavras.pop(randrange(len(listaDePalavras))))
  for i in listaDeConexoes:
    i.send(('/hear No banheiro tem: ' + ' '.join(PalavrasDaRodada) + '!\n').encode())
  for idx,i in enumerate(listaDeConexoes):
    if idx != jogadorJogando-1: continue  
    i.send(('/hear Jogador ' + str(jogadorJogando) + ' está jogando').encode())

  time.sleep(2)

  listaDeConexoes[jogadorJogando-1].send(('/say/clear SUA VEZ!!\n').encode())
  sentence = listaDeConexoes[jogadorJogando-1].recv(1024)
  sentence = sentence.decode()
  palavrasEnviadas = sentence.split(' ')
  print(palavrasEnviadas)
  for idx, palavraCerta in enumerate(PalavrasDaRodada):
    if palavraCerta != palavrasEnviadas[idx]:
      for idx,i in enumerate(listaDeConexoes): i.send(('/hear Jogador ' + str(jogadorJogando) + ' perdeu').encode())
      partidaRodando = 0
      break
  if jogadorJogando == Esperando:
    jogadorJogando = 0
  else: jogadorJogando = jogadorJogando+1

partidaRodando = 0

conn.close()
print("Server closed connection to client: ", client)

