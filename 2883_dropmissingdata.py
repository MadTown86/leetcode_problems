# https://leetcode.com/problems/drop-missing-data/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])


if __name__ == "__main__":
    inp = [[32, "Piper", 5], [217, "Grace", 19], [779, None, 20], [849, None, 14]]
    p = pd.DataFrame(inp, columns=["student_id", "name", "age"])
    print(dropMissingData(p))
