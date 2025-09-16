# Titanic Dataset Exploratory Data Analysis

## Description
This project performs an Exploratory Data Analysis (EDA) on the Titanic dataset to understand passenger survival patterns and relationships between different features.

## Dataset
The analysis uses two main files:
- `train.csv`: Training dataset with 891 passengers
- `test.csv`: Test dataset with 418 passengers

### Features
- Survived: Passenger survival (0 = No; 1 = Yes)
- Pclass: Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)
- Sex: Gender of passenger
- Age: Age in years
- SibSp: Number of siblings/spouses aboard
- Parch: Number of parents/children aboard
- Ticket: Ticket number
- Fare: Passenger fare
- Cabin: Cabin number
- Embarked: Port of embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

## Analysis Performed
- Missing values identification
- Distribution analysis of numerical features
- Categorical features visualization
- Survival rate analysis
- Correlation analysis between features

## Requirements
```
pandas
matplotlib
seaborn
```

## Usage
Run the analysis script:
```bash
python eda_titanic.py
```

## Key Findings
- Age and fare distributions
- Survival rates by passenger class, gender, and port of embarkation
- Correlation patterns between numerical features

## Author
OUINDOU Ayeyemi Pharel Aaron

## License
This project is open source and available under the MIT License.
