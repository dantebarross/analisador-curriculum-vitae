import fitz
import nltk, re, pprint
from numpy import arange
from matplotlib import pyplot


arquivo_pdf = 'cv_files/cv_danilo.pdf'
pdf = fitz.open(arquivo_pdf)
page = pdf.loadPage(0) # vai carregar apenas primeira página ('0')
text = page.getText('text')
text_replaced = (text.replace('●', ''))
pdf.close()

blank_lines_remover = text_replaced.split("\n")
non_empty_lines = [line for line in blank_lines_remover if line.strip() != ""]
texto_cv = ""
for line in non_empty_lines:
      texto_cv += line + "\n"


curriculum = (texto_cv.replace('\u200b', ''))

# Aplicações do NLTK em cima do texto
palavras = nltk.word_tokenize(curriculum, 'portuguese') # Separar palavras
sentences = nltk.sent_tokenize(curriculum, 'portuguese') # Separar sentenças
palavras_tagueadas = nltk.pos_tag(palavras) # POS-TAG (Part-of-speech) de cada palavra/token
entidades_nomeadas = nltk.ne_chunk(palavras_tagueadas, 'portuguese') # Extrair Nomes de Entidades


# Vamos remover Stop Words
from nltk.corpus import stopwords
stop_words = set(stopwords.words('portuguese'))

filtered_sentence = [w for w in palavras if not w in stop_words]
filtered_sentence = []

for w in palavras:
    if w not in stop_words:
        filtered_sentence.append(w) # 'filtered_sentence' é a variável SEM STOP WORDS

# Vamos remover pontuações
punctuation=re.compile(r'[-.?!,–:/;()|0-9]') # Vamos definir as pontuações e números que devem ser eliminados
post_punctuation=[]
for words in filtered_sentence:
    word=punctuation.sub('', words)
    if len(word)>0:
        post_punctuation.append(word) # 'post_punctuation' é a variável sem pontuações

# Vamos encontrar e-mails
emails = re.findall(r'[\w\.-]+@[\w\.-]+', curriculum) # SUCESSO
print(emails)

# Vamos encontrar números de telefone
telefones = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', curriculum) # SUCESSO
['3334445555', '333.444.5555', '333-444-5555', '333 444 5555',
 '(333) 444 5555', '333 4445555', '(333)4445555', '333444-5555',
 '+13334445555', '+1 333 4445555']
print(telefones)

''' Criar quatro listas de palavras chave

educação e experiência profissional
Licenciatura, Licenciado, Bacharelado, Bacharel, Estágio, Estagiário, carreira

línguas
Inglês, Avançado, Espanhol, Intermediário, Básico, árabe, italiano, francês

habilidades
Linguística Computacional, Natural Language Processing, NLP, Processamento de Linguagem Natural, Git, GitHub, GitLab, Python, NLTK, Spacy, Webscraping, BeautySoup, Selenium, Regex, Pandas, Numpy, Matplotlib, Machine Learning, Data Science

escritório
Microsoft Office, Google, Slack, Trello
'''



