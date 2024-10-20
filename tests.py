from main import BooksCollector
import pytest


@pytest.fixture
def book_list():
    book_list = [['Вино из одуванчиков', 'Фантастика'],
                 ['Кладбище домашних животных', 'Ужасы'],
                 ['Империя и основание', 'Фантастика'],
                 ['Петровка 38', 'Детективы'],
                 ['Ну погоди!', 'Мультфильмы'],
                 ['Кладбище домашних животных', 'Ужасы'],
                 ['Гонки по вертикали', 'Детективы'],
                 ['Конец вечности', 'Фантастика'],
                 ['Джентльмены удачи', 'Комедии'],
                 ['Томиноккеры', 'Ужасы']
                 ]
    return book_list

@pytest.fixture
def collector(book_list):
    collector = BooksCollector()
    for book_name, book_genre in book_list:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
    return collector



# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    @pytest.mark.skip
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
     #   assert len(collector.get_books_rating()) == 2
        assert len(collector.get_books_genre()) == 2
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

        # Проверка добавления новой книги в словарь без указания жанра
    def test_add_new_book_add_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Вино из одуванчиков')
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 1 and 'Вино из одуванчиков' in books_genre

    # Проверка установки жанра книги для каждого жанра
    @pytest.mark.parametrize('book_name, book_genre', [['Вино из одуванчиков', 'Фантастика'],
                                                       ['Кладбище домашних животных', 'Ужасы'],
                                                       ['Петровка 38', 'Детективы'],
                                                       ['Ну погоди', 'Мультфильмы'],
                                                       ['Джентльмены удачи', 'Комедии']
                                                       ])
    def test_set_book_genre_set_genre(self, book_name, book_genre):
        collector = BooksCollector()
        book_name = 'Вино из одуванчиков'
        book_genre = 'Фантастика'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
        books_genre = collector.get_books_genre()
        assert books_genre.get(book_name) == book_genre

    # Получение жанра книги по имени книги
    def test_get_book_genre_return_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Вино из одуванчиков')
        collector.set_book_genre('Вино из одуванчиков', 'Фантастика')
        assert collector.get_book_genre('Вино из одуванчиков') == 'Фантастика'

        # Получение списка книг с определенными жанрами - положительный тест
    @pytest.mark.parametrize('book_genre, book_num', [['Фантастика', 3], ['Ужасы', 2],
                                                      ['Детективы', 2],
                                                      ['Мультфильмы', 1],
                                                      ['Комедии', 1]
                                                      ])
    def test_get_books_with_specific_genre_return_books_list_for_genre(self, collector, book_genre, book_num):
        assert len(collector.get_books_with_specific_genre(book_genre)) == book_num

    # Получение списка книг с определенными жанрами - отрицательный тест
    def test_get_books_with_specific_genre_error_for_non_existent_genre(self, collector):
        assert len(collector.get_books_with_specific_genre('Романы')) == 0

    # Получаем словарь book_genre
    def test_get_books_genre_get_all_books_dict(self, collector, book_list):
        assert collector.get_books_genre() == dict(book_list)

    # Книги, подходящие детям
    def test_get_books_for_children_return_list_books_for_children(self, collector):
        assert collector.get_books_for_children() == ['Вино из одуванчиков', 'Империя и основание', 'Ну погоди!',
                                                          'Конец вечности', 'Джентльмены удачи']

    # Добавляем книги в избранное
    def test_add_book_in_favorites_add_book_to_favorites(self, collector):
        collector.add_book_in_favorites('Вино из одуванчиков')
        collector.add_book_in_favorites('Томиноккеры')
        collector.add_book_in_favorites('Петровка 38')
        collector.add_book_in_favorites('Джентльмены удачи')
        collector.add_book_in_favorites('Ну погоди!')
        assert collector.get_list_of_favorites_books() == ['Вино из одуванчиков', 'Томиноккеры', 'Петровка 38',
                                                           'Джентльмены удачи', 'Ну погоди!']

    # Удаляем книгу из избранного
    def test_delete_book_from_favorites_book_removes_from_favorites(self, collector):
        collector.add_book_in_favorites('Вино из одуванчиков')
        collector.add_book_in_favorites('Томиноккеры')
        collector.delete_book_from_favorites('Вино из одуванчиков')
        assert collector.get_list_of_favorites_books() == ['Томиноккеры']

    #  Получаем список избранных книг
    def test_get_list_of_favorites_books_return_list_with_result(self):
        collector = BooksCollector()
        collector.add_new_book('Ставка больше, чем жизнь')
        collector.set_book_genre('Ставка больше, чем жизнь', 'Детективы')
        collector.add_book_in_favorites('Ставка больше, чем жизнь')
        assert collector.get_list_of_favorites_books() == ['Ставка больше, чем жизнь']


