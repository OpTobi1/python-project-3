class BookAnalyzer:
    def __init__(self, authors_books):
        self.authors_books = authors_books

    def analyze_book(self, text: str) -> dict:
        # כתיבת לוגיקה לניתוח ספר כאן
        pass

    def analyze_authors(self) -> dict:
        # לניתוח ספרי סופרים באמצעות analyze_book
        pass

    def most_frequent_word(self, analysis: dict) -> tuple:
        # מציאת המילה הנפוצה ביותר בניתוח
        pass

    def compare_authors(self, author1: str, author2: str) -> str:
        # השוואת שני סופרים
        pass

    def export_analysis(self, filename: str) -> None:
        # ייצוא ניתוח לקובץ
        pass



analyzer = BookAnalyzer(authors_books)
analysis = analyzer.analyze_authors()
print(analysis)
analyzer.export_analysis("analysis.csv")
