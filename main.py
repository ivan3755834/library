file_name = "hello.txt"

def load_book():
    books = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip():
                    num, nume, date = line.strip().split('')
                    books.append({'num': num, 'name': name, 'date':date})
    except FileNotFoundError:
                    pass
    return books
def save_books(books):
    with open(file_name, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(f"{book['num']}{book['name']}{book['date']}\n")

def add_book():
    num = input("Введите номер книги: ")
    name = input("Введите название книги: ")
    date = input("Введите дату издания книги(дд.мм.гггг) книги: ")

    books = load_book()
    books.append({'num': num, 'name': name, 'date':date})
    save_books(books)
    print("Книга добавлена")
def delete_book():
    search = input("Удалите по номеру(1) или по названию(2): ")

    if search == '1':
        num = input("Введите номер книги для удаления: ")
        books = [book for book in books if book['num'] != num]

    else:
        name = input("Введите название книги для удаления: ")
        books = [book for book in books if book['name'] != name]

    save_books(books)
    print('Книга удалена')

def clear_books():
    confirm = input("Вы уверены что хотите отчистить весь список?(да\нет): ")
    if confirm.lower() == 'да':
        save_books([])
        print('Список очищен')
def search_book():
    search_type = input("Поиск по номеру(1), по названию(2), по дате издания(3): ")
    books = load_books()
    found = []

    if search_type == '1':
        num = input("Поиск по номеру: ")
        found = [book for book in books if book['num'] != num]
    elif search_type == '2':
        name = input("Поиск по названию: ")
        found = [book for book in books if book['name'].lower() == name.lower()]
    else:
        input("Поиск по дате: ")
        found = [book for book in books if book['date'] == date]

    if found:
        print("Найденные книги")
        for book in found:
            print(f"{book['num']} {book['name']} {book['date']} ")

    else:
        print('Книги не найдены')


