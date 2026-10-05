import datetime  #날짜/ 시간과 관련된 기능을 가져옴.
import json  #JSON 형식의 데이터를 다루기 위한 모듈 가져옴.
import random

def save(data):  #데이터 저장 함수 정의.
    with open("memo.json", "w", encoding="utf-8") as f:  #memo.json 파일을 쓰기 모드로 열기.
         json.dump(data, f, ensure_ascii=False, indent=4)  #리스트를 JSON 형식으로 파일에 저장.

def load():  #데이터 불러오기 함수 정의.
    try:  #예외 처리 시작.
        with open("memo.json", "r", encoding="utf-8") as f:  #memo.json 파일을 읽기 모드로 열기.
            return json.load(f)  #파일에서 JSON 데이터를 읽어와 리스트로 반환.
    except (FileNotFoundError, json.JSONDecodeError):  #파일이 없거나 JSON 형식이 잘못되었을 경우 예외 처리.
        return []  #빈 리스트 반환.
    
data= load() #데이터 불러오기 함수 호출하여 data 변수에 저장.


def add_keyword(data):  #키워드 추가 함수 정의.
    keyWord = input("키워드를 적어주세요: ").strip()  #키워드 입력.
    if(keyWord == ""):  #만약 키워드가 비어있으면
        print("키워드를 입력해주세요.")  #메시지 출력.
        return  #함수 종료.
    dateTime = str(datetime.date.today())  #현재 날짜를 문자열로 변환.
    dict1 = {'word': keyWord, 'added': dateTime, 'removed': None}  #키워드와 날짜를 딕셔너리로 저장.
    data.append(dict1)  #리스트에 딕셔너리 추가.   

def show_keywords(data):  #키워드 출력 함수 정의.
    for n, idx in enumerate(get_active_indexes(data), 1):  #리스트의 인덱스와 값을 가져옴.
        print(f"{n}. {data[idx]['word']}")  #인덱스와 키워드 출력.
        print(f"   추가 날짜: {data[idx]['added']}")  #추가 날짜 출력.

def remove_keyword(data):  #키워드 제거 함수 정의.
    show_keywords(data)  #키워드 출력 함수 호출.
    active_idx = get_active_indexes(data)  #활성화된 키워드의 인덱스를 가져옴.
    try:  #예외 처리 시작.
        choice_idx = int(input("제거할 키워드 번호를 선택하세요.")) - 1  #사용자에게 제거할 키워드 번호 입력 받음.
    except ValueError:
        print("잘못된 입력입니다.")  #숫자가 아닌 값을 입력했을 경우 메시지 출력.
        return
    if (0 <= choice_idx < len(active_idx)):  #입력한 번호가 활성화된 키워드의 범위 내에 있는지 확인.
        real_idx = active_idx[choice_idx]  #실제 인덱스를 가져옴.
        data[real_idx]['removed'] = str(datetime.date.today())  #제거 날짜를 현재 날짜로 설정.
        print(data[real_idx]['word'] ) #제거된 키워드 출력.
    else:
        print("잘못된 번호입니다.")  #잘못된 번호 입력 시 메시지 출력.

def combine(data):  #키워드 결합 함수 정의.
    active = [] 
    for e in data:  #리스트의 값을 가져옴.
        if ( e['removed'] is None):  #만약 제거 날짜가 None이면(즉, 활성화된 키워드이면)
            active.append(e['word'])  #활성화된 키워드를 리스트에 추가.
    if (len(active) < 2):  #활성화된 키워드가 2개 미만이면
        print("활성화된 키워드가 2개 이상 필요합니다.")  #메시지 출력.
        return  #함수 종료.
    picked = random.sample(active, 2)  #활성화된 키워드 중 2개를 랜덤으로 선택.
    print (" + ".join(picked))  #선택된 키워드를 결합하여 출력.

def get_active_indexes(data):  #활성화된 키워드의 인덱스를 가져오는 함수 정의.
    return [i for i, e in enumerate(data) if e['removed'] is None]

while True:  #무한 루프 시작.
    print("1. 추가, 2. 목록, 3. 제거, 4. 조합, 5. 종료")  #메뉴 출력.
    choice = input("번호를 선택하세요.")  #사용자에게 선택 입력 받음.
    if choice == '1':  #사용자가 1을 선택하면 키워드 추가 함수 호출.
        add_keyword(data)
        save(data)  #데이터 저장 함수 호출.
    elif choice == '2':  #사용자가 2를 선택하면 키워드 출력 함수 호출.
        show_keywords(data)
    elif choice == '3':  #사용자가 3을 선택하면 키워드 제거 함수 호출.
        remove_keyword(data)
        save(data)  #데이터 저장 함수 호출.
    elif choice == '4':  #사용자가 4를 선택하면 키워드 결합 함수 호출.
        combine(data)
    elif choice == '5':  #사용자가 5를 선택하면 프로그램 종료.
        print("프로그램을 종료합니다.")  #종료 메시지 출력.
        break  #루프 종료.
