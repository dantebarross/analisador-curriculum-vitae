import nltk
from numpy import arange
from matplotlib import pyplot
from nltk.corpus import brown

# Gerar tabelas
def tabulate(cfdist, words, categories):
    print('{:16}'.format('Category'), end=' ')                    # column headings
    for word in words:
        print('{:>6}'.format(word), end=' ')
    print()
    for category in categories:
        print('{:16}'.format(category), end=' ')                  # row heading
        for word in words:                                        # for each word
            print('{:6}'.format(cfdist[category][word]), end=' ') # print table cell
        print()                                                   # end the row

cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))
genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
tabulate(cfd, modals, genres)



# Gerar gráficos
colors = 'rgbcmyk'  # red, green, blue, cyan, magenta, yellow, black

def bar_chart(categories, words, counts):
    "Plot a bar chart showing counts for each word by category"
    ind = arange(len(words))
    width = 1 / (len(categories) + 1)
    bar_groups = []
    for c in range(len(categories)):
        bars = pyplot.bar(ind + c * width, counts[categories[c]], width,
                          color=colors[c % len(colors)])
        bar_groups.append(bars)
    pyplot.xticks(ind + width, words)
    pyplot.legend([b[0] for b in bar_groups], categories, loc='upper left')
    pyplot.ylabel('Frequency')
    pyplot.title('Frequency of Six Modal Verbs by Genre')
    pyplot.show()

genres2 = ['news', 'religion', 'hobbies', 'government', 'adventure']
modals2 = ['can', 'could', 'may', 'might', 'must', 'will']
cfdist = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in genres2
    for word in nltk.corpus.brown.words(categories=genre)
    if word in modals2)

counts = {}
for genre in genres2:
    counts[genre] = [cfdist[genre][word] for word in modals2]

bar_chart(genres2, modals2, counts)