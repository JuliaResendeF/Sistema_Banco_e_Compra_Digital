import PySimpleGUI as sg
import os
import Sistema_Compras

sg.theme('Neutral Blue')  
sg.set_options(font=('Arial Bold', 16))
#Obs: Ocorrem erros na visualização das palavras com acento no PySimpleGUI
#Por isso os acentos foram retirados de todos os textos 

#Inicialização de variaveis usadas no sistema
Name=""
Valor=""
Recuperar_dados_produto = []
Voltar=sg.Button('<-',key='-Back-',size=(3,1))
Botao_Comprar=sg.Button("Comprar",size=(20,1),key='-Compra_Confirmar-')
Pagamento = sg.Checkbox('Transferência bancária', key='-TB-',font=('Arial Bold', 15))

#Layouts e janelas da interface
layout_menu = [[sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/control.png'),size = (250, 250)),
           sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/monitor.png' ),size = (250, 250)),
           sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/headset.png' ),size = (250, 250))],
          [sg.Text('Pro Control 25v',size=(20,1),justification="center"),
           sg.Text('Monitor Gamer 4K',size=(20,1),justification="center"),
           sg.Text('Headset sem fio',size=(20,1),justification="center")],
          [sg.Button('Comprar',size=(20,-10),key='1'),sg.Button('Comprar',size=(20,1),key='2'),sg.Button('Comprar',size=(20,1),key='3')],
          [sg.Text('',size=(1,2))],
          [sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/raposa.png'),size = (250, 250)),
           sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/gato.png' ),size = (250, 250)),
           sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/cozinha.png' ),size = (250, 250))],
          [sg.Text('Raposa de Pelucia',size=(20,1),justification="center"),
           sg.Text('Gato de pelucia',size=(20,1),justification="center"),
           sg.Text('Cozinha Infantil',size=(20,1),justification="center")],
          [sg.Button('Comprar',size=(20,-10),key='4'),sg.Button('Comprar',size=(20,1),key='5'),sg.Button('Comprar',size=(20,1),key='6')],
          [sg.Text('',size=(1,2))],
          [sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/air.png'),size = (250, 250)),
           sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/churrasqueira.png' ),size = (250, 250)),
           sg.Image(os.path.join(Sistema_Compras.Python_Dir,'img/grill.png' ),size = (250, 250))],
          [sg.Text('Fritadeira sem oleo Airfry',size=(20,1),justification="center"),
           sg.Text('Churrasqueira Eletrica',size=(20,1),justification="center"),
           sg.Text('Grelha Eletrica',size=(20,1),justification="center")],
          [sg.Button('Comprar',size=(20,-10),key='7'),sg.Button('Comprar',size=(20,1),key='8'),sg.Button('Comprar',size=(20,1),key='9')]
          ,[sg.Text('',size=(1,2))]]

layout_Perfil =[[Voltar,sg.Text('',size=(45,1))],[sg.Image(Sistema_Compras.Image_Data,key='-img-')]
                ,[sg.Text(Name,font=('Arial Bold',35),justification='center',size=(30,1),key='-name-')],
                [sg.Text(Valor,font=('Arial Bold',28),justification='center',size=(30,1),key='-Price-')],
                [Botao_Comprar],[sg.Text('')],[sg.Text('Desc',key='-desc-',size=(50,5),justification='center')]]

Voltar =sg.Button('<-',key='-Back-',size=(3,1))
 
layout_Compra=[[Voltar],[sg.Text('')],[sg.Text('Valor Total')],[sg.Text('',font=('Arial Bold', 38),key='-Valor-')],
               [sg.Text('',size=(-5))],[sg.Text('Método de pagamento')], 
               [Pagamento],
               [sg.Text('',size=(1))],[sg.Button('Finalizar',key='-confirmar-')]]

column_layout = [
    [sg.Column(layout_menu, scrollable=True, vertical_scroll_only=True, size=(1000, 600),justification='center')]
]

window = sg.Window('Site Compra', column_layout,size=(850,600),element_justification='center',finalize=True)
window2 = sg.Window('Site Compra', layout_Perfil,size=(600,700),element_justification='c',finalize=True)
window2.hide()
window3 = sg.Window('Site Compra', layout_Compra,size=(600,450),finalize=True)
window3.hide()


#Funcionamento dos botões, navegação entre janelas e conexão entre arquivos python
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
#Devido a algumas limitações do PySimpleGUI não é possivel existir mais de um botão com a mesma função ou key,
#Por isso foi nescesário criar uma key para cada botão de 'compra'
    if event == '1' or '2' or '3':
        window2.un_hide()
        window.hide()
        Recuperar_dados_produto  = Sistema_Compras.Retorno_Data(int(event))
        #Recuperação das informações de um produto especifico com a key escolhida (key->linha no arquivo txt)
        #[Nome,Valor,Quant,img,Desc]
        name=str(Recuperar_dados_produto[0])
        price=str(Recuperar_dados_produto[1])
        imagem=(str(Recuperar_dados_produto [3]))
        Desc=(str(Recuperar_dados_produto [4]))
        #Atualização dos elementos na interface 
        window2['-name-'].update(name)
        window2['-Price-'].update("R$"+price)
        window2['-img-'].update(os.path.join(Sistema_Compras.Python_Dir, imagem))
        window2['-desc-'].update(Desc)
        while True:
            evento2, valores2 = window2.read()
            if evento2 == sg.WINDOW_CLOSED:
              break
            elif evento2 == '-Back-':
                window.un_hide()
                window2.hide()
                break
            elif evento2 =='-Compra_Confirmar-':
                 window3.un_hide()
                 window2.hide()
                 #Atualização do valor da compra com o valor recuperado anteriormente
                 window3['-Valor-'].update("R$"+price)
                 while True:
                  evento3, valores3 = window3.read()
                  if evento3 == sg.WINDOW_CLOSED:
                      break
                  elif evento3 == '-Back-':
                     window.un_hide()
                     window3.hide()
                     break
                  elif evento3 == '-confirmar-':
                    if valores3['-TB-']:
                    #Verificação e finalização da compra com a função() do arquivo Sistema_Compras
                     Verifica=Sistema_Compras.Finalizar_Compra(int(event))
                     window3['-TB-'].update(False)
                     if Verifica == False:
                         sg.popup('Saldo insufuciente')
                     else:
                         sg.popup('Compra realizada!')
                         valores3 == ''
                         window.un_hide()
                         window3.hide()
                         break     
                    else:
                     sg.popup('Selecione o método de pagamento')
            break   
            
            


