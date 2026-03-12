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
            sql = "INSERT INTO vendas (produto, quantidade, valor, total) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (produto, quantidade, valor, total))
        else:
            sql = "INSERT INTO vendas (produto, quantidade, valor, total, data_venda) VALUES (%s, %s, %s, %s, %s)"
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
            print(f"ID: {venda[0]} | Produto: {venda[1]} | Qtd: {venda[2]} | Total: R$ {venda[5]:.2f} | Data: {venda[4]}")
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
        print("Venda removida." if cursor.rowcount > 0 else "ID não encontrado.")
    except ValueError:
        print("ID deve ser número.")
    finally:
        cursor.close()
        conexao.close()

def obter_vendas_api():
    conexao = conectar()
    if not conexao: return []
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM vendas ORDER BY data_venda DESC")
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()

def cadastrar_venda_api(produto, quantidade, valor):
    conexao = conectar()
    if not conexao: return {"erro": "Sem conexão"}
    cursor = conexao.cursor()
    try:
        total = quantidade * valor
        cursor.execute("INSERT INTO vendas (produto, quantidade, valor, total) VALUES (%s, %s, %s, %s)", (produto, quantidade, valor, total))
        conexao.commit()
        return {"mensagem": "Venda cadastrada!", "total": total}
    finally:
        cursor.close()
        conexao.close()

def remover_venda_api(id_venda):
    conexao = conectar()
    if not conexao: return {"erro": "Sem conexão"}
    cursor = conexao.cursor()
    try:
        cursor.execute("DELETE FROM vendas WHERE id=%s", (id_venda,))
        conexao.commit()
        return {"mensagem": "Removido"} if cursor.rowcount > 0 else {"erro": "Não encontrado"}
    finally:
        cursor.close()
        conexao.close()

def atualizar_venda_api(id_venda, produto, quantidade, valor):
    conexao = conectar()
    if not conexao: return {"erro": "Sem conexão"}
    cursor = conexao.cursor()
    try:
        total = quantidade * valor
        sql = "UPDATE vendas SET produto=%s, quantidade=%s, valor=%s, total=%s WHERE id=%s"
        cursor.execute(sql, (produto, quantidade, valor, total, id_venda))
        conexao.commit()
        return {"mensagem": "Atualizado"} if cursor.rowcount > 0 else {"erro": "Não encontrado"}
    finally:
        cursor.close()
        conexao.close()
