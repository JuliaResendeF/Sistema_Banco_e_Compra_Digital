import os
import Sistema_Banco
from datetime import date
#Autor: Julia Resende 
#Projeto sistema de compra e conta bancaria

#Localização dos arquivos txt usados na mesma pasta dos arquivos python
Python_Dir = os.path.dirname(os.path.abspath(__file__))
Produto_Data_Dir = os.path.join(Python_Dir, 'Produtos_Data.txt')
Extrato_Data= os.path.join(Python_Dir, 'Extrato_Data.txt')
Image_Data = os.path.join(Python_Dir,'control_P.png' )
Hist_Compras_Data = os.path.join(Python_Dir, 'Historico_Compras_Data.txt')
Saldo_Data = os.path.join(Python_Dir, 'Saldo_SistemaBanco.txt')
#Inicialização de variaveis usadas no sistema
Produto=[]
Extrato=[]

#Função para ler as informações do produto(Produtos_Data.txt) e converter de string para matriz
#[Nome,Valor,Quant,img,Desc]
def Retorno_Data(event):
    with open(Produto_Data_Dir, 'r') as arquivo:
        linhas = arquivo.readlines()
        linha_desejada = event
        conteudo_linha = linhas[linha_desejada-1].strip()
    Produto = eval(conteudo_linha)
    return Produto

#Função para confirmar se o saldo é suficiente para a compra 
# e caso seja prosseguir com a compra(adicionar nome no hitorico de compras, Adicionar informações da compra no extrato, Atualizar saldo)
def Finalizar_Compra(event):
    #[Nome,Valor,Quant,img,Desc]
    Produto = Retorno_Data(event)
    #Verificação de saldo disponivel para compra
    price=int(Produto[1])
    Saldo_Atual=Sistema_Banco.AchaSALDO()
    Saldo_Pos_Compra = Saldo_Atual - price
    if Saldo_Pos_Compra < 0:
        return False
    else:
     Extrato =[]
     #Finalização da compra
     #Histórico de compra ->[nome]
     name=str(Produto[0])
     with open(Hist_Compras_Data , 'a') as arquivo:
        arquivo.write("\n"+name)
     #Extrato Banco ->[Saldo antes da compra, Valor da compra, Saldo depois da compra, Data da compra]
     data_atual = date.today()
     data_formatada = data_atual.strftime("%d/%m/%Y")
     Saldo_Atual=Sistema_Banco.AchaSALDO()
     Extrato.append(Saldo_Atual)
     Extrato.append(price)
     Extrato.append(Saldo_Pos_Compra)
     Extrato.append(data_formatada)
     with open(Extrato_Data , 'a') as arquivo:
       arquivo.write("\n"+str(Extrato))
     #Atualização do saldo no Banco
     with open(Saldo_Data , 'w') as arquivo:
      arquivo.write(str(Saldo_Pos_Compra))
     return True

    
    