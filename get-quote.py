import random
def primary():
        #last = 13
        #rnd = random.randint(0, last)
    f = open("C:/users/ola/documents/Python/Gitbud/python-random-quote/quotes.txt", encoding="utf-8")

    quotes = f.readlines()
    f.close()
    quotesNy = []
    for element in quotes:
          quotesNy.append(element.strip())


    print(*quotesNy, sep='\n')
primary()