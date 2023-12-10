from sklearn.model_selection import train_test_split

def split_data(data, test_size=0.3):
    train_data, test_data = train_test_split(data, test_size=test_size, random_state=42)
    return train_data, test_data