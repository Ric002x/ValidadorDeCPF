# Validador de CPF
Neste repositório encontra-se um programa que executa a validação de CPFs. As normas de validação de CPF são normalizadas pela Receita Federal do Brasil, e o programa é baseado nessas normas.


## 📋 Tecnologias E Bibliotecas Utilizadas
Este projeto foi construído somente com **Python** na versão 3.12.3 e não requer a instalação de nenhuma dependência (biblioteca).


## 📦 Instalação
Para poder utilizar o programa, basta clonar o respositório utlizando:
```bash
git clone git@github.com:Ric002x/PortifolioPython.git
```


## 🚀 Como Usar
1. Para executar o programa, utilize o comando:
```bash
python main.py
```
2. Insira um valor de CPF. Lembrando:
 - Um CPF sempre terá um total de 11 dígitos.
 - O código permite a entrada de modos:
  - Sem hífem e ponto: `12345678910`
  - Com hífem e ponto: `123.456.789-10`

3. Após a inserção, o programa realizará as verificações para determinar se o CPF é válido.
 > O programa funcionará em um loop contínuo, permitindo que você insira e verifique múltiplos CPFs consecutivamente. Se desejar encerrar o programa, basta digitar 'parar' ao invés de fornecer um CPF. O programa reconhecerá o comando e encerrará a execução.
