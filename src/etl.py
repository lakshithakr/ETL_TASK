import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    # Add age group
    age_bins = [17, 25, 35, 45, 60]
    age_labels = ['18-25', '26-35', '36-45', '46-60']
    df['AgeGroup'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)

    # Add salary level
    salary_bins = [0, 30000, 60000, 90000, 150000]
    salary_labels = ['Low', 'Medium', 'High', 'Very High']
    df['SalaryLevel'] = pd.cut(df['EstimatedSalary'], bins=salary_bins, labels=salary_labels)

    return df

def save_data(df: pd.DataFrame, path: str):
    df.to_csv(path, index=False)