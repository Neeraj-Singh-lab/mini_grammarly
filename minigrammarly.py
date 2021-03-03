#Mini_Grammarly-----------------------------------------------------------------------------------------  

from PyDictionary import PyDictionary
from translate import Translator
from textblob import TextBlob



def gram(n):
    print(n,'---->',end=" ")
    print(hindi,"\n")
    dictionary=PyDictionary(n)
    x=dictionary.meaning(n)
    if x is None:
        x={'Not Found':['Not Found']}
    else:
        pass
    print("Meaning: ",[i for i in x.values()][0][0],'\n')
    try:
        print ("Synonym: ",dictionary.synonym(n)[0],"\n" )
    except:
        pass
    try:
        print ("Antonym: ",dictionary.antonym(n)[0],"\n")
    except:
        pass
    print("Grammar: ",[i for i in x.keys()])

while True:
    g=input("Enter the word: ")
    b = TextBlob(g)

    g=str(b.correct())
    print("Correct word: ", g)


    #translation
    tran= Translator(to_lang="Hindi")
    hindi = tran.translate(g)

    if " " not in g:
        gram(g)
    elif " " in g:
        print(g,'---->',end=" ")
        print(hindi,"\n")
    else:
        quit()

