import pandas as pd

from src.utils.constants import DATASET_FILE_PATH
from src.utils.file_util import read_csv_file_as_df
from src.utils.logger_util import Log


def run_process():
    Log.setup_logger()
    cyber_attacks_data_frame: pd.DataFrame = read_csv_file_as_df(DATASET_FILE_PATH)
    print(cyber_attacks_data_frame)


if __name__ == '__main__':
    run_process()
