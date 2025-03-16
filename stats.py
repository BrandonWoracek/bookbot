#Function to count the words in the book text
def get_book_words(book):
    words = []
    count = 0
    for text in book.split():
        words.append(text)
    for word in words:
        if word:
            count += 1
    return count

#Count of each character in the book
def get_book_characters(book):
    chars = {}
    for c in book:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

#Sort characters from greatest to least in a list of dictionaries
def sorted_book_characters(book):
    characters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'æ', 'â', 'ê', 'ë', 'ô']
    reduced_list = []
    get_dict = get_book_characters(book)
    for char, count in get_dict.items():
        if char in characters_list:
            reduced_list.append({'character': char, 'count': count})
    reduced_list.sort(key=lambda x: x['count'], reverse=True)
    for item in reduced_list:
        print(f"{item['character']}: {item['count']}")