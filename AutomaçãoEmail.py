# Automação de email usando a lib: smtplib

import smtplib
from email.mime.multipart import MIMEMultipart #Criar email com várias partes, texto, anexo, etc
from email.mime.text import MIMEText # Para colocar os textos dentros dos emails
import openpyxl 

def enviar_email():
    try:
        #Variáveis para armazenar o remetente, senha, destinatário, assunto, corpo
        workbook = openpyxl.load_workbook('/home/adriel/Documentos/Develop/AutomacaoEmail/testeautomacao.xlsx') #Para carregar a planilha;
        pagina_clientes = workbook['Página1'] #Página da planilha;
        for linha in pagina_clientes.iter_rows(min_row=2):#Linha minima que deve começar a ler os dados;
            remetente = "adrielmedeirosaraujo@gmail.com"
            senha = "gmwk avhw dihk ylxs"
            emails = linha[0].value # Extrai o dado da linha/indice;
            to = emails
            destinatario = to
            assunto = "Email automático"
            corpo = """
                    Olá [Nome],

                    Espero que esteja tudo bem com você!

                    Gostaria de retomar nosso último ponto de contato e verificar se houve algum avanço em relação às pendências mencionadas. Estamos nos aproximando do prazo estipulado, e seria interessante alinharmos os próximos passos para garantir que tudo siga conforme o planejado.

                    Fico à disposição para agendarmos uma breve reunião, caso considere necessário. Me avise qual seria o melhor horário para você nos próximos dias.

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

