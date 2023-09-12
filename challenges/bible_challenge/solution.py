
def get_books_of_the_bible_from_data(file_name):

    books_of_the_bible = []
    with open("./challenges/bible_challenge/{}".format(file_name), "r") as file:
        for line in file.readlines():

            starting_indecies = []
            ending_indecies = []

            for i in range(len(line)):
                if line[i] == "[":
                    starting_indecies.append(i)
                elif line[i] == "]":
                    ending_indecies.append(i)

            categories = line[starting_indecies[0]:ending_indecies[0] + 1].removeprefix("[").removesuffix("]").split(",")
            authors = line[starting_indecies[1]:ending_indecies[1] + 1].removeprefix("[").removesuffix("]").split(",")

            for j in range(len(categories)):
                categories[j] = categories[j].strip()

            for k in range(len(authors)):
                authors[k] = authors[k].strip()

            split_content = line.split(',')

            name = split_content[0].strip()
            chapters = split_content[1].strip()
            verses = split_content[2].strip()

            book = [name, int(chapters), int(verses), categories, authors]

            book = {
                'name': name,
                'chapters': chapters,
                'verses': verses,
                'categories': categories,
                'authors': authors
            }

            books_of_the_bible.append(book)
        return books_of_the_bible
    
books = get_books_of_the_bible_from_data('data.txt')

question = [
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

def how_many_chapters_in_the_bible(books):
    return sum([book['chapters'] for book in books])
def how_many_verses_in_the_bible(books):
    return sum([book['verses'] for book in books])

def answer_question(question):
    return ''

def program_loop():
    running = True
    while running:
        response = input("What would you like to do now? You can ask me a question or quit. Choose an option below: \n a. see question \n b. quit ")
        if response == 'quit':
            running = False
        elif response == 'see question':
            question = input("Select a question below, or type 'back'")
            if question == 'back':
                continue
            else:
                answer = answer_question(question)

    print("Exiting program....")

program_loop()