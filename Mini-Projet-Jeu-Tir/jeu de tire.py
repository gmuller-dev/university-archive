    ############################
    #    -*-coding:Utf8 -*-    #
    #                          #
    #Mini Projet Jeu de tire   #
    #                          #
    #Mini Jeu de tire          #
    # fait avec TKinter        #
    #                          #
    #fait par codng101         #
    #                          #
    ############################





from tkinter import*


def disque(X,Y,R,bord,fond):
    ref = cadre.create_oval(X-R,Y-R,X+R,Y+R,outline=bord,fill=fond)
    return ref

def cible ():
    R1=120
    pas=R1//5
    couleur=["red","white","red","white","red"]
    for loop in range(5):
        disque(CentreX,CentreY,R1,"black",couleur[loop])
        R1=R1-pas
    
def deplacement(event):
    global nbtir
    key=event.keysym 
    if key=='Up':
        vit_v[1]-=2
    if key=='Down':
        vit_v[1]+=2
    if key=='Left':
        vit_v[0]-=2
    if key=='Right':
        vit_v[0]+=2
    if key=='space':
        ref_tir.append(disque(pos_v[0],pos_v[1],5,"white","black"))
        score(pos_v[0],pos_v[1])
        nbtir+=1
        
        
        
    return vit_v

def effacetout ():
    global ref_tir
    cadre.delete(*ref_tir)
    ref_tir=[]

def animation ():
    
    for i in range(2):
        
        if pos_v[i]>=limite[i]-1:
            pos_v[i]-=25
            pos_v[i]-=vit_v[i]*2
        if pos_v[i]<=limite[i+2]:
            pos_v[i]+=25
            pos_v[i]-=vit_v[i]*2
        else:
           pos_v[i]+= vit_v[i] 

    cadre.coords(ref_viseur,pos_v[0],pos_v[1])
    fen.after(100,animation)

def score(x,y):
    global Ptotal
    P=0
    d=((x-CentreX)**2+(y-CentreY)**2)**0.5
    if d<=24:
        P+=100
    if d<=48 and d>=24:
        P+=50
    if d<=72 and d>=48:
        P+=25
    if d<=96 and d>=72:
        P+=10
    Ptotal+=P
    return Ptotal
    
            
    
def afficheur():
    affiche.configure(text="SCORE:"+str (Ptotal)+" en "+str(nbtir)+" tirs")
    fen.after(10,afficheur)


def ttreset():
    global Ptotal
    effacetout()
    Ptotal=0
    


    
#constante
nbtir=0
pos_v=[45,350]
LARG=600
HAUT=400
CentreX=LARG//2
CentreY=HAUT//2
ref_tir = []
vit_v=[1,1]
limite=[LARG,HAUT,4,4]



#programme principale
fen=Tk()
cadre = Canvas(fen , width =600 , height = 400 ,bg= "light yellow",\
              bd = 3 ,relief = GROOVE )
cadre.pack()
arriere=PhotoImage(file='arriere.gif')

fond=cadre.create_image(CentreX,CentreY,image=arriere,anchor=CENTER)
cible()
Ptotal=0
viseur=PhotoImage(file='mir.gif')

cadre.bind_all('<Key>',deplacement)

ref_viseur=cadre.create_image(pos_v[0],pos_v[1],image=viseur,anchor=CENTER)

bEfface=Button(fen,text="RAZ" ,command = effacetout,bg="blue" ,bd=3)
bEfface.pack()
breset=Button(fen,text="Reset" ,command =ttreset ,bg="blue" ,bd=3)
breset.pack()
affiche = Label(fen,bg="blue", fg="white" , font =("Arial","25"))
affiche.pack()  
###############################################
afficheur()
animation()
fen.mainloop()
