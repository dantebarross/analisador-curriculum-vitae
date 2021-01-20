from pdf2image import convert_from_path # Conversor de PDF para Imagem
from PIL import Image # Pillow para abrir a imagem
import pytesseract # Executar tecnologia OCR na imagem
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe' # Para usuários do Windows
import nltk, re, pprint


'''
Por enquanto, esse software está tendo muitos problemas por conta da leitura OCR. As falhas de leitura são diversas
e prejudicam muito na hora de processar o texto. Possíveis resoluções: 
1. Transformar o PDF em WORD;
2. Utilizar um leitor OCR melhor, como o do Google API;
3. Se não der certo, apenas trabalhar com formato WORD.
'''


def pdf_to_jpg(arquivo):
    pages = convert_from_path('cv_files/'+ arquivo + '.pdf', 500) # a última variável é o DPI da imagem. Quanto maior, mais qualidade e tamanho
    for page in pages:
        page.save('cv_files/' + arquivo + '.jpg', 'JPEG')

def jpg_to_text(arquivo):
    texto = (pytesseract.image_to_string(Image.open('cv_files/' + arquivo + '.jpg'), lang='por'))  # Extraindo o texto da imagem
    return texto



arquivo = 'cv_danilo' # Altere o nome do arquivo a ser convertido
pdf_to_jpg(arquivo) # Chama função para converter pdf em jpg
texto_cv = jpg_to_text(arquivo) # Chama função para converter jpg em txt e associa à variável 'texto'

# Aplicações do NLTK em cima do texto
palavras = nltk.word_tokenize(texto_cv, 'portuguese') # Separar palavras
sentences = nltk.sent_tokenize(texto_cv, 'portuguese') # Separar sentenças
palavras_taguedas = nltk.pos_tag(palavras, 'portuguese') # POS-TAG (Part-of-speech) de cada palavra/token
entidades_nomeadas = nltk.chunk.ne_chunk(palavras_taguedas, 'portuguese') # Extrair Nomes de Entidades





