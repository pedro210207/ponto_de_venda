from fastapi import FastAPI
from pydantic import BaseModel
import crud

app = FastAPI()

class Venda(BaseModel):
    produto: str
    quantidade: int
    valor: float

@app.get("/")
def cumprimentar():
    return {"mensagem": "olá, essa é a minha primeira api"}

@app.get("/vendas")
def listar_todas_vendas():
    vendas = crud.obter_vendas_api()
    return {"total_vendas": len(vendas), "dados": vendas}

@app.post("/vendas")
def cadastrar_nova_venda(nova_venda: Venda):
    resultado = crud.cadastrar_venda_api(
        nova_venda.produto,
        nova_venda.quantidade,
        nova_venda.valor
    )
    return resultado

@app.delete("/vendas/{id_venda}")
def deletar_venda(id_venda: int):
    resultado = crud.remover_venda_api(id_venda)
    return resultado

@app.put("/vendas/{id_venda}")
def atualizar_venda(id_venda: int, venda_atualizada: Venda):
    resultado = crud.atualizar_venda_api(
        id_venda,
        venda_atualizada.produto,
        venda_atualizada.quantidade,
        venda_atualizada.valor
    )
    return resultado

#comando pra rodar a api: uvicorn api:app --reload