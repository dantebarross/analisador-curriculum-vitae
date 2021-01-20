# Estado atual do programa
Ainda estou na etapa de leitura do documento de Curriculum Vitae! O leitor OCR não foi satisfatório. Outros métodos foram buscados.

Agora não é necessário nenhum leitor OCR pois consegui extrair textualmente os PDFs. Também há a possibilidade de extrair e ler imagens, porém isso não será feito por enquanto.

PDFs são propriedades da Adobe e possuem suas próprias peculiaridades. Automatizar a extração de PDFs pode ser uma tarefa árdua. Estou na etapa de **limpar o texto gerado, linhas em branco, corrigir parágrafos**.





# Analisador automático de Curriculum Vitae
<a name="intro"></a>
## Sumário
1. [Introdução](#git1)
2. [Instalação](#git2)
        1. [NLTK](#git2.1)

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
