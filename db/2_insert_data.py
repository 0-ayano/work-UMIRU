import pymysql.cursors
import csv
import tkinter as tk
import tkinter.filedialog
import time

def selectFile():
    root = tk.Tk()
    root.withdraw()
    types = [ ("csv file", "*.csv") ]
    target_files = tkinter.filedialog.askopenfilenames( filetypes = types, title = "open files" )
    return target_files[0]


database_name = "umiru"
data_box = []


connection = pymysql.connect(host='localhost',
                            user='root',
                            password='root',
                            database=database_name,
                            cursorclass=pymysql.cursors.DictCursor)

with open(selectFile(), 'r') as csv_file:
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(f)
    
    for row in f:
        for i in range( (len(row)-1) // 14 ):
            num = i * 14
            box = [row[0], row[num+1], row[num+2], row[num+5], row[num+6], row[num+7], row[num+13], row[num+14]]
            data_box.append(box)

with connection:
    for data in data_box:
        with connection.cursor() as cursor:
            table_name = "{0}_{1}".format(data[2].replace(' ', ''), data[1].replace(' ', ''))
            query_table_check = f"SHOW TABLES LIKE '{table_name}';"
            result_check = cursor.execute(query_table_check)

            if result_check:
                # print("テーブルは存在しました。")
                pass

       
            else:
                query_table_create = f"CREATE TABLE {table_name} (dt datetime, temp float, shibu float, condact float, do_per float, do_mg float)"
                result_create = cursor.execute(query_table_create)
                if result_create == 0:
                    # print("テーブル作成に成功しました。")
                    pass
                else:
                    print("テーブル作成に失敗しました。")


            query_table_insert = f"insert into {table_name} values('{data[0]}', {data[3]}, {data[4]}, {data[5]}, {data[6]}, {data[7]});"
            result_insert = cursor.execute(query_table_insert)
            if result_insert == 1:
                # print("データの挿入に成功しました。")
                pass
            else:
                print("データの挿入に失敗しました。")
            time.sleep(0.0001)
        connection.commit()