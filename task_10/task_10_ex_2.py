"""Implement a function most_common_words(file_path: str, top_words: int) -> list
which returns most common words in the file.
<file_path> - system path to the text file
<top_words> - number of most common words to be returned
Example:
print(most_common_words(file_path, 3))
> NOTE: Remember about dots, commas, capital letters etc.
"""
import re


def most_common_words(text: str, top_words=3):
    with open(text, 'r', encoding='utf-8') as f:
        txt = f.read()
        words_list = re.findall(r'[a-zA-Z]+', txt)
        counts = {}
        for word in words_list:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1
    list_of_words = [k for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True)]
    return list_of_words[0:top_words]


if __name__ == '__main__':
    filename = 'C:/Users/illic/data/lorem_ipsum.txt'
    print(f'\nThe list with most common word(s) in {filename}: {most_common_words(filename)}')
