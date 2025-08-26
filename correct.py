import json

def load_dictionary(file_path):
    """
    Loads the word replacement dictionary from a JSON file.
    
    Args:
        file_path (str): The path to the JSON file.
        
    Returns:
        dict: A dictionary containing the incorrect-to-correct word mappings.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return {}

def replace_incorrect_words(text, word_map):
    """
    Replaces a set of known incorrect Meitei Mayek words with their correct forms.
    
    Args:
        text (str): The input text containing Meitei Mayek script.
        word_map (dict): The dictionary of incorrect-to-correct word mappings.
        
    Returns:
        str: The text with all known incorrect words replaced.
    """
    words = text.split()
    corrected_words = [word_map.get(word, word) for word in words]
    return ' '.join(corrected_words)

def main():
    # --- Load the dictionary from the JSON file ---
    incorrect_to_correct_map = load_dictionary('dictionary.json')
    
    if not incorrect_to_correct_map:
        print("Could not load dictionary. Exiting.")
        return

    # --- Example Usage ---
    sample_text = "ꯃꯤꯇꯩ ꯂꯣꯟ ꯐꯖꯩ"
    
    print("Original Text:")
    print(sample_text)
    
    corrected_text = replace_incorrect_words(sample_text, incorrect_to_correct_map)
    
    print("\nCorrected Text:")
    print(corrected_text)

if __name__ == "__main__":
    main()

