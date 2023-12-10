import mysql.connector

from src.utils.logger_util import Log


class DatabaseManager(object):
    db_manager_instance = None
    db_conn_obj = None

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
