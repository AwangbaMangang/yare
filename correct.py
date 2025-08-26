# correct.py

# A large dictionary of incorrect-to-correct Meitei Mayek word mappings.
# This should be populated with your specific list of 50,000+ words.
# The keys are the incorrect spellings, and the values are the correct spellings.
INCORRECT_TO_CORRECT_MAP = {
    'ꯃꯩꯇꯩ': 'ꯃꯤꯇꯩ',
    'ꯍꯥꯏ': 'ꯍꯥꯏꯕ',
    'ꯆꯠ': 'ꯆꯠꯄ',
    # ... add your 50,000+ words here
}

def replace_incorrect_words(text):
    """
    Replaces known incorrect Meitei Mayek words with their correct forms.
    This function is optimized for a large number of replacements.
    """
    # Using a list comprehension for a slightly more performant way to replace words
    # than iterating over a dictionary and calling .replace() repeatedly.
    # This splits the text into words and then replaces each word if it's in the map.
    words = text.split()
    corrected_words = [INCORRECT_TO_CORRECT_MAP.get(word, word) for word in words]
    return ' '.join(corrected_words)
