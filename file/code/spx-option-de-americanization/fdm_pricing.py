import QuantLib as ql
import pandas as pd
data = pd.read_csv('data/clean_data2023.csv')
data['MaturityDate'] = pd.to_datetime(data['EXPIRE_DATE']).apply(lambda x: ql.Date(x.day, x.month, x.year))
DATE = '2023-6-20'
min_dte = 30
max_dte = 365*2

# 确保QUOTE_DATE列是日期格式
data['QUOTE_DATE'] = pd.to_datetime(data['QUOTE_DATE'])

# 筛选数据
filtered_data = data[(data['QUOTE_DATE'] == DATE) & (data['DTE'] >= min_dte) & (data['DTE'] <= max_dte)].copy()
# 将EXPIRE_DATE转换为QuantLib的Date对象
filtered_data['MaturityDate'] = pd.to_datetime(filtered_data['EXPIRE_DATE']).apply(lambda x: ql.Date(x.day, x.month, x.year))
# 获取并排序独特的到期日和行权价格
maturity_dates = sorted(filtered_data['MaturityDate'].unique(), key=lambda x: x.serialNumber())
strikes = sorted(filtered_data['STRIKE'].unique())

volatilityMatrix = ql.Matrix(len(strikes), len(maturity_dates))
for i, date in enumerate(maturity_dates):
    for j, strike in enumerate(strikes):
        vol_data = filtered_data[(filtered_data['MaturityDate'] == date) & (filtered_data['STRIKE'] == strike)]['P_IV']
        if not vol_data.empty:
            vol = vol_data.values[0]
        else:
            vol = 0.0
        volatilityMatrix[j][i] = vol

specificDate = ql.Date(4, 5, 2023)  # -day，-month，-year
ql.Settings.instance().evaluationDate = specificDate
calendar = ql.NullCalendar()
dayCounter = ql.Actual365Fixed()
volatilitySurface = ql.BlackVarianceSurface(specificDate, calendar, maturity_dates, strikes, volatilityMatrix, dayCounter)
volatilitySurface.enableExtrapolation()
volatilityHandle = ql.BlackVolTermStructureHandle(volatilitySurface)
riskFreeTS = ql.YieldTermStructureHandle(
    ql.FlatForward(specificDate, 0.0576, ql.Actual365Fixed(), ql.Compounded, ql.Annual)
)
dividendTS = ql.YieldTermStructureHandle(ql.FlatForward(specificDate, 0.0166, ql.Actual365Fixed()))
initialValue = ql.QuoteHandle(ql.SimpleQuote(4061.6))
process = ql.BlackScholesMertonProcess(initialValue, dividendTS, riskFreeTS, volatilityHandle)

#Select Pricing Engine
#Finite Difference
tGrid, xGrid = 2000, 200
engine = ql.FdBlackScholesVanillaEngine(process, tGrid, xGrid)

maturityDate = ql.Date(23, 5, 2023)  # Suppose Expiry Date 2023/May/23


# option_prices = []
# for index, row in data.iterrows():
#     strikePrice = row['STRIKE']
#     payoff = ql.PlainVanillaPayoff(ql.Option.Put, strikePrice)
#     exercise = ql.AmericanExercise(specificDate, maturityDate)
#     option = ql.VanillaOption(payoff, exercise)
#     volatilitySurface = ql.BlackVarianceSurface(specificDate, calendar, maturity_dates, strikes, volatilityMatrix, dayCounter)
#     volatilitySurface.enableExtrapolation()
#     volatilityHandle = ql.BlackVolTermStructureHandle(volatilitySurface)
#     process = ql.BlackScholesMertonProcess(initialValue, dividendTS, riskFreeTS, volatilityHandle)

strikePrice = 4175.0
payoff = ql.PlainVanillaPayoff(ql.Option.Put, strikePrice)
exercise = ql.AmericanExercise(specificDate, maturityDate)
americanOption = ql.VanillaOption(payoff, exercise)
americanOption.setPricingEngine(engine)
# Pricing American Option
optionPrice = americanOption.NPV()
print("The price of the American Option is:", optionPrice)

exercise = ql.EuropeanExercise(maturityDate)
# 创建欧式期权
europeanOption = ql.VanillaOption(payoff, exercise)
# 使用欧式期权定价引擎
engine = ql.AnalyticEuropeanEngine(process)
# 设置定价引擎
europeanOption.setPricingEngine(engine)
# 计算期权价值
optionPrice = europeanOption.NPV()
print("The price of the European Option is:", optionPrice)
