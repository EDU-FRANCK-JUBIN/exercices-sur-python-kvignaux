import re
chaine = input("Entrée un nombre > 50 ")
if(isValid(chaine)):
    print('isok')
else:
    print('Veuillez rentré une chaine valide')


def isValid(chaine):
    regex = re.compile('[atcg]')    # if it got only 'a' 'g' 't' or 'c'
    return(regex.match(chaine))


def nbOccurence():

