import numpy as np
from outils.generalites import * 




def abrevie_rout(listrout, sep="/"):
    """
     Il s'agit de faire une simplification de fraction
    1. On isole le numérateur et le dénominateur chacun dans une liste
    """

    a, b = transformfrac(listrout, sep)

    """ 2. On cherche tous les facteurs premiers du numérateur et
    dénominateur 
    """
    num = decomp_fact_premier(a[0]) # numérateur
    denom = decomp_fact_premier(b[0]) # dénominateur

    """
    3. On appel une fonction qui permet d'enlever les facteurs communs aux dénominateurs et numérateurs puis de les multiplier entre eux
    """
    res1 = multiplierlist(SupprimerValeursIdentiques(num,denom))
    res2 = multiplierlist(SupprimerValeursIdentiques(denom,num))
    # 4. on produit une chaine qui permette de l'écrire comme Nicolas Chuquet
    chaine = str(res1) + "/" + str(res2)
    return chaine


def reduire_rout(listrout, sep="/"):
    """
     Il s'agit de réduire plusieurs fractions entre elles
     c'est-à-dire les mettre à un dénominateur commun 
     (fol 10 r -11v)

     1. On isole dénominateurs et nominateurs de chacune des
     fractions
    """
    nbfraction = len(listrout) # pour taille matrice de représentation
    #de l'opération
    numerateur, denominateur = transformfrac(listrout, sep)

    """
    2. "multiplier les denominateurs particuliers l'ung par l'aultre pour trouver denominateurs commun"
    On pourrait comprendre "denominateurs particuliers" comme
    "unique", si on trouvait plusieurs fois 3 on n'utiliserait 3
    qu'une seule fois mais il n'y a pas d'exemple de ce type. C'est
    pour cette raison que nous ne l'avons pas introduit dans le /else/
    mais nous continuons à lire le texte, alors ....

    Pour Chuquet, en revanche, il est inutile de multiplier tous les
    termes entre  eux. Il faut aupravant savoir si certains des
    dénominateurs sont contenus dans d'autres --- > il y a évidemment
    une économie de calcul
    """

    if T_GrandDenomDiviseurCommun(denominateur)==True:
        rs = [max(denominateur)]
    else:
        #rs = soustrairelistemultiples(denominateur)
        rs = denominateur

    """ 
    Rappel : choix graphique est de mettre les nombres/chiffres dans
    des matrices. 
    Ce qui suppose de calculer la taille de la matrice et pour cela de
    connaitre les plus grands chiffres pour la largeur, la longueur
    est donnée par les  type de nombre + résultats intermédiaires
    fraction 2 lignes et ici 2 résultats intermédiaires 

    Et il faut compter le nombre de chiffre 
    """
    signes = 0 # compter le nombre de signes écrits 
    i = 0
    reduction = []
    denominateur_commun = multiplierlist(rs)
    dessin = []
    while i < len(numerateur):
        denom = denominateur[i]
        num = numerateur[i]
        multiplicateur = denominateur_commun//denom
        d1 = denom*multiplicateur
        n1 = num*multiplicateur
        reduction.append(str(n1) + "/" + str(d1))
        dessin.append([str(n1),0,str(num),str(denom),0])


        # On ajoutes au dénombrement des signes graphiques écrits tous
        #les chiffres des fractions
        signes += len(list(str(denom))) + len(list(str(num)))
        signes += len(list(str(n1)))
        i += 1
    signes += len(rs)
    signes += (len(rs)//2)*len(list(str(denominateur_commun)))


    """ 
    On utilise  une matrice pour le dessin
    """
    ncol = nbfraction + (nbfraction//2)
    nblignes = len(dessin[0])
    x = np.zeros((nblignes,ncol)) # on définit la matrice avec des
    # valeurs à 0

    # Il faut essayer de mettre toutes les listes à la même dimension
    i = 0
    while i < len(x):
        j = 0
        while j < len(x[i]):
            if j%2==1:
                if i==nblignes-1:
                    x[i][j] = denominateur_commun
            else:
                k = j//2
                x[i][j] = dessin[k][i]
            j += 1
        i += 1
    return reduction, x, signes




def reduc_rout_de_rout(listfrac, sep="/"):
    # apparaît au folio 10 v
    # à faire 
    reduction = []
    numerateur, denominateur = transformfrac(listfrac, sep)
    multiplie_numerateur = multiplierlist(numerateur)
    multiplie_denominateur = multiplierlist(denominateur)
    reduction.append(str(multiplie_numerateur) + "/" + str(multiplie_denominateur))
    return reduction




#rout = [["12/60"], ["1/24"],["12/68"], ["6/8"], ["1/2","4/7", "10/11"]]


#rout =  ["1/4","3/2","1/2","1/6", "4/7", "1/5","10/11"]
rout = ["1/2","1/3",  "3/4","5/6", "3/8", "7/12", "19/24"]
#rout = ["1/3","5/7"]
res = reduire_rout(rout)
print(res[0])
print("Chuquet écrit " + str(res[2]) + " signes pour cette opération")
print(res[1])
#for elt in rout:
#    if len(elt)>1:
#        abr = abrevie_rout(elt)
#        frac = reduc_rout_de_rout(elt)
#        print(frac)
#    else:
#        frac = elt
#        abr = abrevie_rout(frac)
#        print(abr)
