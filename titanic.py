import seaborn as sns
import pandas as pd

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