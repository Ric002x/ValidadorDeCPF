# Validador de CPF
Este repositório contém um programa que valida CPFs de acordo com as normas estabelecidas pela Receita Federal do Brasil.


## Versões
O projeto possui duas versões disponíveis para uso, ambas com a opção de rodar o software via terminal ou através de uma interface gráfica desenvolvida com CustomTkinter.

### Versão 1
Nesta versão, o usuário pode inserir um CPF manualmente para realizar a validação.

 - **Terminal**:
   - O usuário é solicitado a digitar um CPF, e o sistema verifica sua validade, retornando o resultado diretamente no terminal.

 - **Gui**:
   - A interface gráfica permite a inserção do CPF em um campo dedicado, oferecendo uma experiência mais amigável.
![imgem da interface](./imgs/gui_1.png)

### Versão 2
Nesta versão, o usuário pode fornecer uma planilha de dados no formato CSV, contendo pelo menos os campos "Nome", "Sobrenome" e "CPF". O validador analisará e informará se cada CPF é válido ou não.

 - **Terminal**:
   - A versão em terminal foi utilizada principalmente para testes. O sistema automaticamente carrega e valida os CPFs de um arquivo de teste localizado em `./cpf_.csv`.

 - **Gui**:
   - A interface gráfica permite que o usuário selecione um arquivo CSV para validação dos CPFs, proporcionando um método prático e intuitivo para processamento de múltiplos CPFs.

![imgem da interface](./imgs/gui_2.png)


## 📋 Tecnologias E Bibliotecas Utilizadas
~~Este projeto foi construído somente com **Python** na versão 3.12.3 e não requer a instalação de nenhuma dependência (biblioteca)~~

 - Este projeto foi construído em Python 3.12.3 e utiliza as seguintes bibliotecas:

    - **CustomTkinter 5.2.2**: Para a criação da interface gráfica.
    - **Pandas 2.2.2**: Para manipulação de arquivos de dados como CSV e Excel.


## 📦 Instalação

1. Clone o repositório com:
```bash
git clone git@github.com:Ric002x/ValidadorDeCPF.git
```

2. Crie e ative o ambiente virtual (opicional):
```bash
python -m venv venv
```

 - Ativando no windows:
```bash
./venv/Scripts/activate
```

- Ativando no macOS/Linux:
```bash
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```


## 🚀 Como Usar

### Versão 1

**Terminal**:

1. Para utilizar esta versão pelo terminal, utilize o comando:
```bash
python ./terminal/main.py
```

2. Insira um valor de CPF. Lembrando:
 - Um CPF sempre terá um total de 11 dígitos.
 - O código permite a entrada de modos:
  - Sem hífem e ponto: `12345678910`
  - Com hífem e ponto: `123.456.789-10`

3. Após a inserção, o programa realizará as verificações para determinar se o CPF é válido.
 > O programa funcionará em um loop contínuo, permitindo que você insira e verifique múltiplos CPFs consecutivamente. Se desejar encerrar o programa, basta digitar 'parar' ao invés de fornecer um CPF. O programa reconhecerá o comando e encerrará a execução.

**Gui**:

1. Para utilizar esta versão pela interface, utilize o comando:
```bash
python ./gui/gui_main.py
```

2. Insira o CPF que deseja verificar, e clique em "Executar Validação".

### Versão 2

**Terminal**:

1. Para utilizar esta versão pelo terminal, utilize o comando:
```bash
python ./terminal/version_2.py
```

2. O programa começará automaticamente a validar os CPFs na planilha de dados fornecida, retornando resultados como:

 - "O CPF de Ricardo é Válido"

 - "O CPF de Alice é Inválido"

**Gui**:

1. Para utilizar esta versão através da interface, execute o comando:
```bash
python ./gui/gui_version_2.py
```

2. Clique em "Selecionar Arquivo", escolha a planilha de dados CSV que deseja validar os CPFs, e clique em "Iniciar Validações".

3. Os resultados aparecerão na área inferior da interface, retornando informações coloridas, da mesma forma que no terminal.


## ⬆️ Possíveis Atualizações

 - **Implementar atualização da planilha**:
    - Criar/editar coluna de "Validação": Coluna que informa se o CPF x é válido ou inválido.