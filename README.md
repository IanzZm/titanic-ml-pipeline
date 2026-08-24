# Titanic ML Pipeline

Pipeline completo de dados e modelo de classificação para prever
sobrevivência no Titanic

## O que faz
- Carrega e limpa o dataset do Titanic (valores ausentes, tipos de dados)
- Treina e compara modelos de classificação (Regressão Logística,
  Decision Tree, Random Forest)
- Otimiza hiperparâmetros via GridSearchCV (5-fold cross-validation)
- Modelo final: Random Forest (n_estimators=100, max_depth=10,
  criterion='entropy') — F1 macro de 0.821 em dados de teste

## Estrutura
- `src/limpeza.py` — pipeline de limpeza reutilizável
- `src/modelo.py` — treino do modelo final com hiperparâmetros otimizados
- `notebooks/` — exploração, EDA, modelagem e otimização (processo completo)

## Como rodar
\`\`\`python
from src.limpeza import carregar_e_limpar
from src.modelo import treinar_modelo_titanic
from sklearn.model_selection import train_test_split

df = carregar_e_limpar()
X, y = df[['age','pclass','fare','sex']], df['survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

modelo = treinar_modelo_titanic(X_train, y_train)
previsoes = modelo.predict(X_test)
\`\`\`