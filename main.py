file_name = "books.txt"

def load_books():
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return [line.strip().split(';') for line in file if line.strip()]
    except FileNotFoundError:
        return []

def save_books(books):
    with open(file_name, 'w', encoding='utf-8') as file:
        for book in books:
            file.write(';'.join(book) + '\n')

def add_book():
    num = input("Номер книги: ")
    name = input("Название книги: ")
    date = input("Дата (дд.мм.гггг): ")
    
    books = load_books()
    books.append([num, name, date])
    save_books(books)
    print("Книга добавлена!")

def delete_book():
    books = load_books()
    search = input("Удалить по номеру(1) или названию(2): ")
    
    if search == '1':
        num = input("Номер книги: ")
        books = [book for book in books if book[0] != num]
    else:
        name = input("Название книги: ")
        books = [book for book in books if book[1].lower() != name.lower()]
    
    save_books(books)
    print("Книга удалена!")

def clear_books():
    if input("Очистить весь список? (да/нет): ").lower() == 'да':
        save_books([])
        print("Список очищен!")

def search_book():
    books = load_books()
    search_type = input("Поиск по номеру(1), названию(2) или дате(3): ")
    
    if search_type == '1':
        num = input("Номер: ")
        found = [book for book in books if book[0] == num]
    elif search_type == '2':
        name = input("Название: ")
        found = [book for book in books if name.lower() in book[1].lower()]
    else:
        date = input("Дата: ")
        found = [book for book in books if book[2] == date]
    
    if found:
        print("Найдены книги:")
        for book in found:
            print(f"№{book[0]}: {book[1]} ({book[2]})")
    else:
        print("Книги не найдены")

def show_books():
    books = load_books()
    if books:
        print("Список книг:")
        for book in books:
            print(f"№{book[0]}: {book[1]} ({book[2]})")
    else:
        print("Список пуст")

def menu():
    print("\n1. Добавить книгу")
    print("2. Удалить книгу")
    print("3. Очистить список")
    print("4. Найти книгу")
    print("5. Показать все книги")
    print("6. Выйти")

def main():
    while True:
        menu()
        choice = input("Выберите действие: ")
        
        if choice == "1": add_book()
        elif choice == "2": delete_book()
        elif choice == "3": clear_books()
        elif choice == "4": search_book()
        elif choice == "5": show_books()
        elif choice == "6": break
        else: print("Неверный выбор!")

if name == "main":
    main()
