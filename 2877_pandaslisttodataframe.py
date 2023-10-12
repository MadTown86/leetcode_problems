import pandas as pd
from typing import List
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns= ['student_id', 'age'])

if __name__ == "__main__":
    inp = [[1, 15], [2, 25], [5, 99], [3, 76]]
    print(createDataframe(inp))