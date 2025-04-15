import openpyxl 

def acessarplanilha():
    workbook = openpyxl.load_workbook('/home/adriel/Documentos/Develop/AutomacaoEmail/testeautomacao.xlsx') #Para carregar a planilha;
    pagina_clientes = workbook['Página1'] #Página da planilha;
    for linha in pagina_clientes.iter_rows(min_row=2):#Linha minima que deve começar a ler os dados;
        emails = linha[0].value # Extrai o dado da linha/indice;
        to = emails
        print(to)
acessarplanilha()