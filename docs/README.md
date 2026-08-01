# gitplay
Repositório de estudos sobre Git e GitHub.

*** EXECUTANDO ESTE PROJETO ***

OBS: Para evitar conflitos entre dependências, é uma boa prática criar um ambiente virtual/isolado para cada projeto.

- No diretório do projeto, pelo terminal ative crie e ative o ambiente virtual: 
criando: python -m venv .venv 
ativando: .venv\Scripts\Activate.ps1

- Se der certo, o prompt ficará assim:
(.venv) PS C:\Users\user\gitplay>

Depois instale as dependências/bibliotecas a seguir:

1 - Este Projeto utiliza a biblioteca (pandas), instale:
pip install pandas 

2 - O (pandas), utiliza o (openpyx1) para ler arquivos .xlsx, instale:
pip install openpyxl

SE QUISER, PODE INSTALAR OS DOIS DE UMA VEZ:
pip install pandas openpyxl

3 - Confira se instalou tudo corretamente:
pip show pandas 
pip show openpyxl 

4 - No terminal, ative o ambiente .venv
.\.venv\Scripts\Activate.ps1

Tudo será executado usando o Python e as bibliotecas da .venv.
