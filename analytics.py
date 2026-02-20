import pandas as pd
from database import conectar

def carregar_dataframe():
    conexao = conectar()
    if not conexao:
        return pd.DataFrame()

    df = pd.read_sql("SELECT * FROM vendas", conexao)
    conexao.close()
    return df


def resumo_vendas():
    df = carregar_dataframe()

    if df.empty:
        print("Sem dados.")
        return

    print("\n=== RESUMO GERAL ===")
    print(f"Total vendido: R$ {df['total'].sum():.2f}")
    print(f"Ticket médio: R$ {df['total'].mean():.2f}")
    print(f"Quantidade total vendida: {df['quantidade'].sum()}")

    print("\n=== PRODUTO MAIS VENDIDO ===")
    print(df.groupby("produto")["quantidade"].sum().sort_values(ascending=False).head(1))

    print("\n=== VENDAS POR DIA ===")
    print(df.groupby("data_venda")["total"].sum())