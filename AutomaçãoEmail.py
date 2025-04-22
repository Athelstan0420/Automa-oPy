# Automação de email usando a lib: smtplib

import smtplib
from email.mime.multipart import MIMEMultipart #Criar email com várias partes, texto, anexo, etc
from email.mime.text import MIMEText # Para colocar os textos dentros dos emails
import openpyxl 

def enviar_email():
    try:
        #Variáveis para armazenar o remetente, senha, destinatário, assunto, corpo
        workbook = openpyxl.load_workbook('/.xlsv') #Para carregar a planilha;
        pagina_clientes = workbook['Página1'] #Página da planilha;
        for linha in pagina_clientes.iter_rows(min_row=2):#Linha minima que deve começar a ler os dados;
            remetente = ""
            senha = ""
            emails = linha[0].value # Extrai o dado da linha/indice;
            to = emails
            destinatario = to
            assunto = "Email automático"
            corpo = """
                    
                    Agradeço desde já pela atenção e colaboração!

                    Atenciosamente,
                    [Seu Nome]
                    [Seu Cargo]
                    [Seu Telefone]
                    [Empresa]
                    """
            # Preenchimento de campos na prática:
            mensagem = MIMEMultipart()
            mensagem["from"] = remetente 
            mensagem["to"] = destinatario
            mensagem["subject"] = assunto
            mensagem.attach(MIMEText(corpo, 'plain'))
            #Protocolo de envio:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls() #Entra no servidor;
            servidor.login(remetente, senha) #Acessa o email;
            servidor.sendmail(remetente, destinatario,mensagem.as_string())#Envia o email;
            servidor.quit() #Fecha o servidor
            print("Enviado com sucesso!")
    except:
        print("ERRO!")
enviar_email()






"""
#-------------------------------------------
#Estrutura utilizada para envio de emails:
#-------------------------------------------


#bibliotecas:

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def enviar_email():

    #Variáveis:

    remetente = 'seuemail@gmail.com'
    senha = 'suasenha'
    destinatario = 'destinatario@email.com'
    assunto = 'Bom dia!'
    corpo = 'Este é um e-mail automático enviado às 6h da manhã.'

    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto
    msg.attach(MIMEText(corpo, 'plain'))

    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remetente, senha)
        texto = msg.as_string()
        servidor.sendmail(remetente, destinatario, texto)
        servidor.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print("Erro ao enviar e-mail:", e)
enviar_email()

"""
