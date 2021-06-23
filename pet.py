import numpy as np
import pandas as pd
from icecream import ic

menu = '''
'0. 종료\n''
'1. 라이브러리 임포트\n'
'2. 판다스 버전 출력\n'
'3. 판다스 라이브러리 버전 정보 모두 출력\n'
'4. 주어진 값으로 DataFrame 객체를 생성하시오\n'
'5. 객체내부 정보를 출력\n'
'6. 객체 상위 3열까지 출력\n'
'7. animal과 age 컬럼만 출력\n'
'8. 객체의 3, 4, 8번 열에 해당하는 animal과 age 값만 출력\n'
'9. visits 컬럼에서 3 초과하는 값 출력\n'
'10. age 에서 NaN 값 출력\n'
'11. age가 3살 미만 고양이값 출력\n'
'12. age가 2살이상 4살 미만인 값 출력\n'
'13. f 행의 나이를 1.5살로 변경\n'
'14. 객체에서 visit 의 합 출력\n'
'15. 동물별로 나이의 평균 출력\n'
'16. k열을 추가하여 dog , 5.5세, 우선권없음(no), 방문회수 2회 열을 추가\n'
'16-1 방금 추가한 열 삭제\n'
'17 객체에 있는 동물의 종류의 수 출력\n'
'18. age 는 내림차순, visits 는 오름차순으로 정렬\n'
'19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력\n'
'20. snake 를 python 으로 값을 변경\n'
'21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.')
'''


def quiz2():
    ic(pd.__version__)


def quiz3():
    ic(pd.show_versions())


def quiz_4():
    data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
            'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
            'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

    df = pd.DataFrame(data, index=labels)
    ic(df)


df.info()

df.head(3)

df[['animal', 'age']]

df.loc[['c', 'd', 'h'], ['animal', 'age']]

df[df['visits'] > 3]

df[df['age'].isnull()]

#
df[(df['age'] < 3) & (df['animal'] == 'cat')]

# %%

#
df[(df['age'] >= 2) & (df['age'] < 4)]

# %%

#
df.loc['f', 'age'] = 1.5

# %%

df

# %%

#
df['visits'].sum()

# %%

#
df.groupby('animal')['age'].mean()

# %%

#
df.loc['k'] = ['dog', 5.5, 2, 'no']

# %%

df.drop('k', inplace=True)

# %%

#
df['animal'].value_counts()

# %%

# 18. age 는 내림차순, visits 는 오름차순으로 정렬
df.sort_values(by=['age', 'visits'], ascending=[False, True])

# %%

# 19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력
df['priority'] = df['priority'].map({'yes': True, 'no': False})
df

# %%

# 20. snake 를 python 으로 값을 변경
df['animal'] = df['animal'].replace('snake', 'python')
df

# %%

# 21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.
# 즉,각 행은 animal 이고, 각 열은 visits 이며, 값은 평균연령
# (힌트, 피벗 테이블을 활용해야 함)
df = df.pivot_table(index='animal', columns='visits', values='age', aggfunc='mean')
df

# %%
