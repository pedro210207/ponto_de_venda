import mysql.connector

def conectar():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            port=3308,
            database="ponto_de_venda"
        )
    except mysql.connector.Error as erro:
        print("Erro ao conectar ao banco:", erro)
        return None