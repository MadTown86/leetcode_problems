# https://leetcode.com/problems/create-a-new-column/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd


def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    data = pd.Series(employees["salary"] * 2)
    employees.insert(loc=employees.shape[1], column="bonus", value=data)
    return employees


if __name__ == "__main__":
    inp = [["Piper", 4548], ["Grace", 28150], ["Georgia", 1103]]
    p = pd.DataFrame(inp, columns=["name", "salary"])
    createBonusColumn(p)
