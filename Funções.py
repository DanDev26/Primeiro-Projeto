import json
import datetime
import random

alunos = []



def remove_al():
    print("\n=== Remover Aluno ===")
    nome = input("Digite o nome do aluno: ")

    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            print('Aluno encontrado!')
            alunos.remove(aluno)
            print(f'Aluno {nome} removido com exito!')




def atualizar_plano():
    print("\n=== Atualizar Plano de Treino ===")
    nome = input("Digite o nome do aluno: ")


    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            print(f"Aluno encontrado: {aluno['nome']}")
            novo_plano = plano()
            aluno["plano"] = novo_plano
            print(f"Plano atualizado para: {novo_plano}")
            return


    print("Aluno não encontrado.")


def plano():
    print("== Selecione o Plano Desejado ==")
    print("1. Mensal")
    print("2. Semanal")
    print("3. Dia único")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        return "Mensal"
    elif opcao == "2":
        return "Semanal"
    elif opcao == "3":
        return "Dia único"
    else:
        print("Opção inválida. Tente novamente.")
        return plano()


def adicionar_aluno():
    print("\n=== Cadastro de Aluno ===")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    dtpg = datetime.datetime.now().strftime("%d/%m/%Y")
    matricula = random.randint(1000, 9999)
    pllano = plano()

    aluno = {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "plano": pllano,
        'Data de pagamento': dtpg,
        'matricula:': matricula

    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")


def listar_alunos():
    print("\n=== Lista de Alunos ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for i, aluno in enumerate(alunos, start=1):
            print(f"{i}. Nome: {aluno['nome']},\n Idade: {aluno['idade']} anos,\n Peso: {aluno['peso']} kg,\n Altura: {aluno['altura']} m,\n Plano: {aluno['plano']},\n Data de pagamento: {aluno['Data de pagamento']},\n Matrícula: {aluno['matricula']}\n")



def salvar_dados():
    with open("alunos.txt", "w") as arquivo:
        json.dump(alunos, arquivo)
    print("Dados salvos com sucesso!")


def carregar_dados():
    try:
        with open("alunos.txt", "r") as arquivo:
            global alunos
            alunos = json.load(arquivo)
            print("Dados carregados com sucesso!")
    except FileNotFoundError:
        print("Nenhum dado encontrado. Começando com lista vazia.")