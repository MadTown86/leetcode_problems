import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    q = students.query("student_id == 101")
    return students.loc[students["student_id"] == 101, ["name", "age"]]


if __name__ == "__main__":
    inp = [
        [101, "Ulysses", "13"],
        [53, "William", 10],
        [128, "Henry", 6],
        [3, "Henry", 11],
    ]
    p = pd.DataFrame(inp, columns=["student_id", "name", "age"])
    print(selectData(p))
