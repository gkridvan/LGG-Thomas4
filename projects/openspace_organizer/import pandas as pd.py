import pandas as pd
from typing import List

def load_colleagues(filepath: str) -> List[str]:
    df = pd.read_excel(filepath)
    names = df['Name'].tolist()
    return names
