# 📧 Bot de Atendimento via E-mail

Este projeto é um bot de atendimento automatizado via e-mail, capaz de ler mensagens da caixa de entrada, identificar solicitações de preços de produtos e responder automaticamente utilizando informações armazenadas em um banco de dados MySQL.

## ✨ Funcionalidades
- Ler e-mails não lidos da caixa de entrada.
- Identificar pedidos de preços de produtos usando expressões regulares.
- Consultar os preços no banco de dados MySQL.
- Responder automaticamente com o preço do produto solicitado.
- Enviar respostas formatadas via SMTP.

## 🛠 Tecnologias Utilizadas
- **Python**
- **IMAP & SMTP** (para leitura e envio de e-mails)
- **MySQL** (armazenamento de produtos e preços)
- **Regex** (para identificar padrões de mensagens)

## 📌 Pré-requisitos
Antes de rodar o projeto, certifique-se de ter:
- Python 3 instalado.
- Uma conta de e-mail configurada (Gmail, Outlook, etc.).
- Um servidor MySQL rodando com a base de dados configurada.

## 🚀 Instalação e Configuração
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/bot-email.git
   cd bot-email
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as credenciais de e-mail e banco de dados no código:
   ```python
   EMAIL_USER = "seuemail@gmail.com"
   EMAIL_PASS = "suasenha"

   DB_CONFIG = {
       "host": "localhost",
       "user": "root",
       "password": "sua_senha_mysql",
       "database": "nome_do_banco"
   }
   ```

4. Execute o script:
   ```bash
   python bot_email.py
   ```

## 🗄 Estrutura do Projeto
```
📂 bot-email/
 ├── bot_email.py        # Código principal do bot
 ├── config.py           # Configurações de banco e e-mail
 ├── requirements.txt    # Dependências do projeto
 ├── README.md           # Documentação
```

## 📝 Como Funciona
1. O bot acessa a caixa de entrada e busca e-mails não lidos.
2. Ele identifica mensagens que pedem preços de produtos.
3. Consulta o banco de dados MySQL para buscar os valores.
4. Responde automaticamente com o preço do produto solicitado.



---

Desenvolvido com ❤️ por Samuel Sávio.

