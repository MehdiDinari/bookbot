def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_chars(char_count):
    # Créer une liste de dictionnaires
    sorted_chars = []
    for char, count in char_count.items():
        sorted_chars.append({"char": char, "num": count})
    
    # Trier la liste par nombre décroissant
    sorted_chars.sort(reverse=True, key=lambda x: x["num"])
    
    return sorted_chars
