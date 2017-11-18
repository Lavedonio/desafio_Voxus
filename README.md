# Desafio Voxus
Este é o repositório do projeto desafio feito pela Voxus.

Para rodar o sistema no seu computador, siga os passos abaixo:

## 1. Instalação
Para rodar o sistema no seu computador, você deverá ter os programas abaixo instalados. Siga o processo de instalação na ordem, porque cada um depende dos anteriores.

### 1.1. Python
#### Mac e Linux
O Python já vem instalado no sistema.
#### Windows
Instale o [Python 3.6](https://www.python.org/downloads/windows/). Escolha entre as versões 32-bit ou 64-bit de acordo com as configurações do seu sistema.
Na primeira janela de instalação, selecione a opção **Add Python 3.6 to PATH** e continue a instalação normalmente.

### 1.2. PIP
O pip já vem instalado para as versões do Python 2.7.9 ou superior (na série Python2) e Python 3.4 (ou superior).
Para saber se ele está instalado, abra seu terminal e digite o comando `pip`.

Caso não tiver instalado, vá para a salve [este arquivo](https://bootstrap.pypa.io/get-pip.py) como **git-pip.py** e, no terminal, digite o comando `python get-pip.py`

### 1.3. Virtualenv
No Windows, abra o **Prompt de Comando** e digite o comando `pip install virtualenv`

No Mac e Linux, abra o **Terminal** e digite o comando `sudo pip install virtualenv`

## 2. Configuração
#### Mac e Linux
Abra o **Terminal**, e digite o comando:

`virtualenv --no-site-packages --distribute -p python3 .env && source .env/bin/activate && pip install -r requirements.txt`

Teste o comando `pip freeze`. Se aparecer uma lista de itens idênticos ao do arquivo *requirements.txt*, a instalação ocorreu com sucesso.

Para desativar o ambiente virtual, digite no **Terminal** o comando `deactivate`

#### Windows
Abra o **Prompt de Comando**, e digite o comando:

`virtualenv --no-site-packages --distribute -p python3 .env && cd .env/ && .\Scripts\activate && cd ../ && pip install -r requirements.txt`

Teste o comando `pip freeze`. Se aparecer uma lista de itens idênticos ao do arquivo *requirements.txt*, a instalação ocorreu com sucesso.

Para desativar o ambiente virtual, navegue pelo **Prompt de Comando** até a pasta do ambiente virtual (partindo do último comando, você pode digitar direto `cd .env/`) e digite o comando `.\Scripts\deactivate.bat`

#### Observação: o ambiente virtual não pode ser iniciado dentro de uma pasta que contenha um espaço no seu nome, mesmo que esta não seja seu filho direto. Isto vale para qualquer sistema operacional. Para verificar, digite `pwd` no Terminal do Mac/Linux ou `chdir` no Prompt de Comando do Windows e compare com os exemplos abaixo.

**Exemplos:**

/home/daniel/pasta com espaco/desafio_Voxus *(Errado)*

/home/daniel/pasta_sem_espaco/desafio_Voxus *(Correto)*

## 3. Executar Sistema
Primeiro, ative o ambiente virtual.

No **Mac e Linux**, navegue até a pasta onde o ambiente virtual está instalado. (Normalmente na página principal do projeto. Você não o verá listado se o nome da pasta ou arquivo começar com **.** , a menos que usamos o comando `ls -a`).
Ao avistar a pasta do ambiente virtual, digite: `source .env/bin/activate`

No **Windows** navegue até a pasta onde o ambiente virtual está instalado. Entre na pasta do ambiente virtual com `cd .env/` e digite: `.\Scripts\activate`. Depois, saia da pasta com `cd ..`

Por fim, para rodar o sistema, digite os comandos na ordem:

`python manage.py migrate`

`python manage.py createsuperuser`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver`

## Contato

Em caso de dúvidas, contate-me por email: [daniel.lavedonio@gmail.com](mailto:daniel.lavedonio@gmail.com)
