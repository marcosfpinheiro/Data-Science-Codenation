import pandas as pd


def load_file(file):
    df = pd.read_csv(file)
    return df


def main():
    file = "desafio1.csv"
    df = load_file(file)
    print(df.head())


if __name__ == "__main__":
    main()
