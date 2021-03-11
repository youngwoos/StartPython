import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

mpg = pd.read_csv('data_mpg.csv')


seabo
####

import statsmodels.api as sm
mpg_raw = pd.read_csv("data_mpg.csv")


# 상수항을 추가한 회귀분석 하는 방법
# 방법1. sm.add_constant()을 이용해 상수항 추가
mpg = mpg_raw

y = mpg["hwy"]
x = sm.add_constant(mpg[["displ"]])
mod = sm.OLS(y, x).fit()
mod.summary()


#방법2. 직접 'const' 변수를 추가해 일괄 1 입력

mpg = mpg_raw
mpg['const'] = 1
mod = sm.OLS(mpg['hwy'], mpg[['const', 'displ']]).fit()
mod.summary()

###



# 한글 폰트 해결

# 소숫점 설정
# 주피터와 같은지 확인

# 반올림


df_finalexam = pd.read_excel('finalexam.xlsx',)
df_finalexam

mpg


df
tmp = pd.read_excel('finalexam.xlsx').head(3)
tmp2 = pd.read_csv('csv_exam.csv').head(3)
type(tmp)
type(tmp2)

tmp
tmp2


pd.concat([tmp, tmp])
pd.concat([tmp, tmp], ignore_index = True)


pd.concat([tmp, tmp2])

pd.concat([tmp, tmp2], join = 'inner')

pd.merge([tmp, tmp2], )


pd.concat([tmp, tmp], ignore_index = False)

pd.concat([tmp, tmp2], ignore_index = True)

pd.concat([tmp, tmp2], ignore_index = False)

pd.concat([tmp.reset_index(drop = True, inplace = True), tmp2.reset_index(drop = True, inplace = True)])









df = pd.read_csv('csv_exam.csv')

len(df)
type(df)

sum(df['math'])

sum([1,2,3,4])


type([1,2,3,4])

# 변수 명을 메서드 명과 같이하면 추출, 함수 적용 되나?




sum(df['math'])


tmp = pd.read_excel('finalexam.xlsx')



type(mpg)



## 비율 구하기
mpg = pd.read_csv('data_mpg.csv')
mpg.value_counts('class')/len(mpg)*100


## 하위 집단별 비율 구하기
# groupby().agg() 필요

# (1) 상위 집단별 빈도 구하기
df_a = mpg.groupby('drv').agg(n = ('class', 'count'))
df_a


# (2) 하위 집단별 빈도 구하기
df_b = mpg.groupby(['drv', 'class']).agg(n = ('drv', 'count'))
df_b


# (3) 하위 집단별 빈도를 하위 집단별 빈도로 나누기
sub_ratio = df_b/df_a*100
sub_ratio




# 날짜 데이터 처리

list_of_dates = ['2019-11-20', '2020-01-02', '2020-02-05','2020-03-10','2020-04-16']
employees=['Hisila', 'Shristi','Zeppy','Alina','Jerry']
df = pd.DataFrame({'Joined date': pd.to_datetime(list_of_dates)},index=employees)
df

df.info()

df['Joined date'].dt.year 
df['Joined date'].dt.month

df['Year'] = df['Joined date'].dt.year 
df['Month'] = df['Joined date'].dt.month 


df = pd.read_csv('data_economics.csv')
df
df.info()

df['date'] = pd.to_datetime(df['date'])
df.info()


df['year'] = df['date'].dt.year

sns.lineplot(data = df, x = 'date', y = 'psavert')
plt.show()


ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))






economics = pd.read_csv('data_economics.csv')
economics

sns.lineplot(data = economics, x = 'date', y = 'psavert')
plt.show()





# 날짜 타입으로 바꾸면 seaborn 에러난다

# 기본 데이터로 해보자
# 날짜변수가 어떤 타입인지

flights = sns.load_dataset('flights')
flights.info()

may_flights = flights.query("month == 'May'")
sns.lineplot(data=may_flights, x="year", y="passengers")
plt.show()

flights = sns.load_dataset("flights")
flights.head()


# #
# g = sns.relplot(data = mpg, x = 'displ', y = 'hwy')
# plt.tight_layout()
# 
# relplot은 plt.tight_layout() 안하면 축 잘림



# 그래프 재설정 절차
# 1. 그래프 설정 코드 수정
# 2. 캐시 지우기
# 3. R 세션 재실행 (Ctrl+Shift+F10)
# 4. RStudio refresh (F5)
# 5. Knit
 
# !조건: 그래프 설정, 생성 코드가 같은 청크 안에 있어야함
# 
# ```{python echo=F}
# import seaborn as sns
# mpg = pd.read_csv('data_mpg.csv')
# 
# # 그래프 설정
# plt.rcParams['figure.figsize'] = [6, 4]
# plt.rcParams.update({'font.size': '12'})
# 
# p = sns.scatterplot(data = mpg, x = 'displ', y = 'hwy')
# plt.show()
# ```



# 글자 폰트 크기
plt.rcParams.update({'font.size': '15'})

# 그래프 크기
plt.rcParams['figure.figsize'] = [6, 4]







# # 극단치 처리
# 
# 
# 
# ```{python}
# # 요약 통계량
# mpg['hwy'].describe()
# 
# # 1분위수
# q1 = mpg['hwy'].describe()[4]
# q1
# 
# # 3분위수
# q3 = mpg['hwy'].describe()[6]
# q3
# 
# # 1.5IQR
# iqr15 = (q3 - q1)*1.5
# iqr15
# 
# # 위 경계
# upper = q3 + iqr15
# upper
# 
# # 아래 경계
# lower = q1 - iqr15
# lower
# ```
