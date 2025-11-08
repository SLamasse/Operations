from rich.console import Console
from rich.table import Table
from typing import Dict, Optional

# Initialisation de la console rich pour un affichage stylisé
console = Console()

def generer_table_proportional(base: int, max_denomination: int) -> Dict[int, int]:
    """
    Génère la table de correspondance Nombres (puissances) <-> Dénominations (exposants)
    pour la base et la limite d'itération données.
    
    Args:
        base: La base de la progression géométrique (ex: 2, 3, 10).
        max_denomination: La plus haute dénomination à calculer (nombre d'itérations - 1).
        
    Returns:
        Un dictionnaire {Nombre: Dénomination}.
    """
    table = {}
    for denomination in range(max_denomination + 1):
        # Calcul : Base à la puissance de la Dénomination
        nombre = base ** denomination 
        table[nombre] = denomination
    return table

# --- Fonctions d'Affichage et de Calcul ---

def afficher_table(base: int, table_data: Dict[int, int]):
    """Affiche la table de correspondance en utilisant rich, avec Nombres à gauche
       et Dénominations à droite, les deux colonnes étant alignées à droite."""
    table = Table(title=f"Table des Nombres Proporcionals (Base {base})")
    
    # 1. Colonne de gauche (Nombres) : Aligné à droite
    table.add_column("Nombres", style="magenta", justify="right")
    # 2. Colonne de droite (Dénominations) : Aligné à droite
    table.add_column("Dénominations", style="cyan", justify="right")
    
    # Inverser la table pour itérer par dénomination
    denominations_map = {v: k for k, v in table_data.items()}
    
    for denomination in sorted(denominations_map.keys()):
        nombre = denominations_map[denomination]
        # L'ordre d'ajout des lignes DOIT suivre l'ordre des colonnes : (Nombre, Dénomination)
        table.add_row(str(nombre), str(denomination))
        
    console.print(table)
    print("\n" + "="*50 + "\n")


def calculer_multiplication(base: int, table: Dict[int, int], nombre1: int, nombre2: int):
    """
    Retrouve les dénominations et effectue l'opération selon le principe
    de l'addition des dénominations, en respectant l'ordre d'affichage.
    """
    
    denomination1 = table.get(nombre1)
    denomination2 = table.get(nombre2)
    
    if denomination1 is None or denomination2 is None:
        console.print(f"[bold red]Erreur :[/bold red] L'un des nombres ({nombre1} ou {nombre2}) n'est pas dans la table générée.", style="red")
        return

    # --- Étape 1 : Retrouver les lignes ---
    console.print(f"[bold green]Nombres trouvés dans la table :[/bold green]")
    console.print(f"  - Le Nombre [bold magenta]{nombre1}[/bold magenta] a la Dénomination [bold cyan]{denomination1}[/bold cyan] ($ = {base}^{denomination1}$)")
    console.print(f"  - Le Nombre [bold magenta]{nombre2}[/bold magenta] a la Dénomination [bold cyan]{denomination2}[/bold cyan] ($ = {base}^{denomination2}$)")
    
    print("\n--- Démonstration de la Loi des Dénominations ---\n")
    
    # --- Étape 2 : Affichage de la Multiplication (Opération principale) ---
    resultat_multiplication = nombre1 * nombre2
    console.print(
        f"**1. Multiplication des Nombres (Opération à effectuer) :**"
    )
    console.print(
        f"  [bold magenta]{nombre1}[/bold magenta] x [bold magenta]{nombre2}[/bold magenta] = [bold red]{resultat_multiplication}[/bold red]", style="white"
    )
    
    # --- Étape 3 : Affichage de l'Addition des Dénominations (Méthode de calcul) ---
    nouvelle_denomination = denomination1 + denomination2
    console.print(
        f"\n**2. Addition des Dénominations (Méthode utilisée) :**"
    )
    console.print(
        f"  [bold cyan]{denomination1}[/bold cyan] + [bold cyan]{denomination2}[/bold cyan] = [bold cyan]{nouvelle_denomination}[/bold cyan]", style="white"
    )
    
    # --- Étape 4 : Affichage du Résultat avec Exposant ---
    
    denominations_map = {v: k for k, v in table.items()}
    resultat_nombre = denominations_map.get(nouvelle_denomination)
    
    console.print(
        f"\n**3. Résultat (Nombre avec sa Dénomination) :**"
    )
    
    if resultat_nombre is None:
        console.print(f"[bold red]  Le résultat est hors de la table.[/bold red] La multiplication donne [bold red]{resultat_multiplication}[/bold red], ce qui correspond à $Base^{nouvelle_denomination}$ ($ {base}^{nouvelle_denomination}$).")
    else:
        console.print(
            f"  Le résultat de la multiplication est [bold magenta]{resultat_nombre}[/bold magenta]."
        )
        console.print(
            f"  Sa Dénomination est [bold cyan]{nouvelle_denomination}[/bold cyan]."
        )
        console.print(
            f"  Écriture selon le principe : $\text{{{resultat_nombre}}}^{{{nouvelle_denomination}}}$ (moderne : ${base}^{{{nouvelle_denomination}}}$)"
        )


# --- Fonction Principale ---
def main():
    """Fonction principale pour exécuter le programme avec configuration utilisateur."""
    
    console.print(f"[bold]Configuration de la Table des Nombres Proporcionals[/bold]", style="white on blue")
    
    try:
        # Configuration par l'utilisateur
        base_input = console.input("Entrez la [bold yellow]Base[/bold yellow] de la suite (ex: 2 pour la suite originale, 3 pour 1, 3, 9, ...): ")
        max_denom_input = console.input("Entrez le [bold yellow]Nombre d'itérations[/bold yellow] max (la plus haute Dénomination, ex: 10): ")
        
        BASE = int(base_input.strip())
        MAX_DENOMINATION = int(max_denom_input.strip())
        
        if BASE < 2 or MAX_DENOMINATION < 1:
            raise ValueError("La Base doit être >= 2 et le Nombre d'itérations >= 1.")

        console.print(f"\n[bold]Génération de la Table (Base {BASE}, Dénomination max {MAX_DENOMINATION})[/bold]\n")
        
        # Génération et affichage de la table
        table_nombres_denominations = generer_table_proportional(BASE, MAX_DENOMINATION)
        afficher_table(BASE, table_nombres_denominations)
        
        # --- Entrée des Nombres à Multiplier ---
        n1_input = console.input("Entrez le [bold magenta]premier nombre[/bold magenta] (choisissez parmi les Nombres ci-dessus) : ")
        n2_input = console.input("Entrez le [bold magenta]deuxième nombre[/bold magenta] : ")
        
        nombre1 = int(n1_input.strip())
        nombre2 = int(n2_input.strip())
        
        print("\n" + "="*50 + "\n")
        
        # Lancement du calcul
        calculer_multiplication(BASE, table_nombres_denominations, nombre1, nombre2)

    except ValueError as ve:
        console.print(f"[bold red]Erreur de saisie :[/bold red] Veuillez entrer des nombres entiers valides. {ve}", style="red")
    except Exception as e:
        console.print(f"[bold red]Une erreur inattendue est survenue :[/bold red] {e}", style="red")

if __name__ == "__main__":
    main()
