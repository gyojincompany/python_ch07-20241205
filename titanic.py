import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# 한글 깨짐 방지 - 한글용 폰트 추가
plt.rcParams['font.family'] = "Malgun Gothic"
plt.rcParams['axes.unicode_minus'] = False

titanic = sns.load_dataset("titanic")
# print(titanic)
# titanic.to_csv("data/titanic.csv", index=False)  # csv파일로 저장
titanic.info()

print(titanic.isnull().sum())  # 각 필드의 결측치 합

titanic["age"] = titanic["age"].fillna(titanic["age"].median())  # 결측치들을 age 의 중앙값으로 모두 채우기
print(titanic["embarked"].value_counts())  # 각 항구별 탑승객 수->S가 대다수
titanic["embarked"] = titanic["embarked"].fillna("S")  # 2개의 결측치를 'S'로 대입

titanic["embark_town"] = titanic["embark_town"].fillna("Southampton")  # 2개의 결측치를 'Southampton'로 대입

print(titanic["deck"].value_counts())
titanic["deck"] = titanic["deck"].fillna("C")  # 결측치를 'C'로 대입

print(titanic.isnull().sum())  # 각 필드의 결측치 합

f, ax = plt.subplots(1, 2, figsize=(10,5))
print(titanic["survived"][titanic["sex"]=="male"].value_counts())  # 남자의 생존 1, 사망 0 의 수
print(titanic["survived"][titanic["sex"]=="female"].value_counts())  # 여자의 생존 1, 사망 0 의 수

titanic["survived"][titanic["sex"]=="male"].value_counts().plot.pie(ax=ax[0])
titanic["survived"][titanic["sex"]=="female"].value_counts().plot.pie(ax=ax[1])

ax[0].set_title("Survived (Male)")
ax[1].set_title("Survived (Female)")

plt.show()

sns.countplot(data=titanic, x="pclass", hue="survived")  # 객실등급과 생존률
plt.title("객실등급 vs 생존률")
plt.show()