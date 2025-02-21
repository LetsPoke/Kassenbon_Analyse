import os
import pandas as pd


def load_receipts_data():
    csv_file = os.path.join("output", "autogenerated", "parsed_receipts.csv")
    df = pd.read_csv(csv_file)

    # Convert date and time to strings
    df["date"] = df["date"].astype(str)
    df["time"] = df["time"].astype(str)

    return df
