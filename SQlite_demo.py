import sqlite3
import pandas as pd

try:
    # Kết nối tới DB và tạo cursor
    sqliteConnection = sqlite3.connect('databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Viết query và thực thi
    query = "SELECT * FROM InvoiceLine LIMIT 5;"
    cursor.execute(query)

    # Lấy dữ liệu và đưa ra DataFrame
    df = pd.DataFrame(cursor.fetchall())
    print(df)

    # Đóng cursor
    cursor.close()

except sqlite3.Error as error:
    print("Error occurred - ", error)

finally:
    # Đóng kết nối DB dù thành công hay thất bại
    if sqliteConnection:
        sqliteConnection.close()
        print("SQLite Connection closed")
