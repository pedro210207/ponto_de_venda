from fastapi import FastAPI
from pydantic import BaseModel
import crud

app = FastAPI()

class Venda(BaseModel):
    produto: str
    quantidade: int
    valor: float

@app.get("/")
def home():
    return {"mensagem": "API Ponto de Venda ativa"}

@app.get("/vendas")
def listar():
    vendas = crud.obter_vendas_api()
    return {"total": len(vendas), "dados": vendas}

@app.post("/vendas")
def cadastrar(venda: Venda):
    return crud.cadastrar_venda_api(venda.produto, venda.quantidade, venda.valor)

@app.delete("/vendas/{id_venda}")
def deletar(id_venda: int):
    return crud.remover_venda_api(id_venda)

@app.put("/vendas/{id_venda}")
def atualizar(id_venda: int, venda: Venda):
    return crud.atualizar_venda_api(id_venda, venda.produto, venda.quantidade, venda.valor)

#comando pra rodar a api: uvicorn api:app --reload