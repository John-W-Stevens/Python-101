
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
