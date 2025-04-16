import Funções


def menu():
    while True:
        print("\n=== Sistema de Academia ===")
        print("1. Adicionar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Plano de Treino")
        print('4. Remover Aluno')
        print('5. Salvar dados')
        print('6. Carregar dados')
        print("7. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            Funções.adicionar_aluno()
        elif opcao == "2":
            Funções.listar_alunos()
        elif opcao == "3":
            Funções.atualizar_plano()
        elif opcao == "4":
            Funções.remove_al()
        elif opcao == '5':
            Funções.salvar_dados()
        elif opcao == '6':
            Funções.carregar_dados()
        elif opcao == "7":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")



menu()
