import random
def primary():
        #last = 13
        #rnd = random.randint(0, last)
    f = open("C:/users/ola/documents/Python/Gitbud/python-random-quote/quotes.txt", encoding="utf-8")  #gör om txt filen till utf 8 så åäö '' syns
    quotes = f.readlines()
    f.close()
    quotesNy = []
    for element in quotes:
          quotesNy.append(element.strip())          #Lägger allt på egna rader
    print(*quotesNy, sep='\n')                      #Tar bort \n
primary()