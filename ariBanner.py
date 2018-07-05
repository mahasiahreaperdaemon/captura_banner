#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import os
import sys

#alvo = "bitaraxa.com.br"
#porta = 80

print("\033[32m#=#=#=#=#=#=#=#=#=#")
print("     CAPTURA DE BANNER     ")
print("#=#=#=#=#=#=#=#=#=#")
print("Criado por: \033[35mAstaroth Ariel\033[m")
print("--------------------------\033[m")

alvo = sys.argv[1]
porta = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((alvo, porta))

payload = "GET / HTTP/1.1\r\nHOST: {}\r\nConnection: keep-alive\n\r\n".format(alvo)

s.send(payload.encode(encoding="utf-8"))

resposta = s.recv(4096)

os.system("clear")

print(resposta.decode("utf-8"))
banner = resposta.decode("utf-8")
print("========================================")

salvar = input("Deseja salvar num arquivo .txt? S/N: ")
if salvar == "S" or salvar == "s":
    nomeArq = input("Nome pro arquivo: ")
    arquivo = open("{}.txt".format(nomeArq), "w")
    arquivo.write(banner)
    arquivo.close()
    print("Arquivo salvo como \033[35m{}.txt\033[m".format(nomeArq))
elif salvar == "N" or salvar == "n":
    print("Arquivo não foi salvo")
