import random
import time

def code_alea(): # renvoyer une liste de 4 éléments allant de 0 à 5 aléatoirement
    Secret=[]
    for i in range(4): # nombre de trous
        x=random.randint(0,5) # associer une des 6 couleurs à chaque trou aléatoirement
        Secret.append(x) # ajouter le numéro de la couleur à la liste
    return(Secret) # renvoyer une liste de 4 éléments allant de 0 à 5 aléatoirement


# Prendre en entrée 2 propositions sous forme de 4-liste
# renvoyer un entier dont le chiffre des dizaines correspond au nombre de boules...
# ...de la même couleur et placées dans le même trou et le chiffre des unités correspond...
# ...au nombre de boules de la même couleur mais placées dans un trou différent 
def score(S,P):  
   r=0
   for i in range(4): # Pour chaque trou
       if S[i]==P[i]: # Si 2 boules ont la même couleur dans le même n° de trou
           r=r+1      # Ajouter 1 au chiffre des dizaines du score
   b=-r 
   for j in range(6): # Pour chaque couleur
       n=0
       m=0
       for k in range(4): # Pour chaque trou
           if S[k]==j:    # Pour le  code secret si la boule d'emplacement k est de couleur j
               n=n+1      # augmenter le compteur n d'une unité
           if P[k]==j:    # Pour la  proposition si la boule d'emplacement k est de couleur j
               m=m+1      # augmenter le compteur m d'une unité
       if n<m:            # S'il y a plus de boules de couleur j dans la prop que dans le code
           b=b+n          # le chiffre des unités est n soustrait au chiffre des dizaines
       else:              # Sinon
           b=b+m          # le chiffre des unités est m soustrait au chiffre des dizaines
   s=10*r+b               # le score est le chiffre des unités additionné au chiffre des dizaines
   return(s)

# renvoyer une liste de l'ensemble des listes allant de [0,0,0,0] à [5,5,5,5]
# nous piocherons dans cette liste les listes dont nous aurons besoin dans les algorithmes
def ens():
    E=[]
    for j0 in range(6):
        for j1 in range(6):
            for j2 in range(6):
                for j3 in range(6):
                    L=[j0,j1,j2,j3]
                    E.append(L)
    return(E)

E=ens()

# trouver le code secret à partir de la proposition précédente et renvoyer le nombre de coups pour le trouver
def force_brute(S):
    n=1 # n correspond au nombre de coups
    P=[0,0,1,1] # P est ici la proposition initiale
    sc=[score(S,P)] # sc est la liste contenant le score entre la propositon initiale et le code secret
    if sc[0]==40:
        return(n)  # si P est le code secret renvoyer n=1
    else:
        while sc[n-1]!=40: # tant que P n'est pas le code secret
            for i in range(len(E)):
                if score(E[i],P)==sc[-1]: # si le score entre un élément de la liste complète avec P
                    P=E[i] # est le même que le score entre P et la solution affecter P à cet élément
                    sc.append(score(S,P)) # ajouter le score de P avec le code secret à sc
                    n+=1 # porter le nbre de coup à une unité de plus
    return(n) # renvoyer le nombre de coups n pour trouver le code secret

def stat(f):  
    L=[]
    M=[]
    n=1
    s=0
    for i in E:
        L.append(f(i)) # Crée une liste correspondant au nbre de coups pour résoudre chaque solution
    while sum(M)!=len(E): # Tant que toutes les solutions ne sont pas résolues en un nbre de coup donné
        for i in L:
            if i==n:
                s+=1 # compte le nombre de solutions résolues en un nbre de coups
        M.append(s)
        s=0
        n+=1
    return(M)

#permet de voir le nombre de listes de la liste complète résolues en un nombre de coups donné

FB=[1, 12, 24, 37, 42, 54, 69, 99, 85, 95, 107, 130, 100,
    92, 85, 80, 54, 40, 34, 24, 12, 6, 5, 2, 2, 3, 0, 1, 1]

# trouver le code secret à partir des propositions précédentes et renvoyer le nombre de coups pour le trouver
def algo1(S):
    n=1 # n correspond au nombre de coups
    P=[0,0,1,1] # P est ici la proposition initiale
    L=[P] # L est la liste où seront stockées les propositions
    sc=[score(S,P)] # sc est la liste contenant le score entre la propositon initiale et le code secret
    if sc[0]==40:
        return(n) # si P est le code secret renvoyer n=1
    else:
        while sc[n-1]!=40: # tant que P n'est pas le code secret
            for i in range(len(E)): # pour parcourir la liste l'ensemble des solutions possible
                j=0
                while j<=n-1 and score(L[j],E[i])==sc[j]: #si le score entre les P et une liste a le même 
                    j=j+1  #score que les P avec avec le code secret
                if j==n:
                    P=E[i] # affecter à P cette liste
                    L.append(P) # ajouter la proposition P à L
                    sc.append(score(S,P)) # ajouter le score de P avec le code secret à sc
                    n+=1
    return(n) # renvoyer le nombre de coups n pour trouver le code secret

def stat_a1():  
    L=[]
    M=[]
    n=1
    s=0
    for i in E:
        L.append(algo1(i)) # Crée une liste correspondant au nbre de coups nécessaire pour résoudre chaque solution
    while sum(M)!=len(E): # Tant que toutes les solutions ne sont pas résolues en un nbre de coup donné
        for i in L:
            if i==n: 
                s+=1 # compte le nombre de solutions résolues en un nbre de coups
        M.append(s) 
        s=0
        n+=1
    return(M)

#permet de voir le nombre de listes de la liste complète résolues en un nombre de coups donné
 

A1=[1, 12, 70, 260, 561, 309, 76, 7]

# Prend en entrée une liste de stats et renvoie la moyenne de nombre...
# ... de coups nécessaire pour trouver la solution sous forme flottants
def moyenne(R):
    n=0
    r=0
    for i in range(len(R)):
        n+= (i+1)*R[i]
        r+= R[i]
    return(round(n/r,2))


# Prend en entrée une liste de stats et renvoie la fréquence et la fréquence cumulée...
# ... (en %) pour chaque nombre de coups nécessaire sous forme de couple de flottants
def frequence(R):
    F=[]
    Fc=[]
    n=0
    for i in range(len(R)):
        f=(R[i]/len(E))*100
        F.append(round(f,1))
        n+=F[i]
        Fc.append(round(n,2))
    return(F,Fc)


sco=[0,1,2,3,4,10,11,12,13,20,21,22,30,40]


def BestProp(C): # Renvoie la meilleure proposition pour une liste de candidats donnéee
    n=0
    D={}
    L=[]
    P=[]
    for i in range(len(C)): # pour les propositions dans la liste des candidats
        for j in sco: # pour les scores dans la listes des scores
            for k in range(len(C)):  # pour les propositions dans la liste des candidats
                if (i,k) not in D: # si le score entre la liste C[i] et C[k] n'est pas dans le dictionnaire
                    D[(i,k)]=score(C[i],C[k]) # calculer ce score et le stocké dans D
                    D[(k,i)]=D[(i,k)] # le score étant symétrique, affecter ce score à (k,i)
                if D[(i,k)]==j: 
                    n+=1 # compte nb de liste de candidats ayant le même score qu'une liste candidat donnée
            L.append(n) # faire correspondre à chaque score ce nombre de liste de candidat
            n=0
        P.append(max(L)) # score ayant le plus grand nb de solutions est le poids correspondant à un candidat
        L=[]
    ppp=min(P) # prendre le plus petit poids de la liste des candidats
    for i in range(len(C)):
        if P[i]==ppp: # correspond au premier candidat qui a le plus petit poids
            return(C[i]) # renvoyer ce candidat


# Trouver le code secret en réduisant au maximum le nombre de candidats et...
# ... en choisissant la proposition la plus adaptée
def six_guess(S):
    C=E  # la liste des candidats initiale est la liste complète
    n=1 # on initialise le nombre de coups
    P=[0,0,1,1] # le proposition de la liste complète ayant le plus petit poids
    sc=score(S, P) # le score entre la solution et la proposition initiale
    if sc==40:
        return(n) # renvoyer 1 si la solution est la proposition initiale
    while sc!=40: # tant qu'on a pas trouver la solution
        L=[]
        for i in C: # pour les propositions dans la liste des candidats
            if score(P,i)==sc:
                L.append(i) # Ajouter à L candidats ayant le même score que la prop précédente avec la solution
        P=BestProp(L) # affecter à P la meilleure propostion parmi ces candidats
        C=L # pour l'éventuelle prochaine boucle affecter à C la liste des candidats
        sc=score(S,P) # calculer le score entre la nouvelle propositon et la solution
        n+=1 # augmenter le nombre de coups d'une unité
    return(n)
    
            
def stat_sg():  
    L=[]
    M=[]
    n=1
    s=0
    for i in E:
        L.append(six_guess(i))
    while sum(M)!=len(E):
        for i in L:
            if i==n:
                s+=1
        M.append(s)
        s=0
        n+=1
    return(M)

SG=[1, 12, 99, 468, 662, 54]

def BestProp2(C):
    n=0
    L=[]
    P=[]
    D={}
    for i in range(len(E)):
        for j in sco:
            for k in range(len(C)):
                if (i,k) not in D:
                    D[(i,k)]=score(E[i],C[k])
                if D[(i,k)]==j:
                    n+=1
            L.append(n)
            n=0
        P.append(max(L))
        L=[]
    ppp=min(P)
    for i in range(len(E)):
        if P[i]==ppp:
            if E[i] in C:
                return E[i]
    for i in range(len(E)):
        if P[i]==ppp:
            return E[i]

def fiveguess(S):
    C=E
    n=1
    P=[0,0,1,1]
    sc=score(S, P)
    if sc==40:
        return(n)
    while sc!=40:
        L=[]
        for i in C:
            if score(P,i)==sc:
                L.append(i)
        P=BestProp2(L)
        C=L
        sc=score(S,P)
        n+=1
    return(n)


def stat_fg():  
    L=[]
    M=[]
    n=1
    s=0
    for i in E:
        L.append(fiveguess(i))
    while sum(M)!=len(E):
        for i in L:
            if i==n:
                s+=1
        M.append(s)
        s=0
        n+=1
    return(M)

FG=[1, 6, 62, 533, 694]

def demande_proposition():
    p = input("Proposition ? ") # taper la proposition que l'on souhaite avec un espace entre chaque chiffre
    return [int(x) for x in p.split(" ")] # renvoyer cette proposition sous forme de 4-liste

def jeu():
    S=code_alea()  # le code secret est aléatoire
    n=0            # nb de coups
    t=1
    P=[]
    while P!=S and n!=12: # tant que la dernière proposition n'est pas le code et que le nb de coups est <=12
        n+=1              # le nombre augmente de 1 à chaque boucle
        t=n
        P= demande_proposition() # On choisit la dernière proposition P
        assert len(P)==4         # s'assurer que P est une 4-liste de nombres entre 0 et 5
        for i in range(4):
            assert P[i]>=0 and P[i]<=5
        blanc=score(S,P)%10     # le nb de drapeaux blancs est le chiffre des unités du score entre S et P
        rouge=score(S,P)//10    # le nb de drapeaux rouges est le chiffre des dizaines du score entre S et P
        if P!=S:                # si P n'est pas S indiquer le nb de drapeaux rouges et blancs
            print('Vous avez ',rouge,' drapeau(x) rouge(s) et ',blanc,' drapeau(x) blanc(s)')
        else:                  # sinon indiquer en quel nombre de tentative on a gagner
            n=12
            print('Vous avez gagné en', t,'tentatives!')
    print('La solution était ',S) # si on perd indiquer le code secret

# prends en entrée un algorithme et un nombre repésentant le nombre de répétition de la résolution ...
# ... de la liste complète par cet algorithme
# renvoie le temps de résolution de la liste complète, le temps moyen de résolution par code, ...
# ... l'écart-type pour la résolution de la liste complète et le code prenant le plus de temps
def temps(f,n):
    L=[]
    F=[]
    M=[]
    for i in range(n):  # répeter n fois le programme suivant
        J=[]            # J est une liste vide
        for j in E:     # pour chaque code de la liste complète
            debut = time.time()
            f(j)
            fin = time.time()
            J.append((fin-debut))  # ajouter à J le temps d'exécution de chaque code
        L.append(J)                # après chaque résolution de E, ajouter J à la liste L
    for j in range(len(E)):      # pour chaque indice de code de la liste complète
        s=0                      # créer un compteur
        for i in range(n):       # pour le nombre de boucle
            s += L[i][j]         # sommer les temps d'exécution de chaque code
        F.append(s/n)            # F est une liste de la moyenne de temps d'exécution de chaque code 
    maxi=max(F)                  # maxi est le temps d'exécution le plus long
    listecomp=sum(F)             # le temps d'exécution de la liste complète est la somme des codes
    for i in L:                  # pour chaque liste dans L
        M.append(abs(listecomp-sum(i)))  # calculer l'écart-type du temps d'exécution
    ecart = sum(M)/n
    return(round(listecomp,2),round(listecomp/len(E),4),ecart,maxi)

