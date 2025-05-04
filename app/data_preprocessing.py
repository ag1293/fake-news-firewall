import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_prepare_data():
    # Load both CSVs
    df_fake = pd.read_csv("data/Fake.csv")
    df_true = pd.read_csv("data/True.csv")

    # Add labels
    df_fake['label'] = 'Fake'
    df_true['label'] = 'Real'

    # Combine
    df = pd.concat([df_fake, df_true])
    
    # Drop duplicates & missing values
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    # Use title + text combined (or just title)
    df['content'] = df['title'] + " " + df['text']

    # Final data
    X = df['content']
    y = df['label']

    return train_test_split(X, y, test_size=0.2, random_state=42)
