import re
from collections import Counter

def most_common_word(text):
    # Remove punctuation and convert text to lowercaseā
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Create a dictionary with word frequencies
    word_freq = {word: text.count(word) for word in re.findall(r'\w+', text)}

    # Return the most common word
    return max(word_freq, key=word_freq.get)

# Example usage
text = "Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python emphasizes code readability with its notable use of significant whitespace."

print("Most common word in the text:", most_common_word(text))