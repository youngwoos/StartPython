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



# 그래프 설정 - knit가 아니라 직접 한번 실행해줘야 하는듯?
# r코드 reticulate로 실행?

# 글자 폰트 크기
# 한번 설정하면 슬라이드 전체 적용되는듯
# 재설정 하려면 캐시 지우기, R 재실행, RStudio 재실행, 생성된 파일 삭제

plt.rcParams.update({'font.size': '15'})

# 그래프 크기
# 작동이 랜덤하다
plt.rcParams['figure.figsize'] = [6, 4]


# # 파이썬 리셋 R 코드
# reticulate::py_config()


del plt
del sns
