import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def treinar_modelo_titanic(X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestClassifier:
    model = RandomForestClassifier(criterion='entropy',max_depth=10, n_estimators= 100, random_state=0).fit(X_train, y_train)

    return model

    

    

