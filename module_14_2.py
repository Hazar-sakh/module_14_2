import sqlite3

con = sqlite3.connect('not_telegram.db')
curs = con.cursor()

curs.execute(
    '''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )
    '''
)
con.commit()

for i in range(1, 11):
    a = i * 10
    curs.execute(
        '''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, ?)
        ''',
        (f'User{i}', f'example{i}@gmail.com', f'{a}', f'{1000}',)
    )
    con.commit()


curs.execute(
    '''
    UPDATE Users SET balance = 500 WHERE id % 2 != 0
    '''
)
con.commit()

l = []
c = 0
for i in range(1, 11):
    if c == 0:
        l.append(i)
    c += 1
    if c == 3:
        c = 0
        continue
    for j in l:
        curs.execute(
            '''
            DELETE FROM Users
            WHERE id = ?
            ''',
            (j,)
        )
        con.commit()

curs.execute(
    '''
    SELECT * FROM Users
    WHERE age <> ?
    ''',
    (60,)
)
sel = curs.fetchall()
con.commit()

# for i in sel:
#     print(f'Имя: {i[1]}| Почта: {i[2]}| Возраст: {i[3]}| Баланс: {i[4]}')

curs.execute(
    '''
    DELETE FROM Users
    WHERE id = 6
    '''
)
con.commit()

curs.execute(
    '''
    SELECT COUNT(id) FROM Users
    '''
)
count = curs.fetchone()[0]
con.commit()

curs.execute(
    '''
    SELECT SUM(balance) FROM Users
    '''
)
bal_s = curs.fetchone()[0]
con.commit()

print(bal_s/count)

con.close()
