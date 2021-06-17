import requests
from bs4 import BeautifulSoup
import os

header = {
	'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.75"
}

codigo = input("código do hentai: ")

URL = f"https://nhentai.net/g/{codigo}"


response = requests.get(URL, headers=header)

if response.status_code == 200:
    content = response.content
    site = BeautifulSoup(content, 'html.parser')


    lista = []

    titulo = site.find('span', attrs={'class': "pretty"})
    titulo2 = site.find('span', attrs={'class': "after"})
    for t in titulo:
        titulo = t
        break
    for t in titulo2:
        titulo2 = t
        break

    imagens = site.find_all('a', attrs={'class': "gallerythumb"})

    for imagem in imagens:
        lista.append("https://nhentai.net"+imagem.get('href'))
    os.system("cls")
    print(f"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\nTítulo: {titulo}{titulo2}\n\nquantidade de capítulos: {len(lista)}\n\n[1] - baixar hentai\n[2] - sair\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\n")
    escolha = input("escolha: ")
    print("\n\n")
    if escolha == "1" or escolha == 1:
        num = 1
        for item in lista:
            response = requests.get(item, headers=header)

            content = response.content
            site = BeautifulSoup(content, 'html.parser')

            imagem = site.find('section', attrs={'id': "image-container"})
            for img in imagem:
                for i in img:
                    photo = (i.get("src"))
                    break

            response = requests.get(photo, headers=header)


            with open(f"capítulo {num}.png", 'wb') as f:
                f.write(response.content)
            print(f"página número {num} baixado!")
            num = num + 1
        os.system("cls")
        input("todas as páginas do hentai foram baixadas!\npressione enter para fechar")

    if escolha == "2" or escolha == 2:
        exit

if response.status_code >= 400:
    print("código de hentai incorreto!")
    input("pressione enter para fechar...")
    exit
