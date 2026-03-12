from database import conectar
import random
from datetime import datetime, timedelta
import mysql.connector

def gerar_dados_realistas(quantidade_vendas=50):
    conexao = conectar()
    if not conexao:
        return

    cursor = conexao.cursor()

    produtos_info = {
        "Mouse Gamer": (120.0, 350.0),
        "Teclado Mecânico": (250.0, 600.0),
        "Teclado Magnético": (300.0, 1000.0),
        "Monitor 144hz": (900.0, 1800.0),
        "Headset com Microfone": (180.0, 450.0),
        "Mousepad Grande": (40.0, 120.0),
        "Cadeira Gamer": (800.0, 2000.0),
        "SSD 1TB": (350.0, 600.0),
        "Placa de Vídeo": (1000.0, 6000.0),
        "Processador": (300.0, 2000.0),
        "Gabinete": (150.0, 500.0)
    }

    nomes_produtos = list(produtos_info.keys())
    data_hoje = datetime.now()

    try:
        for _ in range(quantidade_vendas):
            produto = random.choice(nomes_produtos)
            preco_min, preco_max = produtos_info[produto]
            valor_unitario = round(random.uniform(preco_min, preco_max), 2)
            qtd = random.choices([1, 2, 3], weights=[80, 15, 5])[0]
            total = round(qtd * valor_unitario, 2)
            dias_atras = random.randint(0, 1000)
            data_venda = (data_hoje - timedelta(days=dias_atras)).strftime("%Y-%m-%d")
            sql = "INSERT INTO vendas (produto, quantidade, valor, total, data_venda) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (produto, qtd, valor_unitario, total, data_venda))

        conexao.commit()
        print(f"{quantidade_vendas} vendas geradas com sucesso!")

    except mysql.connector.Error as erro:
        print("Erro ao gerar dados:", erro)
    finally:
        cursor.close()
        conexao.close()

if __name__ == "__main__":
    print("Gerando dados...")
    gerar_dados_realistas(500)