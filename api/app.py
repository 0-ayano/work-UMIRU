import pymysql.cursors
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI

app = FastAPI()

# CORSを回避するために追加（今回の肝）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/current/{place}/{tank}")
def get_current_information(place: str, tank: str):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='umiru',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {place}_{tank} ORDER BY dt DESC LIMIT 1;"
            cursor.execute(sql)
            result = cursor.fetchall()

        if len(result) == 0:
            return {
                "msg": "--Miss--",
            }
        else:
            return {
                "msg": "--Success--",
                "datetime": result[0]["dt"],
                "temp": result[0]["temp"],
                "shibu": result[0]["shibu"],
                "condact": result[0]["condact"],
                "do_per": result[0]["do_per"],
                "do_mg": result[0]["do_mg"],
            }
    finally:
        connection.close()
    
@app.get("/graph/{place}/{tank}/{date1}/{date2}")
def get_graph_information(place: str, tank: str, date1: str, date2: str):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='umiru',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {place}_{tank} WHERE DATE(dt) BETWEEN '{date1}' AND '{date2}';"
            cursor.execute(sql)
            result = cursor.fetchall()

        if len(result) == 0:
            return {
                "msg": "--Miss--",
            }
        else:
            return {
                "msg": "--Success--",
                "data": result,
            }
    finally:
        connection.close()

@app.get("/table")
def get_table_information():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='umiru',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            sql = f"show tables;"
            cursor.execute(sql)
            result = cursor.fetchall()

        if len(result) == 0:
            return {
                "msg": "--Miss--",
            }
        else:
            return {
                "msg": "--Success--",
                "data": result,
            }
    finally:
        connection.close()

@app.get("/first_graph/{place}/{tank}")
def get_table_information(place, tank):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='umiru',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {place}_{tank} ORDER BY dt DESC LIMIT 50;"
            cursor.execute(sql)
            result = cursor.fetchall()

        if len(result) == 0:
            return {
                "msg": "--Miss--",
            }
        else:
            return {
                "msg": "--Success--",
                "data": result,
            }
    finally:
        connection.close()