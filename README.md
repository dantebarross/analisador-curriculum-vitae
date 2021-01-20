# Analisador automático de Curriculum Vitae com base no conteúdo textual

O curriculum vitæ ("trajetória de vida") ou CV é um documento com o tamanho de uma página A4 contendo a trajetória educacional e de carreira de alguém. O objetivo desse tipo de currículo é mostrar sucintamente como a pessoa pode se encaixar em algum projeto, vaga de emprego e outras oportunidades (educacionais e profissionais). As habilidades e competências são levadas em conta.

O presente **Analisador Automático de Curriculum Vitae** tem como objetivo ler o documento (PDF ou Word) e extrair de lá as seguintes informações:
1. Entidades (instituições educacionais, empresas);
2. Análise de sentimento (se o texto traz sentimentos positivos, negativos, neutros);
3. Nível de língua (qual a língua e qual o nível de fluência);
4. Informações pessoais do candidato.


## Instalação

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

### Windows

Caso seja um usuário do Windows, é necessário realizar uma instalação manual para que funcione a biblioteca conversora de PDF em imagem. Siga os passos abaixo:
1. Vá até essa página (https://github.com/oschwartz10612/poppler-windows/releases/) e escolha o _release_ de sua escolha (estou utilizando o _release_ **20.12.1**)
2. Extraia o arquivo zip dentro de sua pasta "Arquivos de Programas" ou "Program Files". No final o diretório será parecido com esse ("C:\Program Files\poppler-20.12.1").
3. Adicione a pasta bin de seu novo diretório no PATH de seu sistema. Para isso realize os passos abaixo:
  1. Clique no botão Iniciar do Windows ou aperte a tecla _Iniciar_. Procure por "Edit the system environment variables" ou "Editar as variáveis de ambiente do sistema";
  2. Clique em "Environment Variables" ou "Variáveis de Ambiente";
  3. Na sessão "System variables" ou "Variáveis do sistema", clique duas vezes em _PATH_, clique em "New"/"Novo";
  4. No campo de digitação aberto, cole o diretório "\bin" de seu diretório do poppler (no meu caso "C:\Program Files\poppler-20.12.1\Library\bin", sem aspas);
  5. Tecle ENTER, dê um OK e reinicie o Command Line caso esteja aberto.
