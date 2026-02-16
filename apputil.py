# update/add code below ...
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
fibonacci(9)

###
def to_binary(n: int) -> str:
    if n < 0:
        print("cannot be negative")
    if n < 2:
        return str(n)
    else:
        return to_binary(n // 2) + str(n % 2)
to_binary(2)
######
import pandas as pd
url = 'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/book/data/bellevue_almshouse_modified.csv'

df_bellevue = pd.read_csv(url)
df_bellevue["gender"] = df_bellevue["gender"].astype(str).str.strip().str.lower()
df_bellevue.loc[~df_bellevue["gender"].isin(["m","w"]), "gender"] = pd.NA

def task_1():
    print("The gender column returned multiple values that I did not expect. " \
    "I changed the letters not representing man or woman to missing because we cannot know what those values mean.")
    return df_bellevue.isna().sum().sort_values().index.tolist()


def task_2():
    print("For ease changing the data column to datetime format first was essential.")
    return (
        df_bellevue.assign(year=pd.to_datetime(df_bellevue["date_in"], errors="coerce").dt.year)
        .groupby("year")
        .size()
        .reset_index(name="total_admissions")
    )


def task_3():
    return df_bellevue.groupby("gender")["age"].mean()


def task_4():
    return df_bellevue["profession"].value_counts().head(5).index.tolist()
