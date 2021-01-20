import fitz, nltk, re
import matplotlib.pyplot as plt

# Altere o nome 'cv_danilo' para o nome do currículo a ser analisado
nome_pdf = 'cv_danilo'

arquivo_pdf = 'cv_files/'+nome_pdf+'.pdf'
pdf = fitz.open(arquivo_pdf)
page = pdf.loadPage(0) # vai carregar apenas primeira página ('0')
text = page.getText('text')
text_replaced = (text.replace('●', ''))
#pdf.close()

blank_lines_remover = text_replaced.split("\n")
non_empty_lines = [line for line in blank_lines_remover if line.strip() != ""]
texto_cv = ""
for line in non_empty_lines:
      texto_cv += line + "\n"

curriculum = (texto_cv.replace('\u200b', ''))


# Defina as palavras chave a serem procuradas de acordo com suas preferências. Cada lista é uma categoria.
palavras_chave1 = ['microsoft office', 'google', 'slack', 'trello']
palavras_chave2 = ['inglês', 'espanhol', 'árabe', 'francês', 'italiano', 'avançado', 'fluente', 'intermediário', 'básico']
palavras_chave3 = ['linguística computacional', 'lc', 'natural language processing', 'nlp',
                   'processamento de linguagem natural', 'git', 'github', 'gitlab', 'python', 'nltk', 'spacy', 'webscraping',
                  'beautysoup', 'selenium', 'regex', 'pandas', 'numpy', 'matplotlib', 'machine learning', 'data science', 'ml',
                   'ds', 'deeplearning', 'deep learning', 'dl', 'inteligência artificial', 'artificial intelligence', 'ai', 'ia']
palavras_chave4 = ['licenciatura', 'licenciado', 'licenciada', 'bacharelado', 'bacharel', 'estágio', 'estagiário', 'estagiária', 'cto', 'fundador']


# Vamos encontrar e-mails
emails = re.findall(r'[\w\.-]+@[\w\.-]+', curriculum)
print('Lista de e-mails:', emails)


# Vamos encontrar números de telefone
telefones = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', curriculum)
['3334445555', '333.444.5555', '333-444-5555', '333 444 5555',
 '(333) 444 5555', '333 4445555', '(333)4445555', '333444-5555',
 '+13334445555', '+1 333 4445555']
print('Lista de telefones:', telefones)


# Arrays 'x' e 'y' de cada categoria listada
pc_1_x = []
pc_1_y = []
pc_2_x = []
pc_2_y = []
pc_3_x = []
pc_3_y = []
pc_4_x = []
pc_4_y = []

# Vamos procurar as palavras chave e retornar a quantidade
for i in palavras_chave1: #PALAVRAS_CHAVE1
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(i), curriculum.lower()))
    if count > 0:
        pc_1_x.append(i)
        pc_1_y.append(count)
        #print(i, 'count:', count)

for i in palavras_chave2: #PALAVRAS_CHAVE2
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(i), curriculum.lower()))
    if count > 0:
        pc_2_x.append(i)
        pc_2_y.append(count)
        #print(i, 'count:', count)

for i in palavras_chave3: # PALAVRAS_CHAVE3
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(i), curriculum.lower()))
    if count > 0:
        pc_3_x.append(i)
        pc_3_y.append(count)
        #print(i, 'count:', count)

for i in palavras_chave4: # PALAVRAS_CHAVE4
    count = sum(1 for _ in re.finditer(r'\b%s\b' % re.escape(i), curriculum.lower()))
    if count > 0:
        pc_4_x.append(i)
        pc_4_y.append(count)
        #print(i, 'count:', count)

#print(plt.style.available) # printar estilos disponíveis
#plt.style.use('ggplot') # mudar estilo do gráfico
#plt.xkcd() # exibir em visual cartoon
#plt.figure(figsize=(15,10)) # ajustar tamanho x, y
plt.barh(pc_1_x, pc_1_y, label='Software de Escritório')
plt.barh(pc_2_x, pc_2_y, label='Línguas')
plt.barh(pc_3_x, pc_3_y, label='Habilidades Computacionais')
plt.barh(pc_4_x, pc_4_y, label='Educação e Carreira')
plt.legend(['Software de Escritório', 'Línguas', 'Habilidades Computacionais', 'Educação e Carreira'])
#plt.xticks(rotation=90) #horizontalizar o eixo X
#plt.xlabel('Atributos') # título de X
#plt.ylabel('Quantidade') título de Y
plt.title('Resumo do Curriculum Vitae ' + nome_pdf)
plt.tight_layout()
plt.savefig('cv_files/' + nome_pdf)
plt.show()

#Códigos não utilizados

# Aplicações do NLTK em cima do texto
# palavras = nltk.word_tokenize(curriculum, 'portuguese') # Separar palavras
# sentences = nltk.sent_tokenize(curriculum, 'portuguese') # Separar sentenças
# palavras_tagueadas = nltk.pos_tag(palavras) # POS-TAG (Part-of-speech) de cada palavra/token
# entidades_nomeadas = nltk.ne_chunk(palavras_tagueadas, 'portuguese') # Extrair Nomes de Entidades

# Vamos remover Stop Words
# from nltk.corpus import stopwords
# stop_words = set(stopwords.words('portuguese'))
# filtered_sentence = [w for w in palavras if not w in stop_words]
# filtered_sentence = []
#
# for w in palavras:
#     if w not in stop_words:
#         filtered_sentence.append(w) # 'filtered_sentence' é a variável SEM STOP WORDS

# Vamos remover pontuações
# punctuation=re.compile(r'[-.?!,–:/;()|0-9]') # Vamos definir as pontuações e números que devem ser eliminados
# post_punctuation=[]
# for words in filtered_sentence:
#     word=punctuation.sub('', words)
#     if len(word)>0:
#         post_punctuation.append(word) # 'post_punctuation' é a variável sem pontuações