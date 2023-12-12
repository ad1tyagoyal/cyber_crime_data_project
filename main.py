import pandas as pd

from src.utils.constants import DATASET_FILE_PATH, DATABASE_ARGS
from src.utils.file_util import read_csv_file_as_df
from src.utils.logger_util import Log
from src.utils.db_util import DatabaseManager


def run_process():
    Log.get_instance().setup_logger()
    db_args: dict[str, str] = DATABASE_ARGS
    DatabaseManager.get_instance().establish_connection(db_args)
    DatabaseManager.get_instance().make_schema('cyber_crimes')
    cyber_attacks_data_frame: pd.DataFrame = read_csv_file_as_df(DATASET_FILE_PATH)
    DatabaseManager.upload_data(table_name='crime_data', df=cyber_attacks_data_frame)
    DatabaseManager.close_connection()


if __name__ == '__main__':
    run_process()
