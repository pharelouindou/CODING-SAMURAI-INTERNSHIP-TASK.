import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('train.csv')

print("Missing values per column:")
print(df.isnull().sum())

num_cols = ['Age', 'Fare']
for col in num_cols:
    plt.figure()
    sns.histplot(df[col].dropna(), kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

cat_cols = ['Pclass', 'Sex', 'Embarked']
for col in cat_cols:
    plt.figure()
    sns.countplot(x=col, data=df)
    plt.title(f'Distribution of {col}')
    plt.show()

for col in cat_cols:
    plt.figure()
    sns.barplot(x=col, y='Survived', data=df)
    plt.title(f'Survival Rate by {col}')
    plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

print("\nBasic statistics:")
print(df.describe(include='all'))
