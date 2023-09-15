from parse_data import get_books_of_the_bible_from_data
from questions import answer_question, questions

books = get_books_of_the_bible_from_data('data.txt')

for question in questions:
    answer = answer_question(question, books)
    print('{} - Answer: {}'.format(question, answer))