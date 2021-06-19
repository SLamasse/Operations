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
    des matrices. On pourra compter la quantité de chiffres écrits ce
    qui suppose de calculer la taille de la matrice et pour cela de
    connaitre les plus grands chiffres pour la largeur, la longueur
    est donnée par les  type de nombre + résultats intermédiaires
    fraction 2 lignes et ici 2 résultats intermédiaires 
    """

    i = 0
    reduction = []
    while i < len(numerateur):
        denom = denominateur[i]
        num = numerateur[i]
        denominateur_commun = multiplierlist(rs)
        multiplicateur = denominateur_commun//denom
        d1 = denom*multiplicateur
        n1 = num*multiplicateur
        reduction.append(str(n1) + "/" + str(d1))
        i += 1 
    return reduction




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
rout = ["1/2","1/3", "3/4","5/6", "3/8", "7/12", "19/24"]
res = reduire_rout(rout)
print(res)

#for elt in rout:
#    if len(elt)>1:
#        abr = abrevie_rout(elt)
#        frac = reduc_rout_de_rout(elt)
#        print(frac)
#    else:
#        frac = elt
#        abr = abrevie_rout(frac)
#        print(abr)
