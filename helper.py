def decoreer(tekst=""):
    tekst="header"
    lengte = len(tekst) + 4
    print()
    print(lengte * "*")
    print(f"* {tekst} *")
    print(lengte * "*")
    print()


def fooi_pp(bedrag, personen):   
    bedrag_pp = bedrag/personen    
    return f"De fooi per persoon is {bedrag_pp} euro"

#b = int(input("Welk bedrag zit er in de fooienpot? "))
#p = int(input("Over hoeveel mensen moet de pot verdeeld worden? "))
#print(fooi_pp(b,p))   

def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append('--' * len(tekst))
    return uit

def som(dictionary):
    return sum(dictionary.values())