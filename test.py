import pyupbit

access = "jV7xzWySUHtKxz12ZurDA0xZiGAjffnVgZ5E4xsy"          # 본인 값으로 변경
secret = "brILnrEZMWCi4JmTQ4dnZ9LtRk32SEzroQoAA7Y3"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

# print(pyupbit.get_tickers())
print(upbit.get_balance("KRW"))     # KRW-XRP 조회
print(upbit.get_balance("KRW-MVL"))         # 보유 현금 조회
