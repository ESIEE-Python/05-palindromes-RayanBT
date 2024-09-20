"""
Module pour vérifier si une chaîne de caractères est un palindrome.
"""

#### Fonction secondaire


def remove_accents(text):
    """
    Supprime les accents d'une chaîne de caractères en utilisant la méthode translate().

    Args:
        text (str): La chaîne de caractères à traiter.

    Returns:
        str: La chaîne sans accents.
    """
    # Dictionnaire de correspondance pour enlever les accents courants
    accents_translation_table = str.maketrans(
        "áàâäãåéèêëíìîïñóòôöõúùûüýÿç",
        "aaaaaaeeeeiiiinooooouuuuyyc"
    )

    # Appliquer la table de correspondance pour supprimer les accents
    return text.translate(accents_translation_table)


def ispalindrome(p):
    """
    Détermine si une chaîne de caractères est un palindrome.

    Args:
        p (str): La chaîne de caractères à vérifier.

    Returns:
        bool: True si la chaîne est un palindrome, False sinon.
    """
    # Normaliser la chaîne en utilisant 'NFD' pour séparer les accents
    normalized = unicodedata.normalize('NFD', p)

    # Supprimer les accents avec la fonction remove_accents()
    p = remove_accents(normalized)

    # Convertir en minuscules et ne garder que les caractères alphanumériques
    p = ''.join(c.lower() for c in p if c.isalnum())

    print(p)
    # Vérifier si la chaîne est un palindrome
    for i in range(len(p)//2):
        if p[i] != p[-i-1]:
            return False
    return True


#### Fonction principale


def main():
    """
    Fonction principale.
    """

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
