def count_vowels(sentence:str) -> dict:
    """Return list of vowels found in sentence"""
    
    vowels = set('aeiou')
    vowel_count = {}

    for ch in list(sentence):
        if ch in vowels:
            vowel_count.setdefault(ch,0)
            vowel_count[ch] += 1
    
    return vowel_count

def find_common_letters(sentence:str, letters:str='python') -> set:
    """Return set of of characters to both arguments"""
    return set(sentence).intersection(set(letters))