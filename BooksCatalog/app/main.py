from sqlite3 import *


def data_adapter(data: list):
    for row in data:
        for item in row:
            print(f'{item}', end='  ')
        print()


if __name__ == '__main__':

    connection = connect('Books.db')
    cursor = connection.cursor()

    data = cursor.execute("""
        select
            t2.book_id as 'ID',
            t1.author_name as 'Автор',
            t2.book_name as 'Книга',
            t2.genre as 'Жанр'
        from
            Authors t1 inner join Books t2
        on
            t1.author_id = t2.author_id;
    """).fetchall()
    data_adapter(data)