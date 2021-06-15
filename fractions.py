
def touslesdiviseurs(nombre):
    # On recherche tous les diviseurs d'un nombre
    nombre = nombre//2
    diviseurs = [x  for x in range(0, nombre+1) if x != 0 and nombre % x == 0]
    return diviseurs



def decomp_fact_premier(n):
    """
    Décomposition d'un nombre entier n en facteurs premiers
    """
    result = []
    if n==1:
        # si le nombre est 1 on arrête le jeu
        return result
    else:
        # On commence par la parité 
        while n>=2:
            q,r = divmod(n,2) # renvoie quotien et reste
            if r!=0:
                break
            else:
                result.append(2) # on enregistre 2 dans la liste
                n = q
        # à ce niveau le reste à extraire n'est plus un multiple de 2 
        i=3
        while i<=n:
            if i % 2 == 0 :
                pass 
            else:
                q,r = divmod(n,i) # divise le nombre par impair : i 
                if r==0:
                    result.append(i)
                    n=q
                else:
                    i += 2
    return result


def nbmultipledansnombres(num, modulo):
    # On compte le nombre de fois qu'il y a le multiplie dans le nombre
    # afin de simplifier la fraction 
    i = 0
    q = []
    while i < num+1 :
        if num % modulo == 0:
            num = num // modulo
            q.append(int(1))
        i += 1
    return q


def multiplierlist(mylist):
    # Il s'agit de multiplier les éléments d'une liste entre eux
    product = 1
    for x in mylist:
        product *= x
    return product




def transformfrac(listrout, sep) :
    # Transforme la liste des fractions en deux listes de mêmes
    #longueurs, denominateurs et nominateurs
    numerateur = []
    denominateur = []
    for elt in listrout:
        a,b = elt.split(sep)
        numerateur.append(int(a))
        denominateur.append(int(b))    
    return numerateur,denominateur




def count_factors(thelist):
    # On compte le nombre d'occurrences de chaque nombre dans la liste
    dico = {}
    for elt in thelist:
        if elt in dico:
            dico[elt] += 1
        else:
            dico[elt] = 1
    lst = list(dico.items())
    return lst



def SupprimerValeursIdentiques(lst,lst1):
    l = lst.copy()
    l1 = lst1.copy()
    i = 0
    while i < len(l1):
        if l1[i] in l:
            l.remove(l1[i]) # n'efface que la première occurrence
            #dans une liste
        elif not l:
            l.append(1)
        i += 1
    return l


def abrevie_rout(listrout, sep="/"):
    # On met numérateur et denominateurs chacun dans une liste
    a, b = transformfrac(listrout, sep)
    # On cherche tous les facteurs premiers de chaque terme de la
    # fraction 
    lst1 = decomp_fact_premier(a[0]) # numérateur
    lst2 = decomp_fact_premier(b[0]) # dénominateur
    # En fait ici on pourrait faire une différence symétrique sur cet
    #ensemble.
    res1 = SupprimerValeursIdentiques(lst1,lst2)
    res2 = SupprimerValeursIdentiques(lst2,lst1)
    r1 = multiplierlist(res1)
    r2 = multiplierlist(res2)
    chaine = str(r1) + "/" + str(r2)
    return chaine


def reduc_rout(listrout, sep="/"):
    # fol 11r 
    # 1. On isole dénominateurs et nominateurs de chacun des fractions
    numerateur, denominateur = transformfrac(listrout, sep)
    multiplie_denominateur =  multiplierlist(denominateur)
    # 2. on fait l'opération pour chaque fraction
    i = 0
    reduction = []
    while i < len(numerateur):
        denom = denominateur[i]
        num = numerateur[i]
        intermediaire = multiplie_denominateur//denom
        reduction.append(str(intermediaire * num) + "/" + str(multiplie_denominateur))
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





rout = [["12/60"], ["1/24"],["12/68"], ["6/8"], ["1/2","4/7", "10/11"]]
for elt in rout:
    if len(elt)>1:
        frac = reduc_rout_de_rout(elt)
        print(frac)
    else:
        frac = elt
    abr = abrevie_rout(frac)
    print(elt)
    print(abr)
