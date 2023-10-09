# https://leetcode.com/problems/drop-duplicate-rows/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=["email"])


if __name__ == "__main__":
    inp = [
        [1, "ella", "emily@example.com"],
        [2, "David", "michael@example.com"],
        [3, "Zacharcy", "sarah@example.com"],
        [4, "Alice", "john@example.com"],
        [5, "Finn", "john@example.com"],
        [6, "Violet", "alice@example.com"],
    ]

    p = pd.DataFrame(inp, columns=["customer_id", "name", "email"])
    print(dropDuplicateEmails(p))
