# https://leetcode.com/problems/modify-columns/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    s = pd.Series(employees["salaries"])
    employees


if __name__ == "__main__":
    inp = [["Jack", 19666], ["Piper", 74754], ["Mia", 125018], ["Ulysses", 109732]]
    p = pd.DataFrame(inp, columns=["name", "salary"])
