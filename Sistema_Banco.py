import ast
import os
#Autor: Julia Resende 
#Projeto sistema de compra e conta bancaria

#Inicialização de variaveis usadas no sistema
Name = "Julia Resende"
lista_compras=[]
#Localização dos arquivos txt usados na mesma pasta dos arquivos python
Python_Dir = os.path.dirname(os.path.abspath(__file__))
Extrato_Data = os.path.join(Python_Dir, 'Extrato_Data.txt')
Saldo_Data = os.path.join(Python_Dir, 'Saldo_SistemaBanco.txt')
Compras_Data = os.path.join(Python_Dir, 'Historico_Compras_Data.txt')

#leitura da lista de compras(Historico_Compras_Data.txt) usada no arquivo Interface_Banco
with open(Compras_Data, 'r') as arquivo:
         linhas = arquivo.readlines()
         for linha in linhas:
            linha = linha.strip()  
            lista_compras.append(linha.split()) 

#leitura do saldo(Saldo_SistemaBanco.txt) para uso 
with open(Saldo_Data, 'r') as arquivo:
       linhas = arquivo.read()
       string = linhas
new_string=string.replace('\n', ',')
Saldo = ast.literal_eval(new_string)

#leitura do extrato(Extrato_Data.txt) usada no arquivo Interface_Banco
with open(Extrato_Data, 'r') as arquivo:
       linhas = arquivo.read()
       string = linhas
new_string=string.replace('\n', ',')
Extrato_List = ast.literal_eval(new_string)

#Função para adicionar um valor escolhido ao saldo(Saldo_SistemaBanco.txt)
def AdicionarSaldo(evento4):
        NovoSaldo=Saldo + evento4
        with open(Saldo_Data , 'w') as arquivo:
         arquivo.write(str(NovoSaldo))  
         
#Função ler o saldo(Saldo_SistemaBanco.txt) para uso nos arquivos Interface_Banco e Sistema_Compras           
def AchaSALDO():
       with open(Saldo_Data, 'r') as arquivo:
        linhas = arquivo.read()
        string = linhas
        new_string=string.replace('\n', ',')
       Saldo = ast.literal_eval(new_string)
       Saldo = int(Saldo)
       return Saldo


