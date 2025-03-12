import pandas as pd
import sqlite3

csv_data  = pd.read_csv('/linux_vim/test.csv')
df = pd.DataFrame(csv_data)

if __name__ == "__main__":
    print(csv_data)
    print(df['Gender'])
