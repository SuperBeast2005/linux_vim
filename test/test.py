import pandas as pd
import sqlite3

csv_data  = pd.read_csv('/linux_vim/test.csv')
df = pd.DataFrame(csv_data)

def create_db():
    con = sqlite3.connect('/linux_vim/data.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS male(id, surname, name, email, ip)')
    cur.execute('CREATE TABLE IF NOT EXISTS female(id, surname, name, email, ip)')
    con.commit()
    con.close()
    
def insert_male():
    con = sqlite3.connect('/linux_vim/data.db')
    cur = con.cursor()
    data = df[df.gender == 'Male']
    cur.execute(f'INSERT INTO male  VALUES (?,?,?,?)', data)
    print(data)
    con.commit()
    con.close() 

if __name__ == "__main__":
    print(csv_data)
    print(df[df.gender  == 'Male'])
    create_db()
    insert_male()

