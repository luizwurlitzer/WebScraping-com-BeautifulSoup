import requests
#from selenium import webdriver
from bs4 import BeautifulSoup
#import selenium
#from selenium import webdriver
#from selenium.webdriver.support.ui import WebDriverWait

#driver = webdriver.Chrome("C:/Users/luiz.wurlitzer/Desktop/chromedriver.exe")
#wait = WebDriverWait(driver, 5)

def info(texto,soup):
    arquivo = open("C:/Users/luiz.wurlitzer/Desktop/extracao.txt", 'a')
    base_p = soup.findAll('h2', text=texto)[0].parent
    k = base_p.findAll('p')
    for i in range(len(k)):
        arquivo.writelines(k[i].text)
        arquivo.writelines(";")
        arquivo.writelines("\n")
    arquivo.close()

def info2(texto, span,soup):
    arquivo = open("C:/Users/luiz.wurlitzer/Desktop/extracao.txt", 'a')
    base_p = soup.findAll('h2', text=texto)[0].parent
    x = base_p.find_next('div',{'class':span})
    k = x.findAll('p')
    for i in range(len(k)):
        arquivo.writelines(k[i].text)
        arquivo.writelines(";")
        arquivo.writelines("\n")
    arquivo.close()
def pob(soup):
    arquivo = open("C:/Users/luiz.wurlitzer/Desktop/extracao.txt", 'a')
    base_p = soup.findAll('h2', text="POB / Lesões")[0].parent
    p = base_p.find('table',{'class':'table table-bordered'})
    x = p.find_next('tbody')
    k = x.findAll('tr')
    for i in range(len(k)):
        r = k[i].findAll('td')
        for z in range(len(r)):
            arquivo.writelines(r[z].text)
            arquivo.writelines(", ")
        arquivo.writelines("\n")


    try:
        base_p = soup.findAll('h2', text="Tripulação")[0].parent
        p = base_p.find('table', {'class': 'table table-bordered'})
        x = p.find_next('tbody')
        k = x.findAll('tr')
        for i in range(len(k)):
            r = k[i].findAll('td')
            for z in range(len(r)):
                arquivo.writelines(r[z].text)

                arquivo.writelines("\n")


    except:
        arquivo.writelines("Tripulação não localizada")
        arquivo.writelines("\n\n")
    arquivo.close()

def coordenadas(soup):
    arquivo = open("C:/Users/luiz.wurlitzer/Desktop/extracao.txt", 'a')
    tst = str(soup.find('iframe'))
    localizacao = tst[155:184]
    arquivo.writelines("Coordenadas: "+localizacao)
    arquivo.writelines(";")
    arquivo.writelines("\n")
    arquivo.close()


def rodar():
    ids = [201904261718061,201312104344521,201312318599537,201312104344521]
    try:
        arquivo = open("C:/Users/luiz.wurlitzer/Desktop/extracao.txt", 'r+')
    except FileNotFoundError:
        arquivo = open("C:/Users/luiz.wurlitzer/Desktop/extracao.txt", 'w+')
        #arquivo.writelines(u'Arquivo criado pois nao existia\n')
    arquivo.close()
    for i in range(len(ids)):
        retorno = requests.get('http://www.potter.net.br/show_fnco/{!s}'.format(ids[i]), verify=False)
        soup = BeautifulSoup(retorno.text, 'html5lib')
        info("Informações Gerais",soup)
        info2("Aeronave Envolvida #1", "span8",soup)
        info2("Aeronave Envolvida #1", "span4",soup)
        try:
            info2("Aeronave Envolvida #2", "span8",soup)
            info2("Aeronave Envolvida #2", "span4",soup)
        except:
             print("\n")

        pass

        info("Informações Adicionais",soup)
        coordenadas(soup)
        pob(soup)


rodar()