# Sistema de Automação de E-mails e Gestão de Produtos - Samuel Motopeças

Este projeto consiste em um sistema automatizado que gerencia e-mails e realiza consultas a um banco de dados de produtos para oferecer respostas automáticas e precisas a clientes. O sistema combina funcionalidades de processamento de e-mails com integração a um banco de dados MySQL.

---

## 🚀 Funcionalidades

- **Recepção e análise de e-mails não lidos:** 
  - Conexão com uma conta do Gmail via IMAP para buscar mensagens.
- **Respostas automáticas personalizadas:**
  - Integração com um banco de dados para buscar informações sobre produtos.
- **Envio de respostas por e-mail:**
  - Responde automaticamente os clientes via SMTP.
- **Gestão de produtos no banco de dados:**
  - Produtos armazenados com preços e descrições.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:**
  - `imaplib` e `email`: Para gerenciamento de e-mails.
  - `smtplib`: Para envio de respostas automáticas.
  - `mysql.connector`: Para conexão e consulta ao banco de dados.
- **Banco de Dados:**
  - MySQL
- **Servidor de e-mail:**
  - Gmail (IMAP e SMTP)

---

## 📋 Pré-requisitos

1. **Conta Gmail:** 
   - Ative o acesso para aplicativos menos seguros ou gere uma senha de aplicativo (recomendado).
2. **MySQL:** 
   - Banco de dados rodando localmente.
3. **Bibliotecas Python:** 
   - Instale as dependências executando:
     ```bash
     pip install mysql-connector-python
     ```

---

## ⚙️ Configuração

### Banco de Dados MySQL

1. **Criação do banco de dados:**
   Execute os seguintes comandos SQL para configurar o banco de dados:

   ```sql
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
Atualize as configurações no arquivo Python: Substitua as informações em DB_CONFIG pelas credenciais do seu banco de dados MySQL.
Conta de E-mail
Atualize as variáveis EMAIL_USER e EMAIL_PASS com suas credenciais de e-mail.
Use uma senha de aplicativo para maior segurança.

🚀 Como Executar
Certifique-se de que o banco de dados MySQL está rodando.
Execute o script Python:
bash
Copiar
Editar
python automatization-email.py
O sistema irá buscar e-mails não lidos, processar o conteúdo e enviar respostas automáticas.

🧪 Testes
E-mails de teste: Envie e-mails para a conta configurada no script e verifique se as respostas automáticas estão corretas.
Banco de dados: Faça consultas manuais para garantir que os dados estão sendo recuperados corretamente.
📦 Estrutura do Projeto
📂 Projeto
├── automatization-email.py   # Script principal
├── README.md                 # Documentação do projeto
📚 Referências
Documentação do IMAP
Documentação do MySQL Connector
📝 Licença
Este projeto está licenciado sob a licença MIT.

📞 Contato
Samuel - samueelsavio@gmail.com

Se precisar de ajuda para ajustar o conteúdo ou adicionar mais detalhes, é só avisar! 🚀
