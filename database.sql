CREATE DATABASE IF NOT EXISTS ponto_de_venda;
USE ponto_de_venda;

CREATE TABLE IF NOT EXISTS vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    produto VARCHAR(50) NOT NULL,
    quantidade INT NOT NULL,
    valor DECIMAL(10,2) NOT NULL,
    data_venda DATE DEFAULT CURRENT_DATE,
    total DECIMAL(10,2) NOT NULL
);