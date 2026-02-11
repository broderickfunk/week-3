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
def task_1():
    # columns sorted least -> most missing values
    return df_bellevue.isna().sum().sort_values().index.tolist()


def task_2():
    # dataframe: year, total_admissions
    return (
        df_bellevue.assign(year=pd.to_datetime(df_bellevue["date_in"], errors="coerce").dt.year)
                  .groupby("year")
                  .size()
                  .reset_index(name="total_admissions")
    )


def task_3():
    # series: index=gender, values=avg age
    return df_bellevue.groupby("gender")["age"].mean()


def task_4():
    # list: 5 most common professions
    return df_bellevue["profession"].value_counts().head(5).index.tolist()