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

# f, ax = plt.subplots(1, 2, figsize=(10,5))
# print(titanic["survived"][titanic["sex"]=="male"].value_counts())  # 남자의 생존 1, 사망 0 의 수
# print(titanic["survived"][titanic["sex"]=="female"].value_counts())  # 여자의 생존 1, 사망 0 의 수
#
# titanic["survived"][titanic["sex"]=="male"].value_counts().plot.pie(ax=ax[0])
# titanic["survived"][titanic["sex"]=="female"].value_counts().plot.pie(ax=ax[1])
#
# ax[0].set_title("Survived (Male)")
# ax[1].set_title("Survived (Female)")
#
# plt.show()

# sns.countplot(data=titanic, x="pclass", hue="survived")  # 객실등급과 생존률
# plt.title("객실등급 vs 생존률")
# plt.show()

titanic2 = titanic.select_dtypes(include=[int, float, bool])
# titanic 칼럼 중 문자열을 제외한 정수, 실수, bool 타입의 칼럼만 추출하여 다시 저장
print(titanic2)

titanic_corr = titanic2.corr(method="pearson")  # 상관분석
print(titanic_corr)
# titanic_corr.to_csv("data/titanic_corr.csv", index=False)
# print(sns.get_dataset_names())  # seaborn 에서 제공하는 기본 데이터 이름 출력

# sns.pairplot(titanic2, hue="survived")
# plt.show()

# sns.catplot(data=titanic, x="pclass", y="survived", hue="sex", kind="point")
# plt.show()

def category_age(age):
    if age < 10: # 10세 미만
       return 0
    elif age< 20: # 10대
       return 1
    elif age< 30: # 20대
       return 2
    elif age< 40: # 30대
       return 3
    elif age< 50: # 40대
       return 4
    elif age< 60: # 50대
       return 5
    elif age< 70: # 60대
       return 6
    else: # 70세 이상
       return 7

titanic["age2"] = titanic["age"].apply(category_age)
# titanic 데이터에 새로운 칼럼이 생성->기존의 age 칼럼의 나이로 등급으로 환산
print(titanic)
titanic["sex"] = titanic["sex"].map({"male":1, "female":0})
# 성별 male->1, female->0 으로 변환(문자열->숫자)
print(titanic)
titanic["family"] = titanic["sibsp"] + titanic["parch"] + 1
# 형제/자매/배우자 + 부모/자식 + 본인 -> family 열로 새로 생성
print(titanic)

heatmap_data = titanic[["survived","sex","age2","family","pclass","fare"]]
print(heatmap_data.corr())

colormap = plt.cm.RdBu

sns.heatmap(heatmap_data.corr(), cmap=colormap, linecolor="white", annot=True,
            annot_kws={"size":10}, square=True, linewidths=0.1, vmax=1.0)

plt.show()