from database import conectar
import mysql.connector

def cadastrar_venda():
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor()

    try:
        produto = input("Produto: ").strip().upper()
        quantidade = int(input("Quantidade: "))
        valor = float(input("Valor unitário: "))
        data_venda = input("Data (AAAA-MM-DD) ou ENTER para hoje: ").strip()

        total = quantidade * valor

        if data_venda == "":
            sql = """
                INSERT INTO vendas (produto, quantidade, valor, total)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql, (produto, quantidade, valor, total))
        else:
            sql = """
                INSERT INTO vendas (produto, quantidade, valor, total, data_venda)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (produto, quantidade, valor, total, data_venda))

        conexao.commit()
        print(f"Venda cadastrada! Total: R$ {total:.2f}")

    except ValueError:
        print("Quantidade e valor devem ser números.")
    except mysql.connector.Error as erro:
        print("Erro ao cadastrar:", erro)
    finally:
        cursor.close()
        conexao.close()


def listar_vendas():
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor()

    try:
        cursor.execute("SELECT * FROM vendas ORDER BY data_venda DESC")
        vendas = cursor.fetchall()

        if not vendas:
            print("Nenhuma venda encontrada.")
            return

        for venda in vendas:
            print(f"""
ID: {venda[0]}
Produto: {venda[1]}
Quantidade: {venda[2]}
Valor: R$ {venda[3]:.2f}
Data: {venda[4]}
Total: R$ {venda[5]:.2f}
-----------------------------
""")

    except mysql.connector.Error as erro:
        print("Erro ao listar:", erro)
    finally:
        cursor.close()
        conexao.close()


def remover_venda():
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor()

    try:
        id_venda = int(input("ID da venda para remover: "))
        cursor.execute("DELETE FROM vendas WHERE id=%s", (id_venda,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Venda removida.")
        else:
            print("ID não encontrado.")

    except ValueError:
        print("ID deve ser número.")
    except mysql.connector.Error as erro:
        print("Erro ao remover:", erro)
    finally:
        cursor.close()
        conexao.close()