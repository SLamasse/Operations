
def T_GrandDenomDiviseurCommun(lst):
    l = sorted(lst, reverse=True)
    i = 0
    r = True
    while i < len(l):
        if l[0]%l[i]==0:
            pass
        else:
            r = False
        i += 1
    return r

def soustrairelistemultiples(lstdenom):
    #
    # On ne doit garder que les plus petits multiples d'un nombre
    #
    lst = sorted(lstdenom.copy()) # On ordonne du plus grand au plus
    # petit
    m = []
    for el in lst :
        if el%2==0:
            lst.remove(el)
    return lst


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


