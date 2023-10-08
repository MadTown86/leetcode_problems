import pandas as pd


def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

if __name__ == "__main__":
    inp = [[846, 'Mason', 21, 'Forward', 'RealMadrid'],
     [749, 'Riley', 30, 'Winger', 'Barcelona'],
     [155, 'Bob', 28, 'Striker', 'ManchesterUnited'],
     [583, 'Isabella', 32, 'Goalkeeper', 'Liverpool']]
    p = pd.DataFrame(inp, columns=['rank', 'name', 'age', 'position', 'team'])
    print(selectFirstRows(p))