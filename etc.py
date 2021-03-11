import pandas as pd
import seaborn as sns
import numpy as pd

mpg = pd.read_csv('data_mpg.csv')

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

sum(df['math'])

sum([1,2,3,4])


type([1,2,3,4])

# 변수 명을 메서드 명과 같이하면 추출, 함수 적용 되나?




sum(df['math'])


tmp = pd.read_excel('finalexam.xlsx')


