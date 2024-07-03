import json
import datetime
import os


def log(text):
    now = datetime.datetime.now()
    now_date = now.strftime("%Y-%B-%d-%H-%M-%S")

    # 현재 스크립트가 실행되는 디렉토리 경로 가져오기
    script_directory = os.path.dirname(os.path.abspath(__file__))
    # 파일 경로 설정
    file_path = os.path.join(script_directory, "etl_project_log.txt")

    with open(file_path, "a") as f:
        f.write(now_date + " " + text + "\n")


# 추출한 데이터 json 형식으로 저장하기
def gdp_to_json(gdp_data):
    log("json store start")
    file_path = "Countries_by_GDP.json"
    with open(file_path, "w") as f:
        json.dump(gdp_data, f)
    f.close()
    log("json store end")


# gdp 100B 이상인 국가 출력하기
def gdp_over_100B_print(gdp_data):
    log("gdp_over_100B_print start")
    for data in gdp_data:
        if data and data["GDP_USD_billion"] > 100:
            print(data["Country"], " - ", data["GDP_USD_billion"])
    log("gdp_over_100B_print end")
