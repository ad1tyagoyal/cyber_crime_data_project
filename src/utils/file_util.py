import os
import pandas as pd
from pathlib import Path

from src.utils.logger_util import Log


def read_csv_file_as_df(file_path: str) -> pd.DataFrame:
    file: Path = Path(file_path)
    if not file.is_file():
        Log.get_instance().error_log('No file exists at location ' + str(file))
        return pd.DataFrame()
    Log.get_instance().info_log('Reading file at location ' + str(file))
    cyber_crime_df: pd.DataFrame = pd.read_csv(file_path, delimiter=',')
    return cyber_crime_df
