from outils.generalites import * 





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
