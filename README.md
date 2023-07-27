# Sistema Banco e Compra Digital

> Status: Finalizado
## Resumo
Projeto feito em Python com o auxílio do PySimpleGUI para criação da interface e de arquivos de texto para armazenamento de dados.

Este projeto possui dois sistemas, um sistema que simula uma conta de banco com as funcionalidades de saldo, extrato, histórico de compras e adicionar saldo, e um sistema que simula uma plataforma de compras digital em que é possível visualizar e comprar produtos com o saldo do sistema de banco. Os dois sistemas compartilham dados através de documentos .txt que funcionam como um banco de dados para que dados sejam lidos e adicionados pelos sistemas. Os dados dos produtos no sistema de compras (nome, preço, quantidade no estoque, imagem e descrição) são armazenados no documento **Produtos_Data.txt** e acessados para construir elementos da interface do sistema, ao realizar uma compra o saldo do sistema banco é acessado no documento **Saldo_SistemaBanco.txt**, é feita uma verificação para saber se o saldo é suficiente para a compra, e caso seja, a compra é realizada, nessa operação o preço do produto é descontado do saldo, os dados da compra (valor do saldo antes da compra, valor do produto, valor do saldo após a compra e data da compra) são registrados no arquivo **Extrato_Data.txt** e o nome do produto é registrado no arquivo **Historico_Compras_Data.txt**. No sistema banco o saldo é acessado no documento **Saldo_SistemaBanco.txt**, os dados da tabela de extrato são lidos no documento **Extrato_Data.txt** e os dados na lista do histórico de compras são lidos no documento **Historico_Compras_Data.txt**.

## Requisitos:
```
Python 3.11.4
```
```
PySimpleGUI 4.60.5
```
## Arquivos que devem ser executdos para usar os sistemas (Executar com python):
```
Interface_Banco.py
```
```
Interface_Compras.py
```
## Manual
```
Obs: Todos os textos exibidos nas interfaces estão propositalmente sem acento, pois o PySimpleGUI não suporta exibi-los
```
### Sistema Banco
Na tela inicial são exibidos o nome do dono da conta do banco, o nome fictício do banco, o saldo atual da conta, os botões Extrato, Histórico de compras e Adicionar Saldo.
O saldo atual da conta é armazenado no arquivo **Saldo_SistemaBanco.txt**, é lido no arquivo **Sistema_Banco.py** e usado no arquivo **interface_Banco.py**, para usar o saldo em operações matemáticas é necessário ler os dados do arquivo txt (que são Strings) e converte-los em int.
<p align="center">
    <img src="https://github.com/JuliaResendeF/Sistema_Banco_e_Compra_Digital/assets/108032382/8de3f90b-38c5-4c68-91dc-6c46c6fb010e">
    
O botão de extrato exibe o layout_Extrato que possui um botão para retornar a tela inicial e uma tabela com as colunas (Saldo ,Compra ,Saldo atual e data), elas exibem respectivamente o Saldo anterior a compra, o  valor da compra, o saldo após o desconto do valor da compra e data em que a compra foi realizada. Esses dados estão armazenados no arquivo **Extrato_Data.txt**, são lidos no arquivo **Sistema_Banco.py** e são formatados em formato de tabela no arquivo **interface_Banco.py**, para isso é necessário ler os dados do arquivo txt (que são Strings) e converte-los em lista.
<p align="center">
    <img src="https://github.com/JuliaResendeF/Sistema_Banco_e_Compra_Digital/assets/108032382/76cbc818-4948-4501-b8cc-cfe93f6cec34">

 ```
Obs: Os arquivos de texto suportam apenas Strings, por isso é necessário converter os dados lidos em int ou lista para o uso.
```
### Exemplo de formatação usada no arquivo **Extrato_Data.txt** que está em String e depois é convertida em lista.
 ```
[Saldo anterior a compra, valor do produto, Saldo após a compra, data da compra]
[2575, 140, 2435, '05/07/2023']
```
O botão histórico de compras exibe o layout_Hist que possui um botão para retornar a tela inicial e uma lista com os nomes de todos as compras feitas em sequência. Esses dados estão armazenados no arquivo **Historico_Compras_Data.txt**,são lidos no **arquivo Sistema_Banco.py** e são formatados em lista no arquivo **interface_Banco.py**, para isso é necessário ler os dados do arquivo txt (que são Strings) e converte-los em lista.
<p align="center">
    <img src="https://github.com/JuliaResendeF/Sistema_Banco_e_Compra_Digital/assets/108032382/219cb7a9-60af-4170-be78-50a1542d2d95">

O botão Adicionar Saldo exibe o layout_ADS que possui um botão para retornar a tela inicial e os botões R$20, R$50, R$200, R$500 e R$1000 que adicionam estes valores no saldo atual da conta quando executados, para isso é necessário somar o saldo atual com o valor escolhido e substituir o valor do saldo (valor antes da operação de soma) por este novo valor no arquivo **Saldo_SistemaBanco.txt**, esta operação é feita no arquivo **Sistema_Banco.py**.
<p align="center">
    <img src="https://github.com/JuliaResendeF/Sistema_Banco_e_Compra_Digital/assets/108032382/94db0389-31a4-4087-9b17-c6adf40f5d0d">
    
### Sistema Compras
Na tela inicial são exibidas as informações dos produtos disponíveis para a compra (Imagem ilustrativa e nome), cada um dos produtos possui um botão “comprar” que quando executado exibe o layout_perfil. 
```
Obs: Todos as imagens ilustrativas da pasta /img/ foram feitas exclusivamente para o projeto com o auxílio do software Microsoft Paint
```
<p align="center">
    <img src="https://github.com/JuliaResendeF/Sistema_Banco_e_Compra_Digital/assets/108032382/5acd50fc-6e8e-4133-9dd4-4979cd667379">

O layout_perfil funciona como uma interface base que exibe as informações do produto escolhido (nome, imagem, valor e descrição), esses dados estão armazenadas no arquivo **Produtos_Data.txt**, eles são lidos pelo arquivo **Sistema_Compras.py** e aplicados na interface pelo arquivo **Interface_Compras,py**, para isso é necessário converter os dados de String para lista. Essa interface também contém um botão “comprar” que confirma a escolha do produto para a compra e exibe o layout_Compra.
<p align="center">
    <img src="https://github.com/JuliaResendeF/Sistema_Banco_e_Compra_Digital/assets/108032382/adca302b-7de2-438d-89dc-ab721523d530">

O layout_Compra exibe o valor do produto escolhido, que é lido no arquivo **Produtos_Data.txt** reutilizando o valor do produto usado no layout_Perfil, uma opção de método de pagamento “transferência bancaria”, um botão para retornar a tela inicial e um botão para finalizar a compra. 
<p align="center">
    <img src="https://github.com/JuliaResendeF/Sistema_Banco_e_Compra_Digital/assets/108032382/aedb70e2-947e-4844-b05d-a5b96bed6110">
    
Caso o botão de finalização seja executado e nenhuma opção de pagamento seja selecionada, será exibido um popup informando “Selecione um método de pagamento” e a compra não será finalizada, Caso o botão de finalização seja executado e a opção de pagamento “transferência bancaria ” seja selecionada a compra será finalizada, nessa operação o valor do saldo é lido no arquivo **Saldo_SistemaBanco.txt** pelo arquivo **Sistema_Banco.py** e essa informação é usada pelo arquivo **Sistema_Compras.py**, o valor do produto é descontado do valor do saldo e é feita uma verificação para saber se o saldo é suficiente para a compra (se o resultado da conta foi um número negativo ou não), caso o saldo não seja suficiente a compra não é realizada e é exibido um popup informando “Saldo insuficiente”, caso o saldo seja suficiente para a compra, o valor do saldo após a compra é convertido de int para String e substitui o antigo saldo (saldo antes da compra) no arquivo **Saldo_SistemaBanco.txt**.Os dados do saldo antes da compra, do valor do produto , do saldo após a compra e da data da compra (que é obtido através da biblioteca Datetime) são incluídos em uma lista que é convertida em String e adicionada no arquivo **Extrato_Data.txt**, essa operação também lê o nome do produto comprado no arquivo **Produtos_Data.txt** e o adiciona ao arquivo **Historico_Compras_Data.txt**.


