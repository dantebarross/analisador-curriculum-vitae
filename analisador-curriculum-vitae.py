import fitz
import nltk, re, pprint


arquivo_pdf = 'cv_files/cv_danilo.pdf'
pdf = fitz.open(arquivo_pdf)
page = pdf.loadPage(0) # vai carregar apenas primeira página ('0')
text = page.getText('text')
text_replaced = (text.replace('●', ''))
#print(text_1)
pdf.close()

blank_lines_remover = text_replaced.split("\n")
non_empty_lines = [line for line in blank_lines_remover if line.strip() != ""]
texto_cv = ""
for line in non_empty_lines:
      texto_cv += line + "\n"


curriculum = (texto_cv.replace('\u200b', ''))

# with open('pagina0.txt', 'w') as file:
#     file.write(curriculum.replace('\t', ''))


# Aplicações do NLTK em cima do texto
palavras = nltk.word_tokenize(curriculum, 'portuguese') # Separar palavras
sentences = nltk.sent_tokenize(curriculum, 'portuguese') # Separar sentenças
palavras_tagueadas = nltk.pos_tag(palavras) # POS-TAG (Part-of-speech) de cada palavra/token
entidades_nomeadas = nltk.chunk.ne_chunk(palavras_tagueadas, 'portuguese') # Extrair Nomes de Entidades

nouns = [word for (word, pos) in palavras_tagueadas if pos in ['NN','NNP','NNS','NNPS']]
print(nouns)