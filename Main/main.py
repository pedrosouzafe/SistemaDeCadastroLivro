import calendar
import json
import datetime
import os

def limpar_tela():
    sistema = os.name
    if sistema == "nt":  # Windows
        os.system('cls')
    else:  # Linux/MacOS/Unix
        os.system('clear')

# Traduz o nome do mês
def traduzirMes(mes):
    meses = {
        "January": "Janeiro",
        "February": "Fevereiro",
        "March": "Março",
        "April": "Abril",
        "May": "Maio",
        "June": "Junho",
        "July": "Julho",
        "August": "Agosto",
        "September": "Setembro",
        "October": "Outubro",
        "November": "Novembro",
        "December": "Dezembro"
    }

    return meses.get(mes, None)

def cadastrarLivros():
    limpar_tela()
    print("\n --- Cadastro de Livro --- ")

    titulo = input("Digite o título do livro: ")
    limpar_tela()

    print("\n --- Cadastro de Livro --- ")
    autor = input("Digite o autor do livro: ")
    limpar_tela()

    # É pra caso o usuário digite o ano com os caracteres menor que 4
    while True: 
        try:

            print("\n --- Cadastro de Livro --- ")
            anoPublic = int(input("Digite o ano de publicação do livro (yyyy): ")) 
            anoAtual = datetime.date.today().year

            if 1000 <= anoPublic <= anoAtual:
                break
            else:
                limpar_tela()
                print(f"Digite um valor entre 1000 e {anoAtual}: ")
        except:
            limpar_tela()
            print("Digite um valor correto")

    limpar_tela()

    # Caso o número de páginas seja menor que zero
    while True:
        try:
            
            print("\n --- Cadastro de Livro --- ")
            numPag = int(input("Digite o número de páginas do livro: "))

            if(numPag <= 0):
                limpar_tela()
                print("Erro no cadastro! Digite um valor maior que zero. ")
            else:
                break
        except ValueError:
            limpar_tela()
            print("Digite um valor válido")

    limpar_tela()

    print("\n --- Cadastro de Livro --- ")
    categoria = input("Digite a categoria do livro (Ex: Ficção, Romance, etc.): ")
    limpar_tela()

    # Para aparecer a data de forma organizada
    dataAtual = datetime.date.today()
    dia = dataAtual.day
    mes = dataAtual.month
    ano = dataAtual.year
    noMes = calendar.month_name[mes]
    # ---------------------------------------

    cadastro = {
        "titulo": titulo,
        "autor": autor,
        "ano_publicacao": anoPublic,
        "numero_de_paginas": numPag,
        "categoria": categoria,
        "data_de_cadastro": f"{dia} de {traduzirMes(noMes)} de {ano}"
    }

    return cadastro

def salvarDados(arquivo, dados):
    try:
        with open(arquivo, "r", encoding='utf-8') as file:
            cadastro = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        cadastro = []

    cadastro.append(dados)
    
    with open(arquivo, "w", encoding='utf-8') as file:
        json.dump(cadastro, file, indent=4, ensure_ascii=False)
    print("Dados do livro salvos com sucesso! ")

# Função principal
def main():
    arquivo = "livros.json"

    while True:
        print("\n1. Cadastrar novo livro ")
        print("2. Ver livros cadastrados ")
        print("3. Sair ")
        opc = input("Escolha uma opção: ")

        if(opc == "1"):
            dados = cadastrarLivros()

            if dados:
                salvarDados(arquivo, dados)
        elif(opc == "2"):
            

            try:
                limpar_tela()

                with open(arquivo, "r") as file:
                    registros = json.load(file)
                if(registros):

                    print("\n--- Livros Cadastrados ---\n")

                    for reg in registros:
                        print(f"Titulo: {reg['titulo']}\nAutor: {reg['autor']}\nAno de publicação: {reg['ano_publicacao']}\nNúmero de Páginas: {reg['numero_de_paginas']}\nCategoria do Livro: {reg['categoria']}\nData do cadastro: {reg['data_de_cadastro']}")
                        print('-' * 30)
                    
                else:
                    print("Nenhum registro encontrado.")
            except FileNotFoundError:
                print("Nenhum registro encontrado. ")
        
        elif(opc == "3"):
            limpar_tela()

            print("Saindo...")
            break
        else:
            limpar_tela()
            print("Digite uma opção válida. ")

if __name__ == "__main__":
    main()
                
        