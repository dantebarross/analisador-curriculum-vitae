# Estado atual do programa
Ainda estou na etapa de leitura do documento de Curriculum Vitae! O leitor OCR não foi satisfatório. Outros métodos serão buscados.

As falhas de leitura foram diversas e prejudicaram muito na hora de processar o texto e utilizar as ferramentas de RegEx e do NLTK. Possíveis resoluções: 
1. Transformar o PDF em WORD;
2. Utilizar um leitor OCR melhor, como o do Google Cloud;
3. Se não der certo, testar outras formas de trabalhar diretamento com o formato WORD ou converter para Texto.


# Analisador automático de Curriculum Vitae
<a name="intro"></a>
## Sumário
1. [Introdução](#git1)
2. [Instalação](#git2)
3. [Instalações extras para usuários Windows](#git3)
3.1 [Instalando o binário do Poppler](#git3.1)
3.2 [Instalando o binário do Tesseract + o suporte para a língua portuguesa](#git3.2)


### 1. Introdução  <a name="git1"></a> [🠡](#intro)
O curriculum vitæ ("trajetória de vida") ou CV é um documento com o tamanho de uma página A4 contendo a trajetória educacional e de carreira de alguém. O objetivo desse tipo de currículo é mostrar sucintamente como a pessoa pode se encaixar em algum projeto, vaga de emprego e outras oportunidades (educacionais e profissionais). As habilidades e competências são levadas em conta.

O presente **Analisador Automático de Curriculum Vitae** tem como objetivo ler o documento (PDF ou Word) e extrair de lá as seguintes informações:
1. Entidades (instituições educacionais, empresas);
2. Análise de sentimento (se o texto traz sentimentos positivos, negativos, neutros);
3. Nível de língua (qual a língua e qual o nível de fluência);
4. Informações pessoais do candidato.


### 2. Instalação  <a name="git2"></a> [🠡](#intro)

Faça um Virtual Environment Python 3.7 através de sua IDE ou através da Command Line:
1. Instale o virtualenv através do comando pip ``pip install virtualenv``
2. Crie o ambiente virtual através do comando abaixo, escolhendo o **path** e o **executável** do Python 3.7:

a. Windows:
```
cd my-project
virtualenv --python C:\Path\To\Python\python.exe venv
```
b. Linux: 
```
cd /path/para/seus/projetos/projeto
virtualenv .
```

O ambiente virtual será criado e executado. Agora, você pode instalar quaisquer bibliotecas que somente o ambiente virtual será afetado. Isso significa que seu python raíz não reconhecerá as bibliotecas instaladas dentro de um virtual environment.

Para instalar as dependências do projeto, abra o Virtual Environment e execute o comando ``pip install -r requirements.txt``

#### 2.1 NLTK  <a name="git2.1"></a> [🠡](#intro)
A biblioteca de Natural Language Processing (NLP) NLTK vai ser instalada no comando ``pip install requirements.txt``, porém é necessário executar, dentro de seu terminal do virtual environment, os seguintes comandos:
```
python # Para executar o python, faça isso dentro do virtual environment
import nltk
nltk.download()
```
Após executar os comandos acima, a janela NLTK Downloader abrirá. Clique duas vezes na opção all-nltk para baixar os pacotes de ferramenta. Aguarde pois o download e instalação podem demorar alguns minutos.

### 3. Instalações extras para usuários Windows  <a name="git3"></a> [🠡](#intro)
#### 3.1 Instalando o binário do Poppler  <a name="git3.1"></a> [🠡](#intro)
Caso seja um usuário do Windows, é necessário realizar uma instalação manual para que funcione a biblioteca conversora de PDF em imagem. Siga os passos abaixo:
1. Vá até essa página (https://github.com/oschwartz10612/poppler-windows/releases/) e escolha o _release_ de sua escolha (estou utilizando o _release_ **20.12.1**)
2. Extraia o arquivo zip dentro de sua pasta "Arquivos de Programas" ou "Program Files". No final o diretório será parecido com esse ("C:\Program Files\poppler-20.12.1").
3. Adicione a pasta bin de seu novo diretório no PATH de seu sistema. Para isso realize os passos abaixo:
  1. Clique no botão Iniciar do Windows ou aperte a tecla _Iniciar_. Procure por "Edit the system environment variables" ou "Editar as variáveis de ambiente do sistema";
  2. Clique em "Environment Variables" ou "Variáveis de Ambiente";
  3. Na sessão "System variables" ou "Variáveis do sistema", clique duas vezes em _PATH_, clique em "New"/"Novo";
  4. No campo de digitação aberto, cole o diretório "\bin" de seu diretório do poppler (no meu caso "C:\Program Files\poppler-20.12.1\Library\bin", sem aspas);
  5. Tecle ENTER, dê um OK e reinicie o Command Line caso esteja aberto.

#### 3.2 Instalando o binário do Tesseract + o suporte para a língua portuguesa  <a name="git3.2"></a> [🠡](#intro)
A biblioteca Tesseract (que executa a tecnologia OCR em uma imagem) também precisa do diretório "\bin" no _PATH_:
1. Faça o download do instalador (https://github.com/UB-Mannheim/tesseract/wiki) e instale-o em seu "Arquivos de Programas" (C:\Program Files\Tesseract-OCR);
2. No arquivo _"analisador-curriculum-vitae.py"_ desse repositório, modifique o path até o executável se necessário:
``pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'``

Para istalar o suporte à língua portuguesa:
1. Faça download do modelo treinado (https://github.com/tesseract-ocr/tessdata/blob/master/por.traineddata);
2. Cole o arquivo 'por.traineddata' na pasta 'tessdata', dentro do folder do Tesseract (o meu é 'C:\Program Files\Tesseract-OCR\tessdata').
