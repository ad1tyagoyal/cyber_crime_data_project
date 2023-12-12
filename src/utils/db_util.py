import mysql.connector
import pandas as pd

from src.utils.logger_util import Log


class DatabaseManager(object):
    db_manager_instance = None
    db_conn_obj: mysql.connector.CMySQLConnection = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.db_manager_instance = super(DatabaseManager, cls).__new__(cls)
        return cls.db_manager_instance

    @staticmethod
    def get_instance():
        if not DatabaseManager.db_manager_instance:
            DatabaseManager.db_manager_instance = DatabaseManager()
        return DatabaseManager.db_manager_instance

    @staticmethod
    def establish_connection(db_args: dict[str, str]):
        DatabaseManager.db_conn_obj = mysql.connector.connect(**db_args)
        if DatabaseManager.db_conn_obj.is_connected():
            Log.get_instance().info_log('Successful in establishing connection with MySQL Workbench!')
        else:
            Log.get_instance().error_log('Failed in establishing connection with MySQL Workbench!')

    @staticmethod
    def make_schema(schema_name: str):
        Log.get_instance().info_log('Creating a new schema by name ' + schema_name + '...')
        cursor_obj = DatabaseManager.db_conn_obj.cursor()
        cursor_obj.execute('create database if not exists ' + schema_name)
        Log.get_instance().info_log('Created a new schema by name of ' + schema_name + '!')

    @staticmethod
    def upload_data(table_name: str, df: pd.DataFrame):
        cursor_obj = DatabaseManager.db_conn_obj.cursor()
        create_table_query: str = (f'create table if not exists {table_name} (year VARCHAR(100), states VARCHAR(100), '
                                   f'value VARCHAR(100))')
        cursor_obj.execute(create_table_query)
        insert_query: str = f'insert into {table_name} (year,states,value) values (%s, %s, %s)'
        for x in range(0, len(df.index)):
            values_dict: dict[str, str] = df.iloc[x]
            data_values: tuple[str, str, str] = (str(values_dict['year']), str(values_dict['states']),
                                                 str(values_dict['value']))
            cursor_obj.execute(insert_query, data_values)
            DatabaseManager.db_conn_obj.commit()

    @staticmethod
    def close_connection():
        DatabaseManager.db_conn_obj.close()
