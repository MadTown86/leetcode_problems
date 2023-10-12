import pandas as pd
from typing import List

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    print(players.columns.size)
    print(players.index.size)
    print(players.axes)
    print(players.ndim)
    print(players.shape)
    return [players.index.size, players.columns.size]

if __name__ == "__main__":
    inp = [[846, 'Mason', 21, 'Forward', 'RealMadrid'],
     [749, 'Riley', 30, 'Winger', 'Barcelona'],
     [155, 'Bob', 28, 'Striker', 'ManchesterUnited'],
     [583, 'Isabella', 32, 'Goalkeeper', 'Liverpool']]

    p = pd.DataFrame(inp, columns=['player_id', 'name', 'age', 'position', 'team'])
    getDataframeSize(p)