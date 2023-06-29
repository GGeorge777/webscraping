import csv
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Configurando o Selenium para usar o navegador Firefox
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Navegando para a página inicial do Gizmodo Brasil
navegador.get('https://gizmodo.uol.com.br/')

# Localizando os elementos das postagens
# postagens = driver.find_elements(By.XPATH, '//*[@id="main"]/div[3]/div[1]/div')
postagens = navegador.find_elements(By.CLASS_NAME, 'list-item')[:10]

# print(postagens)

# Criando um dicionário para armazenar os resultados
resultados = {}

# Iterando pelas postagens e extraindo os dados desejados
for i, postagem in enumerate(postagens):
    # Extraindo o título
    titulo_elemento = postagem.find_element(
        By.XPATH, f'//*[@id="mdContent"]/div[{i+1}]/article/header/h3/a')
    titulo = titulo_elemento.text

    # Extraindo a data
    # data_elemento = postagem.find_element(By.XPATH, '//*[@id="mdContent"]/div[1]/article/div[3]/div[1]/div/div')
    data_elemento = postagem.find_element(
        By.XPATH, f'//*[@id="mdContent"]/div[{i+1}]/article/div[3]/div[{1}]/div/div/span/abbr')
    data = data_elemento.text
    data = data.split(' @')
    data = data[0]

    # Extraindo o resumo
    resumo_elemento = postagem.find_element(
        By.XPATH, f'//*[@id="mdContent"]/div[{i+1}]/article/div[3]/div[2]')
    resumo = resumo_elemento.text

    # Adicionando os dados ao dicionário
    # resultados[titulo] = {'Data': data, 'Resumo': resumo}
    resultados[f'Post {i+1}'] = {'Titulo': titulo,
                                 'Data': data, 'Resumo': resumo}

# Imprimindo os resultados
# for elem in resultados.items():
#     print(f"Título: {elem[1]['Titulo']}")
#     print(f"Data: {elem[1]['Data']}")
#     print(f"Resumo: {elem[1]['Resumo']}")
#     print('-' * 50)


with open('dct.csv', 'w', newline='') as arquivo:
    # capturando ['Titulo', 'Data', 'Resumo'] de quauisquer um dos posts
    labels = resultados['Post 1'].keys()
    writer = csv.DictWriter(arquivo, fieldnames=labels)

    writer.writeheader()
    for post in resultados.values():
        print(post)
        writer.writerow(post)


# print(resultados)

# Fechando o navegador
navegador.quit()
