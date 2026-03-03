#Assignment: Homework 3 - Part 2 Author: David Haim Liav Lugasi, ID: 213007271

import csv
from part1_213007271 import linking_words,authors_books, analyze_book as part1_analyze_book

class BookAnalyzer:
    def __init__(self, authors_books):
        self.authors_books = authors_books

    def analyze_book(self, text: str) -> dict:
        return part1_analyze_book(text)

    def analyze_authors(self) -> dict:
        authors_analysis = {}
        for author, text in self.authors_books.items():
            authors_analysis[author] = self.analyze_book(text)
        return authors_analysis

    def most_frequent_word(self, analysis: dict) -> tuple:
        if "most_common_words" in analysis:
            return analysis["most_common_words"][0]
        return None

    def compare_authors(self, author1: str, author2: str) -> str:
        book1_analysis = self.analyze_book(self.authors_books[author1])
        book2_analysis = self.analyze_book(self.authors_books[author2])

        if book1_analysis["numWords"] > book2_analysis["numWords"]:
            return author1
        elif book2_analysis["numWords"] > book1_analysis["numWords"]:
            return author2
        else:
            if book1_analysis["numChars"] > book2_analysis["numChars"]:
                return author1
            elif book2_analysis["numChars"] > book1_analysis["numChars"]:
                return author2
            else:
                return "Draw"

    def export_analysis(self, filename: str) -> None:
        authors_analysis = self.analyze_authors()
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Author", "Num Words", "Num Chars", "Num Sentences", "Most Common Words"])
            for author, analysis in authors_analysis.items():
                writer.writerow([
                    author,
                    analysis["numWords"],
                    analysis["numChars"],
                    analysis["sentencesCount"],
                    ", ".join(analysis["commonFive"])
                ])


analyzer = BookAnalyzer(authors_books)

authors_analysis = analyzer.analyze_authors()
print("Authors Analysis:")
for author, data in authors_analysis.items():
    print(f"{author}: {data}")

author1 = "George Orwell"
author2 = "J.K. Rowling"
winner = analyzer.compare_authors(author1, author2)
print(f"\nComparison: The author with the longer book is {winner}.")


analyzer.export_analysis("authors_analysis.csv")
print("\nAnalysis exported to 'authors_analysis.csv'.")
