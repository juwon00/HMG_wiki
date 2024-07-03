import sqlite3
from etl_project_gdp import log


# 테이블 생성
def create_table():
    log("create table start")
    # 데이터베이스 연결 (파일 기반 DB를 사용)
    conn = sqlite3.connect("World_Economies.db")

    # 커서 생성
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Countries_by_GDP (
            id INTEGER PRIMARY KEY,
            Country TEXT,
            GDP_USD_billion INTEGER
        )
    """
    )
    # 변경 사항 저장
    conn.commit()

    # 데이터베이스 연결 종료
    conn.close()
    log("create table end")


# 테이블 초기화
def delete_table():
    log("delete table start")
    # 데이터베이스 연결 (파일 기반 DB를 사용)
    conn = sqlite3.connect("World_Economies.db")

    # 커서 생성
    cursor = conn.cursor()

    # 테이블 생성
    cursor.execute(
        """
        DELETE FROM Countries_by_GDP
    """
    )
    # 변경 사항 저장
    conn.commit()

    # 데이터베이스 연결 종료
    conn.close()
    log("delete table end")


# 테이블에 데이터 삽입
def insert_data_to_table(gdp):
    log("insert data to table start")
    # 데이터베이스 연결 (파일 기반 DB를 사용)
    conn = sqlite3.connect("World_Economies.db")

    # 커서 생성
    cursor = conn.cursor()

    # 데이터 삽입
    for entry in gdp:
        cursor.execute(
            """
            INSERT INTO Countries_by_GDP (Country, GDP_USD_billion) VALUES (?, ?)
        """,
            (entry["Country"], entry["GDP_USD_billion"]),
        )

    # 변경 사항 저장
    conn.commit()

    # 데이터베이스 연결 종료
    conn.close()
    log("insert data to table end")


# 모든 데이터 select
def select_all_data():
    log("select all data start")
    # 데이터베이스 연결 (파일 기반 DB를 사용)
    conn = sqlite3.connect("World_Economies.db")

    # 커서 생성
    cursor = conn.cursor()

    # 데이터 확인
    cursor.execute("SELECT * FROM Countries_by_GDP")
    rows = cursor.fetchall()

    # 데이터베이스 연결 종료
    conn.close()

    log("select all data end")
    return rows


# 100B 넘는 데이터만 검색
def select_gdp_over_100B():
    log("select gdp over 100B data start")
    # 데이터베이스 연결 (파일 기반 DB를 사용)
    conn = sqlite3.connect("World_Economies.db")

    # 커서 생성
    cursor = conn.cursor()

    # 데이터 확인
    cursor.execute("SELECT * FROM Countries_by_GDP WHERE GDP_USD_billion >= 100")
    rows = cursor.fetchall()

    # 데이터베이스 연결 종료
    conn.close()

    log("select gdp over 100B data data end")
    return rows
