#!/usr/bin/env python
# coding: utf-8

# # Project Name:  "Text Editor with Grammerly"   

# # By Neeraj Singh 2020uch0009

# In[3]:


#---------------------INTRODUCTION----------------------------
'''
No Need to write each lines song in input,as it is already stored in side
You need to give only command to get desired output...
But still you can add/delete more lines to the song
*********If you input wrong spelling of word, output will tell correct splelling********* 
Note: input the words of given song only provided by sir
It will also tell you total verbs,nouns pronouns,adjective, adverb,interjection,preposition with just one command
I can make my program much better by using file handling and import libraries but it is not allowed....
I can make my program much better by using file handling and 
import libraries, ising try except but it is not allowed....

'''
#*********************COMMANDS****************************************
#-SNo--WORK------------------SYNTAX--------------------EXAMPLE---------------
'''
0  SHOW CORRECT SPELLING     > check line             > check set le mance asled sever nook dry tomight
                                            OUTPUT:   > corrected: Let me dance asked never look cry tonight 

1  TO ADD A NEW LINE         > add line               > add Let me love you   
2  TO DELETE A LINE          > del line               > del Let me love you
3  TO VIEW DOCUMENT          > show doc               > show doc
4  TO FIND MEANING OF WORD   > mean word              > mean look
5  FIND MEANING OF ALL WORDS > mean all               > mean all
6  CHECK PRESENCE OF A WORD  > find word              > find hero
7  REPLACE OLD TO NEW        > replace old new        > replace Let Now
8  COUNT OCCURENCE OF WORD   > occur word             > occur tonight
9  FREQUENCY OF EACH WORD    > all_word               > all_word
10 TO PRINT UNIQUE WORD      > unique                 >unique
11 SHOW LINE CONTAINING A WORD > see word             >see dance 
12 TO SHOW DESIRED LINE      > line number            >line 10
13 TO PRINT IN LOWER CASE    > upper                  >upper
14 TO PRINT IN UPPER CASE    > lower                  >lower
15 COUNT TOTAL LINES         > total_lines            >total_lines
16 COUNT TOTAL WORDS         > count_words            >count_words 
17 COUNT TOTAL LETTERS       > count_alpha            >count_alpha
18 VIEW REVERSED DOCUMENT    > reverse doc            >reverse doc 
19 EACH LINE REVERSED        > reverse line           >reverse line
20 EACH WORD REVERSED        > reverse words          >reverse words
21 FIRST LETTER CAPITAL EACH WORD> alternate          >alternate
22 ASCENDING ORDER           > view ascend            >view ascend 
23 DESCENDING ORDER          > view descend           >view descend
24 TO VIEW ALL NOUNS         > show noun              >show noun
25 TO VIEW ALL PRONOUNS      > show pronoun           >show pronoun
26 TO VIEW ALL ADJECTIVE     > show adjective         >show adjective
27 TO VIEW ALL ADVERB        > show adverb            >show adverb
28 TO VIEW ALL VERB          > show verb              >show verb
29 TO VIEW ALL INTERJECTION  > show interjection      >show interjection
30 TO QUIT                   > quit                   >quit


'''




# In[ ]:



#CODES
lines=['Let me be your hero',
      'Would you dance',
      'If I asked you to dance ?',
      'Would you run',
      'And never look back ?',
      'Would you cry',
      'If you saw me crying ?',
      'And would you save my soul, tonight ?',
      'Would you tremble', 'If I touched your lips ?',
      'Would you laugh ? ', 'Oh please tell me this.',
      'Now would you die', 'For the one you loved ?',
      'Hold me in your arms, tonight.',
      'I can be your hero, baby.',
      'I can kiss away the pain.',
      'I will stand by you forever.',
      'You can take my breath away.',
      'Would you swear', "That you'll always be mine ?",
      'Or would you lie ?', 'Would you run and hide ?',
      'Am I in too deep ?', 'Have I lost my mind ?',
      "I don't care...", "You're here tonight.",
      'I can be your hero, baby.',
      'I can kiss away the pain.',
      'I will stand by you forever.',
      'You can take my breath away.',
      'Oh , I just want to hold you.',
      'I just want to hold you , oh , yeah.',
      'Am I in too']

#making list of words
words=[]
for line in lines:
    y=line.split()
    for j in y:
        if j!='?' and j!="," and j!=".":
            words.append(j)

#-----------------------------------------------------------------------

#ADDING HAND MADE DICTIONARY
eng_dict={'let': ['verb', 'to allow or permit'],
         'me': ['pronoun', 'the objective case of I, used as a direct or indirect object'],
         'be': ['verb', 'to exist or live'],
         'your': ['pronoun', 'a form of the possessive case of you used as an attributive adjective'],
         'hero': ['noun', 'a person noted for courageous acts or nobility of character(Vinit Sir)'],
         'would': ['verb', 'a simple past tense and past participle of will'],
         'you': ['pronoun', 'the pronoun of the second person singular or plural'],
         'dance': ['verb', "to move one's feet or body, or both, rhythmically in a pattern of steps"],
         'if': ['conjunction', 'in case that; granting or supposing that'],
         'i': ['pronoun', 'addressing himself'],
         'asked': ['verb', 'to put a question to; inquire of'],
         'to': ['preposition', 'used for direction toward a point, person, place'],
         'run': ['verb', 'to go quickly'],
         'and': ['conjunction', 'used to connect grammatically coordinate words'],
         'never': ['adverb', 'not ever; at no time'],
         'look': ['verb ', "to turn one's eyes toward something or in some direction in order to see"],
         'back': ['verb', 'to go or move backward'],
         'cry': ['verb', 'to weep'],
         'saw': ['verb', 'to see'],
         'crying': ['verb', 'weeping,sheding tears, with or without sound.'],
         'save': ['verb', 'to keep safe, intact, or unhurt'],
         'my': ['pronoun', 'a form of the possessive case of I used as an attributive adjective'],
         'soul': ['noun', 'the spiritual part of humans as distinct from the physical part'],
         'tonight': ['noun', 'this present or coming nigh'],
         'tremble': ['verb', 'to shake involuntarily with quick, short movements, as from fear, excitement'],
         'touched': ['adjective', 'affected with emotion; moved, especially with sympathy or gratitude'],
         'lips': ['noun', 'either of the two fleshy parts or folds forming the margins of the mouth'],
         'laugh': ['verb', 'to express, pleasure, derision,  with an audible, vocal expulsion of air'],
         'oh': ['interjection', 'used as an expression of surprise, pain, disapprobation, etc.'],
         'please': ['adverb', 'used as a polite addition to requests, commands, etc.'],
         'tell': ['verb', 'to give an account or narrative of; narrate'],
         'this': ['pronoun', 'used to indicate a person, thing, idea, state, event, time, remark'],
         'now': ['adverb', 'at the present time or moment'],
         'die': ['verb', 'to cease to live; undergo the complete and permanent cessation of all vital functions'],
         'for': ['preposition', 'with the object or purpose of'],
         'the': ['article', 'used, especially before a noun'],
         'one': ['advective', 'being or amounting to a single unit or individual or entire thing'],
         'loved': ['verb', 'a profoundly tender, passionate affection for another person.'],
         'hold': ['verb', 'to have or keep in the hand; keep fast; grasp'],
         'in': ['preposition', 'used to indicate inclusion within space, a place, or limits'],
         'arms': ['noun', 'weapons collectively'],
         'can': ['verb', 'to be able to; have the ability, power, or skill to'],
         'baby': ['noun', 'an infant or very young child'],
         'kiss': ['verb', 'to touch or press with the lips slightly pursed'],
         'away': ['adverb', 'from this or that place; off'],
         'pain': ['noun', 'physical suffering or distress, as due to injury, illness, etc.'],
         'will': ['verb', 'am (is, are, etc.) about or going to'],
         'stand': ['verb', 'to be in an upright position on the feet'],
         'by': ['preposition', 'near to or next to'],
         'forever': ['adverb', 'without ever ending; eternally'],
         'take': ['verb', "to get into one's hold or possession by voluntary action"],
         'breath': ['noun', 'respiration, especially as necessary to life'],
         'swear': ['verb', 'to make a solemn declaration by sacred being or object, as a deity or the Bible.'],
        'always': ['adverb', 'every time; on every occasion; without exception'],
         'mine': ['pronoun', 'something that belongs to me'],
         'lie': ['noun', 'a false statement made with deliberate intent to deceive; an intentional untruth'],
         'hide': ['verb', 'to conceal from sight; prevent from being seen or discovered'],
         'too': ['adverb', 'in addition; also; furthermore; moreover'],
         'deep': ['adjective', 'extending far down from the top or surface'],
         'have': ['verb', 'to possess; own; hold for use; contain'],
         'lost': ['adjective', 'no longer possessed or retained'],
         'mind': ['verb', 'to pay attention to'],
         "don't": ['verb', 'contraction of do not'],
         'care': ['noun', 'a state of mind in which one is troubled; worry, anxiety, or concern'],
         'here': ['adverb', 'in this place; in this spot or locality'],
         'just': ['adjective', 'guided by truth, reason, justice, and fairness'],
         'want': ['verb', 'to feel a need or a desire for; wish for']}
#code for meaning and grammar
def eng(n):
    for y in eng_dict.keys():
        if n==y:
            print(n,"("+(eng_dict[y])[0]+")",":"+(eng_dict[y])[1])
            break
        elif n==(eng_dict[y])[0]:
            print(y)
        elif n=="all":
            print(y,"---->",eng_dict[y])
            
 
#-----------------------------------------------------------------------
#code for unique word
def uni():
    l=[]
    for i in words:
        max=0
        for j in words:
            if i==j:
                max=max+1
        if max==1:
            l.append(i)
    print(l)
#--------------------------------------------------------------------

#code To count total number of WORDS in parragraph
def c_w(x):
    return len(x)
#--------------------------------------------------------------------
#To print whole document
def doc():
    for i in lines:
        print(i)
#-----------------------------------------------------------------------
#To count total number of ALPHABETS

def c_alpha():
    h=0
    for i in words:
        for o in i:
            if (o>='A' and o<="Z") or (o>='a' and o<="z"):
                h=h+1

    return h
#-----------------------------------------------------------------------
# Code to count no of particular letter searched by user

def c_let(s):
    h=0
    for i in words:
        for o in i:
            if o.lower()==s:
                h=h+1

    print(h)
#-----------------------------------------------------------------------
#Code Search any word is available in the Song
def fi(a):
    if a in words:
        return "Yes It is present"
    else:
        return "Ooops No such word found!!!"
#-----------------------------------------------------------------------
# Count total lines of song
def li():
    a=0
    for i in lines:
        a=a+1
    print ("Total lines are:",a)
#-----------------------------------------------------------------------
# code to count no of particular words searched by user

def pword(x):
    n=0
    for i in words:
        if i==x:
            n=n+1
    print(x,"occurs",n,"times")

#-----------------------------------------------------------------------
# Code to print the line in which that input word occurs
def lword(x):
    for i in lines:
        if x in i:
            print(i)
#-----------------------------------------------------------------------
#code to print lines in upper and lower case
def upp(x):
    for i in lines:
        s=""
        for j in i :
            if x=="upper":
                if j >= "a" and j <= "z":
                    s=s+chr(ord(j)-32)
                else:s=s+j
            else:
                if j>="A" and j <="Z":
                    s=s+chr(ord(j)+32)
                else:
                    s=s+j 
        print(s)

#-----------------------------------------------------------------------
# for replace : replace old_word new_word"
def rep(x,y):
    global lines
    l=[]
    print( "Successfully replaced!")
    print( "See below")
    for i in lines:
        n=i.split()
        s=''
        for j in n:
            if j==x:
                s=s+y+" "
            else:
                s=s+j+" "
        l.append(s.strip())
        print(s)
    
    q=input("Do you want to Save or Not: Enter yes or no")
    if q=="yes":
        lines=l
        print("Successfully Saved")
    else:
        print( "No changes done to original document")
#-----------------------------------------------------------------------
# count the frequency of all words that occur in song
def dic_words():
    dic={}
    for i in words:
        if i in dic.keys():
            dic[i]=dic[i]+1
        else:
            dic[i]=1
    for i in dic.keys():
        print(i,dic[i])
#-----------------------------------------------------------------------
# first letter of each word becomes Capital
def alt():
    n=[]
    for i in lines:
        s=''
        for j in i.split():
            if j[0]>='a' and j[0]<='z':
                k=chr((ord(j[0])-32))
            else:
                k=j[0]
            k=k+j[1::]
            s=s+k+" "
        print(s)
#-----------------------------------------------------------------------            
# print all words in ascending order  
def chote_se_bada(p):
    k=[]
    for i in words:
        k.append(i.lower())
    k=list(set(k))
    for j in range(len(k)):
        f=0
        for i in range(len(k)-1-j):
            if k[i]<=k[i+1]:
                k[i],k[i+1]=k[i+1],k[i]
                f=1
        if f==0:
            break
    if p=="descend":
        print(k)
    else:
        print(k[::-1])
   
#-----------------------------------------------------------------------
#spelling check
def gram(x):
    word=[]
    count=[]
    for i in words:
        if len(i)==len(x) :
            c=0
            for j in range(len(x)):
                if i[j]==x[j]:
                    c=c+1


            word.append(i)
            count.append(c)
    xx=max(count)
    for i in range(len(word)):
        if count[i]==xx:
            return (word[i])


    
    
#The real code is here...............
print("Song is already stored in databases"+"\n"+"You need to give only commands or Tasks: ")

print("STILL, If you want to enter song  lines by yourself Enter: add line ")

        
    

while True:
    x=input("Enter TASK: ").split()
    if x[0]=="show":
        if x[1]=="doc": #show doc
            doc()
        elif x[1]=="noun":eng(x[1])# show noun
        elif x[1]=="pronoun":eng(x[1])#show pronoun
        elif x[1]=="verb":eng(x[1])#show verb
        elif x[1]=="preposition":eng(x[1])#show preposition
        elif x[1]=="adverb":eng(x[1])#show adverb
        elif x[1]=="interjection":eng(x[1])# show interjection
        elif x[1]=="adjective":eng(x[1])#show  adjective
        else:
            print("Check spelling or No such recird found")
            
    elif x[0]=="count_words":#count_words
        print("Total words are: ",c_w(words))
    elif x[0]=="count_alpha":#count_alpha
         print("Total aplhabets are: ",c_alpha())
    elif x[0]=="find":#find word
        print(fi(x[1]))
    elif x[0]=="total_lines":# total lines
        li()
    elif x[0]=="occur":#occur word
        pword(x[1])
    elif x[0]=="see":#see word
        lword(x[1])
    elif x[0]=="line":# sshow desired line
        print(lines[int(x[1])+1])
    elif x[0]=="upper":#upper
        upp(x[0])
    elif x[0]=="lower":#lower
        upp(x[0])
    elif x[0]=="count": #count letter
        c_let(x[1])
    elif x[0]=="reverse":
        if x[1]=="doc":#reverse doc
            for i in lines[::-1]:
                print(i)
        elif x[1]=="words":#reverse lines
            for i in lines:
                print(i[::-1])
        elif x[1]=="lines":#reverse words
            for i in lines:
                s=""
                for k in (i.split())[::-1]:
                    s=s+k+" "
                print(s)      
    elif x[0]=="replace":# replace old new
        rep(x[1],x[2])
    
    elif x[0]=="all_word":#all_word count frequecy
        dic_words()
    elif x==['alternate']:#capital first letter of each word
        alt()
    elif x[0]=='view':#alphabetic print
        chote_se_bada(x[1])
    elif x[0]=="unique":#unique words -> occuring only once
        uni()
    elif x[0]=="add":# add line........
        s=''
        for i in x[1::]:
            s=s+i+"  "
        lines.append(s.strip())
        print("Successfully Added")
    elif x[0]=="del":# del line..........
        s=''
        for i in x[1::]:
            s=s+i+"  "
        lines.remove(s.strip())
        print("Successfully Deleted")
        
    elif x[0]=="mean":#meaning word
        b=x[1]
        eng(b)
    elif x[0]=="check":
        print("corrected: ",end='')
        
        for i in x[1::]:
            print(gram(i),end=" ")
        print()
    
    elif x==["quit"]:#quit
        quit()
    else: print("Ooops !Could Not find this task Try again")
#Code Ends-----------------------------------------------------------------------------------

#EXECUTION BELOW
    


# In[ ]:




