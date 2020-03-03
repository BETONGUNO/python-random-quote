import random
def primary():
    
    f = open("C:/users/ola/documents/Python/Gitbud/python-random-quote/quotes.txt")
    quotes = f.readlines()
    quotesNy = []
    f.close()
    for element in quotes:
          quotesNy.append(element.strip())
    #last = 13
    #rnd = random.randint(0, last)
    print(quotesNy)

primary()
