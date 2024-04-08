def rechercher(table_de_hachage, entier):
    dernier_chiffre = abs(entier) % 10
    if entier in table_de_hachage[dernier_chiffre]:
        return True
    else:
        return False


def ajouter(table_de_hachage, entier):
    if not rechercher(table_de_hachage, entier):
        dernier_chiffre = abs(entier) % 10
        table_de_hachage[dernier_chiffre].append(entier)
        table_de_hachage[dernier_chiffre].sort()


def supprimer(table_de_hachage, entier):
    if rechercher(table_de_hachage, entier):
        dernier_chiffre = abs(entier) % 10
        index = table_de_hachage[dernier_chiffre].index(entier)
        table_de_hachage[dernier_chiffre][index] = table_de_hachage[dernier_chiffre][-1]
        table_de_hachage[dernier_chiffre].pop()
        table_de_hachage[dernier_chiffre].sort()


def hachage(str):
    nombre = 0
    i = 0
    while i < len(str):
        nombre += ord(str[i])
        i += 1
    return nombre

