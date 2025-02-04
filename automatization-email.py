import imaplib
import email
from email.header import decode_header
import smtplib
from email.mime.text import MIMEText
import mysql.connector 

IMAP_SERVER = "imap.gmail.com"
IMAP_PORT = 993
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_USER = "testepysamuel@gmail.com"
EMAIL_PASS = "nzpzcmpmgltrfxoi"

DB_CONFIG = {
    "host": "localhost",
    "user": "root",  
    "password": "colg@t2A",
    "database": "Samuel_motopecas"
}

def conectar_banco():
    """Função para conectar ao banco de dados."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None

def buscar_produto(nome_produto):
    """Busca informações de um produto no banco de dados."""
    conn = conectar_banco()
    if not conn:
        return "Erro ao acessar o banco de dados."

    cursor = conn.cursor(dictionary=True)
    query = "SELECT produto, preco FROM produtos WHERE produto LIKE %s LIMIT 1"
    cursor.execute(query, (f"%{nome_produto}%",))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return f"O produto '{resultado['produto']}' custa R${resultado['preco']}."
    else:
        return "Desculpe, não encontramos informações sobre o produto solicitado."

def buscar_emails():
    """Busca e processa e-mails não lidos."""
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("inbox")
    status, messages = mail.search(None, "UNSEEN")
    emails = messages[0].split()
    
    for num in emails:
        _, data = mail.fetch(num, "(RFC822)")
        for response in data:
            if isinstance(response, tuple):
                msg = email.message_from_bytes(response[1])
                subject, encoding = decode_header(msg["Subject"])[0]
                if isinstance(subject, bytes):
                    subject = subject.decode(encoding if encoding else "utf-8")
                from_email = msg.get("From")
                
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode()
                else:
                    body = msg.get_payload(decode=True).decode()

                print(f"Novo e-mail de {from_email} com assunto: {subject}")
                
                resposta = encontrar_resposta_no_banco(body)
                enviar_resposta(from_email, f"Re: {subject}", resposta)
    
    mail.logout()

def enviar_resposta(destinatario, assunto, corpo):
    """Envia uma resposta automática por e-mail."""
    msg = MIMEText(corpo, "plain")
    msg["Subject"] = assunto
    msg["From"] = EMAIL_USER
    msg["To"] = destinatario

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, destinatario, msg.as_string())

    print(f"Resposta enviada para {destinatario}")

def encontrar_resposta_no_banco(mensagem):
    """Encontra a resposta baseada na mensagem do usuário e no banco de dados."""
    palavras = mensagem.split()
    for palavra in palavras:
        resposta = buscar_produto(palavra)
        if "não encontramos informações" not in resposta:
            return resposta
    return "Obrigado por entrar em contato. Responderemos em breve."

if EMAIL_USER and EMAIL_PASS:
    buscar_emails()
