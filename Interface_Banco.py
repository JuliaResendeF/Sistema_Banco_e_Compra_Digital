import Sistema_Banco
import PySimpleGUI as sg

#Autor: Julia Resende 
#Projeto sistema de compra e conta bancaria

sg.set_options(font=('Arial Bold', 16))
sg.theme('Dark Grey 13')

#Variaveis e outras funções que são usadas nos layouts
data = Sistema_Banco.Extrato_List
Saldo = Sistema_Banco.AchaSALDO()
Saldo = sg.Text(Saldo ,font=('Arial Bold',40), key='-saldo-')
Name = sg.Text(Sistema_Banco.Name,size=(20,3))
lista_compras = sg.Listbox(Sistema_Banco.lista_compras,size=(40,20),font=('Arial Bold',20), key="-LISTBOX-", justification="center",background_color="SlateGray",enable_events=True)
Table_Ext_Indices=['Saldo', 'Compra', 'Saldo atual','data']
Table_Ext = sg.Table(values=data, headings=Table_Ext_Indices,
   auto_size_columns=True,
   display_row_numbers=False,
   justification='center', key='-TABLE-',
   selected_row_colors='red on yellow',
   enable_events=True,
   expand_x=True,
   expand_y=True,
   enable_click_events=True)
Voltar=sg.Button('<-',key='-Back-')

#Layouts e janelas da interface
layout_Menu = [[Name, sg.Text('Meu Banco IT',size =(25,3), justification=("center"))]
           ,[sg.Text("R$", size =(2,-1), justification=("center")),Saldo]
           ,[sg.Button("Extrato",size=(17,1))]
           ,[sg.Button("Historico de compras",key='-Compras-')]
           ,[sg.Button("Adicionar Saldo",size=(17,1),key='-ADSaldo-')]]

layout_Hist = [[Voltar,sg.Text("Historico de compras   ",size=(40,1),justification=("center"))],
           [lista_compras]]
Voltar=sg.Button('<-',key='-Back-')
layout_Extrato = [[Voltar,Table_Ext]]
Voltar=sg.Button('<-',key='-Back-')
layout_ADS = [[Voltar,sg.Text('Clique no valor que deseja adicionar',size=(50,1),justification=("center"))],[sg.Text('')],
           [sg.Button('R$ 20',size=(17,1),key='20'),sg.Button('R$ 50',size=(17,1),key='50')],[sg.Text('')],
           [sg.Button('R$ 200',size=(17,1),key='200'),sg.Button('R$ 500',size=(17,1),key='500'),sg.Button('R$ 1000',size=(17,1),key='1000')]]

window = sg.Window("Banco It",layout_Menu,size=(450,500),element_justification='c')
window2 = sg.Window("Banco It", layout_Hist,size=(450,500),element_justification='c',finalize=True)
window2.hide()
window3 = sg.Window("Banco It", layout_Extrato,size=(700,500),element_justification='c',finalize=True)
window3.hide()
window4 = sg.Window("Banco It", layout_ADS,size=(700,300),element_justification='c',finalize=True)
window4.hide()

#Funcionamento dos botões, navegação entre janelas e conexão entre arquivos python
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
     break
 
    if event == "-Compras-":
        window2.un_hide()
        window.hide()
        while True:
            evento2, valores2 = window2.read()
            if evento2 == sg.WINDOW_CLOSED:
                break
            elif evento2 == '-Back-':
                window.un_hide()
                window2.hide()
                break
    if event == "Extrato":
         window3.un_hide()
         window.hide()
         while True:
            evento3, valores3 = window3.read()
            if evento3 == sg.WINDOW_CLOSED:
                break
            elif evento3 == '-Back-':
                window.un_hide()
                window3.hide()
                break     
    if event == '-ADSaldo-':
         window4.un_hide()
         window.hide()
         while True:
            evento4, valores4 = window4.read()
            if evento4 == sg.WINDOW_CLOSED:
                break
            elif evento4 == '-Back-':
                window.un_hide()
                window4.hide()
                break
            else:
             Saldof = Sistema_Banco.AchaSALDO()
             NovoSaldo=Saldof + int(evento4)
             print(NovoSaldo)
             with open(Sistema_Banco.Saldo_Data , 'w') as arquivo:
                arquivo.write(str(NovoSaldo))
             window['-saldo-'].update(Sistema_Banco.AchaSALDO())
             sg.popup('Pagamento realizado!')
             
            
                
            
                    
               
            
            
    