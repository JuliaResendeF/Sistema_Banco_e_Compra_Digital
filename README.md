# Sistema Banco e Compra Digital

> Status: Em desenvolvimento
## Resumo
Este projeto possui dois sistemas, um sistema que simula uma conta de banco com as funcionalidades de saldo, extrato, histórico de compras e adicionar saldo, e um sistema que simula uma plataforma de compras digital em que é possível visualizar e comprar produtos com o saldo do sistema de banco. Os dois sistemas compartilham dados através de documentos .txt que funcionam como um banco de dados para que dados sejam lidos e adicionados pelos sistemas. Os dados dos produtos no sistema de compras (nome, preço, quantidade no estoque, imagem e descrição) são armazenados no documento Produtos_Data.txt e acessados para construir elementos da interface do sistema, ao realizar uma compra o saldo do sistema banco é acessado no documento Saldo_SistemaBanco.txt, é feita uma verificação para saber se o saldo é suficiente para a compra, e caso seja, a compra é realizada, nessa operação o preço do produto é descontado do saldo, os dados da compra (valor do saldo antes da compra, valor do produto, valor do saldo após a compra e data da compra) são registrados no arquivo Extrato_Data.txt e o nome do produto é registrado no arquivo Historico_Compras_Data.txt. No sistema banco o saldo é acessado no documento Saldo_SistemaBanco.txt, os dados da tabela de extrato são lidos no documento Extrato_Data.txt e os dados na lista do histórico de compras são lidos no documento Historico_Compras_Data.txt.

## Requisitos:
```
Python 3.11.4
```
```
PySimpleGUI 4.60.5
```
## Arquivos que devem ser executdos para usar os sistemas(Executar com python):
```
Interface_Banco.py
```
```
Interface_Compras.py
```
