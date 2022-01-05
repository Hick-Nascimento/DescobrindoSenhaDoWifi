#netsh wlan show profiles
#netsh wlan show profile gruwlan key = clear

import subprocess

informacoes = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding='cp860')
print(informacoes)


nome_wifi = "gruwlan"
informacoes = subprocess.check_output(["netsh", "wlan", "show", "profile", nome_wifi, "key" "=" "clear"], encoding='cp860')
print(informacoes)

for linha in informacoes.split('\n'):
    if "Conteúdo da Chave" in linha:
        pos = linha.find(":")
        senha = linha[pos+2:]
        print(senha)