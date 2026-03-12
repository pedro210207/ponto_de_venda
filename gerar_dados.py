import mysql.connector
from faker import Faker
import random

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    port=3308,
    database="ponto_de_venda"
)

cursor = conexao.cursor()

fake = Faker('pt_BR')

produtos = ["Teclado Mecânico", "Mouse Gamer", "Monitor 144hz", "Mousepad", "Headset"]

print("Gerando 50 vendas falsas...")

for _ in range(50):
    produto = random.choice(produtos)
    quantidade = random.randint(1, 3)
    valor_unitario = round(random.uniform(50.0, 1500.0), 2)

    total = valor_unitario * quantidade 
    
    data_venda = fake.date_between(start_date='-60d', end_date='today')

    sql = "INSERT INTO vendas (produto, quantidade, valor, total, data_venda) VALUES (%s, %s, %s, %s, %s)"
    
    # Passamos as 5 variáveis na mesma ordem
    valores = (produto, quantidade, valor_unitario, total, data_venda)
    
    cursor.execute(sql, valores)

conexao.commit()
print("Dados inseridos com sucesso!")

cursor.close()
conexao.close()