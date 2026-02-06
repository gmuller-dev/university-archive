        ############################
        #    -*-coding:Utf8 -*-    #
        #                          #
        #Pendu_v0.67               #
        #                          #
        #jeux du pendu avec plus de#
        # trois cent mille mots    #
        #                          #
        #fait par codng101         #
        #                          #
        ############################
import os


from random import randint
play=1



#pendu graph
dessin=["""
---------------LE JEU DU PENDU---------------
    Vous avez uniquement 8 chances avant que
    l'on vous passe la corde au coup !!!
            Bonne chance !






""",
"""  Première erreur!
   
    
          
          
          
          
          
    
   ---
""",
"""
    |
    |
    |
    |
    |
    |
   ---
""",
"""   La potence est en place!
    --------
    | /      
    |/       
    |      
    |      
    |       
    |
   ---
""",
"""  Vous monté(e) sur l'échaffaut!
    --------|
    | /     |
    |/       
    |     
    |      
    |       
    |
   ---
""",
"""  Vous avez le corde au coup! 
    --------|
    | /     |
    |/      0
    |      
    |       
    |       
    |
   ---
""",
"""
    --------|
    | /     |
    |/      0
    |      \|
    |       
    |       
    |
   ---
""",
""" La fin est proche!
    --------|
    | /     |
    |/      0
    |      \|/
    |       
    |       
    |
   ---
""",
"""
    --------|
    | /     |
    |/      0
    |      \|/
    |       |
    |      /  
    |
   ---
""",
"""
    --------|
    | /     |
    |/      0
    |      \|/
    |       |
    |      / \   
    |
   ---
"""]
while(play):
    fichierMots = open("listedemots.txt",'r')

    listeMots = fichierMots.readlines()
    fichierMots.close()
    motCache=""
    motMystere = listeMots[randint(0, len(listeMots)) -1][:-1]
    for i in range(len(motMystere)):
        
        if motMystere[i]!="-" :
            motCache +='*'
        elif motMystere[i]==" ":
            motMystere.remove(" ")
        else:
            motCache +="-"

    letfausse=" "

    lettreEntre=[]
    err=0
    x=1
    while (x):
        
        print(dessin[err])
        
        print(motCache)
        
        print("\nProposez une lettre.")
        motEntre = input("Alors? :")
       

        print("-----------------------------------------------------------------")
        trouve =False
        os.system("cls")
        
        lettreEntre.append(motEntre)
        loopmot = lettreEntre
        if motEntre !=" ":
            for a in range(len(loopmot)):
                if lettreEntre[a]== "/":
                    lettreEntre.remove("/")
                    loopmot = lettreEntre
                    continue
                if lettreEntre[a]== "!":
                    lettreEntre.remove("!")
                    loopmot = lettreEntre

                    
        if len(motEntre)>1:
            print("Trop de caractère")
            lettreEntre.remove(motEntre)
            loopmot = lettreEntre


            
        if motEntre==" ":
            print ("Caractére invalide")
            lettreEntre.remove(motEntre)
            loopmot = lettreEntre

                    
        lettreEntre.sort()
        print("Voilà les lettres entrées ultérieurement:",lettreEntre)
        if motEntre=="/" :
            print ("Le mot est :",motMystere)
            err-=1
        if motEntre=="!":
            err= -1
        
        
        for i in range(len(motMystere)):
            if motEntre == motMystere[i]:
                motCache=motCache[:i]+motEntre+motCache[i+1:]
                trouve=True
        
       
            
    
        if trouve==False:
            err=err+1
            letfausse=letfausse+motEntre
        
    
        if motMystere == motCache:
                x=0
                print("Vous avez gagné!!!En",err,"erreur. \n Le mot était :",motMystere) 
        if err>8:
            print("Vous êtes mort dans d'affreuses souffrances car vous avez fait trop d'erreurs")
            x=0
            print("Le mot était :",motMystere)
       
    end=input("Fin\n Recommencer? Y/N ")
    if end=="y" :
        play=1
    else :
        play=0

if end=="n":
    print("\n good bye \n thanks for playing\n Game by Muller Guillaume")
    input()
        


    

    
            
