CREATE DATABASE Samuel_motopecas;

USE Samuel_motopecas;

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    produto VARCHAR(100) NOT NULL, 
    preco DECIMAL(10,2) NOT NULL
);

INSERT INTO produtos (produto, preco) VALUES 
('Óleo para motor 10W40', 49.90),
('Pneu traseiro 150/70', 329.99),
('Capacete LS2', 599.90),
('Pastilha de freio', 89.90),
('Kit relação (corrente, coroa e pinhão)', 399.90),
('Bateria Moura 12V', 259.90),
('Farol de LED universal', 149.90),
('Velas de ignição NGK', 35.50),
('Filtro de ar esportivo', 79.90),
('Luva de proteção X11', 129.90),
('Jaqueta impermeável Texx', 499.90),
('Manopla esportiva ProTaper', 89.90),
('Cavalete central universal', 189.90),
('Baú Givi 45L', 799.90),
('Alarme antifurto Positron', 219.90),
('Protetor de motor (Crash Bar)', 349.90),
('Fluido de freio DOT 4', 29.90),
('Retrovisor esportivo', 69.90),
('Lanterna traseira LED', 99.90),
('Chave de roda articulada', 59.90);






