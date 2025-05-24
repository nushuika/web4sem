def remove_punctuation(word):
    result = ""
    for char in word:
        if char.isalnum():
            result += char
    return result

def find_max_length(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        cleaned_words = [remove_punctuation(word) for word in words]
        max_length = 0
        max_words = []
        for word in cleaned_words:
            word_length = len(word)
            if word_length > max_length:
                max_length = word_length
                max_words = [word]
            elif word_length == max_length:
                if word not in max_words:
                    max_words.append(word)
    return max_words

if __name__ == "__main__":
    filename = 'example.txt'
    max_length_words = find_max_length(filename)
    for word in max_length_words:
        print(word)
