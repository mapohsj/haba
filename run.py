from pykiwoom.kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

account_num = kiwoom.GetLoginInfo("ACCOUNT_CNT")        # 전체 계좌수
accounts = kiwoom.GetLoginInfo("ACCNO")                 # 전체 계좌 리스트
user_id = kiwoom.GetLoginInfo("USER_ID")                # 사용자 ID
user_name = kiwoom.GetLoginInfo("USER_NAME")            # 사용자명
keyboard = kiwoom.GetLoginInfo("KEY_BSECGB")            # 키보드보안 해지여부
firewall = kiwoom.GetLoginInfo("FIREW_SECGB")           # 방화벽 설정 여부

print("전체 계좌수 : ", account_num)
print("전체 계좌 리스트 : ", accounts)
print("사용자 ID : ", user_id)
print("사용자명 : ", user_name)
print("키보드보안 해지여부 : ", keyboard)
print("방화벽 설정 여부 : ", firewall)

kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(len(kospi), kospi)
print(len(kosdaq), kosdaq)
print(len(etf), etf)

name = kiwoom.GetMasterCodeName("005930")
print(name)

state = kiwoom.GetConnectState()
if state == 0:
    print("미연결")
elif state == 1:
    print("연결완료")

stock_cnt = kiwoom.GetMasterListedStockCnt("005930")
print("삼성전자 상장주식수: ", stock_cnt)

# 감리구분은 '정상', '투자주의', '투자경고', '투자위험', '투자주의환기종목'의 값
감리구분 = kiwoom.GetMasterConstruction("005930")
print(감리구분)

상장일 = kiwoom.GetMasterListedStockDate("005930")
print(상장일)
print(type(상장일))        # datetime.datetime 객체

전일가 = kiwoom.GetMasterLastPrice("005930")
print(int(전일가))
print(type(전일가))

종목상태 = kiwoom.GetMasterStockState("005930")
print(종목상태)

group = kiwoom.GetThemeGroupList(1)
pprint.pprint(group)

tickers = kiwoom.GetThemeGroupCode('141')
print(tickers)

tickers = kiwoom.GetThemeGroupCode('330')
for ticker in tickers:
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)

# 조건식을 PC로 다운로드
kiwoom.GetConditionLoad()

# 전체 조건식 리스트 얻기
conditions = kiwoom.GetConditionNameList()
print("conditions :: ", conditions)

# 0번 조건식에 해당하는 종목 리스트 출력
condition_index = conditions[0][0]
print("condition_index :: ", condition_index)
condition_name = conditions[0][1]
print("condition_name :: ", condition_name)
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print("codes :: ", codes)


# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

# 삼성전자, 10주, 시장가주문 매수
kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, "005930", 10, 0, "03", "")

# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

# 삼성전자, 10주, 시장가주문 매도
kiwoom.SendOrder("시장가매도", "0101", stock_account, 2, "005930", 10, 0, "03", "")