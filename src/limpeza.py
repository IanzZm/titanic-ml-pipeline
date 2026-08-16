import seaborn as sns
import pandas as pd


def carregar_e_limpar() -> pd.DataFrame:
    df = sns.load_dataset('titanic')

    # limpando/preenchendo os dados vazios
    df = df.dropna(subset=['embark_town'])
    df['age'] = df['age'].fillna(df['age'].median())
    df = df.drop(columns='deck')

    # convertendo as colunas para os tipos otimizados
    df['alive'] = df['alive'] == 'yes'
    df['sex'] = df['sex'].astype('category')
    df['pclass'] = df['pclass'].astype('category')

    portos_info = pd.DataFrame({
        'embark_town': ['Southampton', 'Cherbourg', 'Queenstown'],
        'pais': ['Inglaterra', 'França', 'Irlanda']
    })
    df = df.merge(portos_info, how='left', on='embark_town')

    return df
