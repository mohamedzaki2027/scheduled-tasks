import pandas as pd


class DataManager():
    def __init__(self, path):
        self.data = {}
        self.load_data(path)

    def load_data(self, path):
        df = pd.read_csv(path)
        self.data = {(row['month'], row['day']): row
                     for (index, row) in df.iterrows()}

    def search_data(self, birthday_date):
        return self.data.get(birthday_date)
