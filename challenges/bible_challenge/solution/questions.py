from functools import reduce

questions = [
    'How many chapters are there in the Bible?',
    'How many verses are there in the Bible?',
    'How many books of the Bible have unknown (human) authors?',
    'How many different known (human) authors are there?',
    'What book of the Bible has the highest average amount of verses per chapter?',
    'What book of the Bible has the average lowest amount of verses per chapter (only consider books with more than 8 chapters)?',
    'How many different categories of Bible books are there?',
    'Which categories are the largest (by verse count)?',
    'Which categories are the smallest (by verse count)?',
    'How many verses and chapters are there in the major prophets?',
    'How many verses and chapters are there in the minor prophets?',
    'What percentage of the Bible did Paul write (based on number of verses Paul wrote out of the whole)?',
    'What percentage of the Bible did Moses write (based on number of verses Moses wrote out of the whole)?',
    'What percentage of the Bible did John write (based on number of verses John wrote out of the whole)?',
]

def get_total_chapters_in_bible(books):
    return sum([book['chapters'] for book in books])

def get_total_verses_in_bible(books):
    return sum([book['verses'] for book in books])

def get_books_with_unknown_human_authors(books):
    return len(list(filter(lambda book: 'Unknown' in book['authors'], books)))

def get_all_authors(books):
    distinct_authors = set()
    for book in books:
        authors = book['authors']
        for author in authors:
            distinct_authors.add(author)
    return distinct_authors

def get_book_with_highest_average_amount_of_verses_per_chapter(books):
    return reduce(lambda book_1, book_2: book_1['verses'] // book_2['chapters'] > book_2['verses'] // book_2['chapters'], books)

def get_book_with_lowest_average_amount_of_verses_per_chapter(books):
    filtered_books = filter(lambda book: book['chapters'] >= 8, books)
    return reduce(lambda book_1, book_2: book_1['verses'] // book_1['chapters'] < book_2['verses'] // book_2['chapters'], filtered_books)

def get_all_categories(books):
    categories = set()
    for book in books:
        for category in book['categories']:
            categories.add(category)
    return categories;

def get_largest_category_by_verse_count(books):

    max_category, max_verses = '', 0

    categories_to_verse_count = {}

    for book in books:
        category = book['category']
        if category in categories_to_verse_count:
            verses = categories_to_verse_count[category] + book['verses']
            categories_to_verse_count.update({category: verses})
        else:
            categories_to_verse_count.update({category: book['verses']})

        if categories_to_verse_count[category] > max_verses:
            max_verses = categories_to_verse_count[category]
            max_category = category
    
    return max_category

def answer_question(question, books):
    if question == questions[0]: return get_total_chapters_in_bible(books)
    if question == questions[1]: return get_total_verses_in_bible(books)
    if question == questions[2]: return get_books_with_unknown_human_authors(books)
    if question == questions[3]: return get_all_authors(books)