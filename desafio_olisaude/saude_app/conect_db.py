import psycopg2
from contextlib import contextmanager


@contextmanager
def conect_db():
    """
        Connect to the Database
    """
    conexao = psycopg2.connect(
        host='localhost',
        database='oli_saudeDB',
        user='postgres',
        password='Din@199419972005'
    )

    try:
        yield conexao
    finally:
        conexao.close()


def select_problems():
    with conect_db() as con:  # To call the function connect_db to open the connection with database
        with con.cursor() as cursor:  # To start the cursor
            score = f'((1 / (1 + exp(-(-2.8 + sum(degree_problem) )))) * 100)'
            sql = f'select code_costumer_id, round({score}, 2) ' \
                  f'as score from saude_app_problemhearth group by ' \
                  f'code_costumer_id order by score desc'
            cursor.execute(sql)  # To get all products of database
            data_score = cursor.fetchall()  # To calculate how much products exist in table of database
            return data_score


if __name__ == '__main__':
    for d in select_problems():
        print(f'Code Costumer: {d[0]}')
        print(f'Score: {d[1]}\n')
