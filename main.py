"""
Module pour vérifier si une chaîne de caractères est un palindrome.
"""
import unicodedata

#### Fonction secondaire


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

    # Convertir en minuscules, enlever les accents et ne garder que les caractères alphanumériques
    p = ''.join(c.lower() for c in normalized if c.isalnum() and not unicodedata.combining(c))

    print(p)
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
