import os

DATASET_FILE_PATH: str = os.getcwd() + '/src/data/state-wise-year-wise-number-of-cyber-crimes-reported.csv'
DATABASE_ARGS: dict[str, str] = {
    'host': 'localhost',
    'user': 'root',
    'passwd': '1234',
    'database': 'cyber_crimes'
}

