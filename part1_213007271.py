# Assignment: Homework 3 - Part 1 , Author: David Haim Liav Lugasi , ID: 213007271

from dict import linking_words,books_by_authors,books_by_authors_1,books_by_authors_2,books_by_authors_3,books_by_authors_4,books_by_authors_5,books_by_authors_6

authors_books = {}
list_books_by_authors = [books_by_authors,books_by_authors_1,books_by_authors_2,books_by_authors_3,books_by_authors_4,books_by_authors_5,books_by_authors_6]
for i in list_books_by_authors:
    for author,book in i.items():
        authors_books[author] = book



def analyze_book(text):
    output = {}

    numWords = len(text.split(" "))
    output["numWords"] = numWords

    numChars = len(text)
    output["numChars"] = numChars

    sentencesCount = text.count("?") + text.count("!") + text.count(".")
    output["sentencesCount"] = sentencesCount


    if numWords > 0:
        avgWordLength = numChars / numWords
    else:
        avgWordLength = 0
    output["avgWordLength"] = avgWordLength


    if sentencesCount > 0:
        avgSentenceLength = numWords / sentencesCount
    else:
        avgSentenceLength = 0
    output["avgSentenceLength"] = avgSentenceLength


    commonFive = []
    countingDict = {}
    for word in text.split():
        if word.strip().lower() not in linking_words:
            if word in countingDict:
                countingDict[word] += 1
            else:
                countingDict[word] = 1


    for i in range(5):
        max = 0
        wordMax = ""
        for k,v in countingDict.items():
            if v > max:
                wordMax = k
                max = v
        countingDict.pop(wordMax)
        commonFive.append(wordMax)

    output["commonFive"] = commonFive
    return output




def analyze_authors(authors_books):
    total_words = 0
    total_chars = 0
    authors_analysis = {}

    for author, book in authors_books.items():
        book_analysis = analyze_book(book)


        unique_words = len(set(
            word.strip().lower() for word in book.split()
            if word.strip() not in linking_words and word.strip() != ""
        ))
        book_analysis["uniqueWordCount"] = unique_words


        total_words += book_analysis["numWords"]
        total_chars += book_analysis["numChars"]


        authors_analysis[author] = book_analysis


    avg_words = total_words / len(authors_books)
    avg_chars = total_chars / len(authors_books)


    authors_analysis["averageBookLength"] = {
        "avgWords": avg_words,
        "avgChars": avg_chars
    }

    return authors_analysis




def common_word(books_dict):
    combined_text = ""
    for book in books_dict.values():
        combined_text += book + " "


    word_count = {}
    for word in combined_text.split():
        cleaned_word = word.strip().lower()
        if cleaned_word not in linking_words and cleaned_word:
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1


    most_common_word = ""
    max_count = 0
    for word, count in word_count.items():
        if count > max_count:
            most_common_word = word
            max_count = count

    print(f"The most common word in the dictionary is '{most_common_word}', appearing {max_count} times.")


for i, books_dict in enumerate(list_books_by_authors, 0):
    print(f"\nbooks by authors {i}:")
    common_word(books_dict)




def compare_authors(author1, author2, authors_books):

    analysis1 = analyze_book(authors_books[author1])
    analysis2 = analyze_book(authors_books[author2])

    stats = ["numWords", "numChars", "sentencesCount", "avgWordLength", "avgSentenceLength"]
    score1 = 0
    score2 = 0
    score3 = 0

    for stat in stats:
        if analysis1[stat] > analysis2[stat]:
            score1 += 1
        elif analysis2[stat] > analysis1[stat]:
            score2 += 1
        else:
            score3 += 1


    print(f"Results for {author1} vs {author2}:")
    print(f"{author1} won in {score1} categories.")
    print(f"{author2} won in {score2} categories.")
    print(f"{author1} and {author2} tie in {score3} categories.")


    if score1 > score2:
        print(f"\nThe winner is {author1}!")
    elif score2 > score1:
        print(f"\nThe winner is {author2}!")
    else:
        print("\nIt's a tie!")



