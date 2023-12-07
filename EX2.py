library = {
    "БСтругацкие": ["Пикник на обочине", "Трудно быть богом"],
    "Чехов": ["Вишневый сад"],
    "Зан": ["Траун"]
}

if input("Хочешь добавить автора и его книгу?[y/n] ") == 'y':
    print("Введи автора и книгу через пробел")
    while True:
        ip = input()
        if ip == "exit":
            break
        if ip.count(" ") < 1:
            print("!Введи автора и книгу через пробел!")
        else:
            author = ip[:ip.find(" ")]
            book = ip[ip.find(" ")+1:]
            if author in library.keys():
                library[author] += [book]
            else:
                library[author] = [book]
            print(f"{author}, {book}  добавлены. Для выхода введите exit.")

while True:
    author = input("\n Введите автора или введите exit, для выхода: ")
    if author == "exit":
        break
    try:
        print(f"Книги {author} в скрежали\n")
        for book in library[author]:
            print(book)
    except:
        print("I couldn't find this author")