from crud import cadastrar_venda, listar_vendas, remover_venda
from analytics import resumo_vendas

def menu():
    while True:
        print("\n=== SISTEMA PONTO DE VENDA ===")
        print("1 - Cadastrar venda")
        print("2 - Listar vendas")
        print("3 - Remover venda")
        print("4 - Resumo de vendas")
        print("0 - Sair")

        op = input("Opção: ").strip()

        if op == "1":
            cadastrar_venda()
        elif op == "2":
            listar_vendas()
        elif op == "3":
            remover_venda()
        elif op == "4":
            resumo_vendas()
        elif op == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()