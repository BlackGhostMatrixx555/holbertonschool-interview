#!/usr/bin/python3
"""
Module to validate UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    number_of_bytes = 0

    for num in data:
        # On ne garde que les 8 bits de poids faible (1 octet)
        byte = num & 0xFF

        if number_of_bytes == 0:
            # Détermination de la taille du caractère UTF-8
            if (byte >> 7) == 0b0:
                # Caractère sur 1 octet (0xxxxxxx)
                continue
            elif (byte >> 5) == 0b110:
                # Caractère sur 2 octets (110xxxxx), attend 1 octet de suite
                number_of_bytes = 1
            elif (byte >> 4) == 0b1110:
                # Caractère sur 3 octets (1110xxxx), attend 2 octets de suite
                number_of_bytes = 2
            elif (byte >> 3) == 0b11110:
                # Caractère sur 4 octets (11110xxx), attend 3 octets de suite
                number_of_bytes = 3
            else:
                # Séquence de départ invalide (ex: commence par 10xxxxxx ou > 4)
                return False
        else:
            # Vérification de l'octet de continuation (doit commencer par 10)
            if (byte >> 6) != 0b10:
                return False
            number_of_bytes -= 1

    # Si tous les caractères commencés ont bien reçu leurs octets de suite
    return number_of_bytes == 0
