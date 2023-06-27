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

@app.get("/10time/{place}/{tank}")
def get_10time_information(place: str, tank: str):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='umiru',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {place}_{tank} WHERE DATE(dt) = CURDATE() AND (HOUR(dt) = 10 AND MINUTE(dt) = 0);"
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

@app.get("/15time/{place}/{tank}")
def get_15time_information(place: str, tank: str):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='umiru',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT * FROM {place}_{tank} WHERE DATE(dt) = CURDATE() AND (HOUR(dt) = 15 AND MINUTE(dt) = 0);"
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
            sql = f"SELECT * FROM {place}_{tank} ORDER BY dt DESC LIMIT 60;"
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

@app.get("/first_graph_10/{place}/{tank}")
def get_table_information_10time(place, tank):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='umiru',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT DATE_FORMAT(t1.dt, '%Y-%m-%d') AS date, \
                            CONCAT(HOUR(t1.dt), ':', MINUTE(t1.dt), ':', SECOND(t1.dt)) AS time1, \
                            t1.temp AS temp1, \
                            t1.shibu, \
                            t1.condact, \
                            t1.do_per, \
                            t1.do_mg \
                    FROM {place}_{tank} as t1 \
                    WHERE (HOUR(t1.dt) = 10 AND MINUTE(t1.dt) = 0) ORDER BY date DESC LIMIT 7;"
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

@app.get("/first_graph_15/{place}/{tank}")
def get_table_information_15time(place, tank):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        database='umiru',
        cursorclass=pymysql.cursors.DictCursor
    )
    
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT DATE_FORMAT(t2.dt, '%Y-%m-%d') AS date, \
                            CONCAT(HOUR(t2.dt), ':', MINUTE(t2.dt), ':', SECOND(t2.dt)) AS time2, \
                            t2.temp AS temp2, \
                            t2.shibu, \
                            t2.condact, \
                            t2.do_per, \
                            t2.do_mg \
                    FROM {place}_{tank} as t2 \
                    WHERE (HOUR(t2.dt) = 15 AND MINUTE(t2.dt) = 0) ORDER BY date DESC LIMIT 7;"

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