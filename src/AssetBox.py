import pandas as pd
from Asset import Asset

class AssetBox:
    def __init__(self, entry):
        self.entry = entry
        self.encode()
        
    @property
    def categorical_df(self):
        return self.df.select_dtypes(
            include=['object', 'category']
        )
        
    @property
    def numerical_df(self):
        return self.df.select_dtypes(
            include=['int', 'float']
        )
        
    @property
    def categorical_features(self):
        return self.categorical_df.dtypes

    @property
    def numerical_features(self):
        return self.numerical_df.dtypes

    def encode(self):
        self.entry = map(
            lambda x: Asset(x).to_dict,
            self.entry,
        )

        self.df = pd.DataFrame(list(self.entry))
        
        
    def print(self):
        print(self.df)
        print(self.numerical_df.corr())


