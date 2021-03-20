from pykiwoom.kiwoom import *
import pprint
# import time
# import pyautogui
# pyqutogui 사용법
# https://blankspace-dev.tistory.com/417


print("02) 로그인")
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)
print("블록킹 로그인 완료")

# print("키움증권 실행")
# time.sleep(2)
# print("비밀번호 입력")
# pyautogui.typewrite("gktjdwo0")
# pyautogui.press("enter")

print("03) 사용자 정보 얻어오기")
account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")            # 키보드보안 해지여부
firewall = kiwoom.GetLoginInfo("FIREW_SECGB")           # 방화벽 설정 여부

print(account_num)
print(accounts)
print(user_id)
print(user_name)
print(keyboard)
print(firewall)

print("04) 종목 코드 얻기")
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(len(kospi), kospi)
print(len(kosdaq), kosdaq)
print(len(etf), etf)

print("05) 종목명 얻기")
name = kiwoom.GetMasterCodeName("005930")
print(name)

print("06) 연결 상태 확인")
state = kiwoom.GetConnectState()
if state == 0:
    print("미연결")
elif state == 1:
    print("연결완료")

print("07) 상장 주식수 얻기")
stock_cnt = kiwoom.GetMasterListedStockCnt("005930")
print("삼성전자 상장주식수: ", stock_cnt)

print("08) 감리구분")
감리구분 = kiwoom.GetMasterConstruction("005930")
print(감리구분)

print("09) 상장일")
상장일 = kiwoom.GetMasterListedStockDate("005930")
print(상장일)
print(type(상장일))        # datetime.datetime 객체

print("10) 전일가")
전일가 = kiwoom.GetMasterLastPrice("005930")
print(int(전일가))
print(type(전일가))

print("11) 종목상태")
종목상태 = kiwoom.GetMasterStockState("005930")
print(종목상태)

print("12) 테마")
group = kiwoom.GetThemeGroupList(1)
pprint.pprint(group)

tickers = kiwoom.GetThemeGroupCode('141')
print(tickers)

tickers = kiwoom.GetThemeGroupCode('330')
for ticker in tickers:
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)

print("*조건검색 일반조회")
# 조건식을 PC로 다운로드
kiwoom.GetConditionLoad()

# 전체 조건식 리스트 얻기
conditions = kiwoom.GetConditionNameList()

# 0번 조건식에 해당하는 종목 리스트 출력
condition_index = conditions[0][0]
condition_name = conditions[0][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(codes)

print("*매매-매수")
# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

# 삼성전자, 10주, 시장가주문 매수
kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, "005930", 10, 0, "03", "")

print("*매매-매도")
# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

# 삼성전자, 10주, 시장가주문 매도
kiwoom.SendOrder("시장가매도", "0101", stock_account, 2, "005930", 10, 0, "03", "")

print("*TR일반조회-싱글데이터 TR 사용하기")
df = kiwoom.block_request("opt10001",
                          종목코드="005930",
                          output="주식기본정보",
                          next=0)
print(df)

print("*TR일반조회-멀티데이터 TR")
dfs = []
df = kiwoom.block_request("opt10081",
                          종목코드="005930",
                          기준일자="20200424",
                          수정주가구분=1,
                          output="주식일봉차트조회",
                          next=0)
print(df.head())
dfs.append(df)

while kiwoom.tr_remained:
    df = kiwoom.block_request("opt10081",
                              종목코드="005930",
                              기준일자="20200424",
                              수정주가구분=1,
                              output="주식일봉차트조회",
                              next=2)
    dfs.append(df)
    time.sleep(1)

df = pd.concat(dfs)
df.to_excel("data\\005930.xlsx")

# 전종목 종목코드
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
codes = kospi + kosdaq

# 문자열로 오늘 날짜 얻기
now = datetime.datetime.now()
today = now.strftime("%Y%m%d")

# 전 종목의 일봉 데이터
for i, code in enumerate(codes):
    if i > 1606:
        print(f"{i}/{len(codes)} {code}")
        df = kiwoom.block_request("opt10081",
                                  종목코드=code,
                                  기준일자=today,
                                  수정주가구분=1,
                                  output="주식일봉차트조회",
                                  next=0)

        out_name = f"data\\{code}.xlsx"
        df.to_excel(out_name)
        time.sleep(3.6)










