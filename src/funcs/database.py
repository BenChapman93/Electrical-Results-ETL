import sqlite3

class Database(object):
    
    DB_LOCATION = "/opt/airflow/database/results.db"

    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(Database.DB_LOCATION)
        self.cur = self.connection.cursor()

    def insert_parameters(self, new_data):
        """Insert a new row of data into the parameters table"""

        self.create_table()

        self.cur.execute('INSERT OR IGNORE INTO parameters VALUES (?, ?, ?, ?, ?, ?)' , new_data)

    def insert_summary(self, new_data):
        """Insert a new row of data into the summary_data table"""

        self.create_table()

        self.cur.execute('INSERT OR IGNORE INTO summary_data VALUES (?, ?, ?, ?, ?, ?, ?)' , new_data)

    def insert_raw(self, df):

        self.create_table()
        self.cur.execute('SELECT DISTINCT File FROM raw_data')
        result = self.cur.fetchall()
        existing_files = [file[0] for file in result]

        file = df['File'][0]

        if file not in existing_files:
            df.to_sql('raw_data', self.connection, index= False, if_exists= 'append')
        else:
            print(f'{file} already in the database.')

    def insert_metrics(self, metrics_df):

        self.create_table()
        self.cur.execute("SELECT name FROM PRAGMA_TABLE_INFO('metrics_data')")
        col_result = self.cur.fetchall()
        columns = [col[0] for col in col_result]

        metrics_df.columns = columns

        self.cur.execute('SELECT DISTINCT File FROM metrics_data')
        file_result = self.cur.fetchall()
        existing_files = [file[0] for file in file_result]

        file = metrics_df['File'][0]

        if file not in existing_files:
            metrics_df.to_sql('metrics_data', self.connection, index= False, if_exists= 'append')

        else:
            print(f'{file} already in database')


    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS raw_data (File text ,Time INTEGER, Channel_1 INTEGER, Channel_2 INTEGER, 
                                                    Channel_3 INTEGER, Channel_4 INTEGER, Channel_5 INTEGER, Channel_6 INTEGER, 
                                                    Channel_7 INTEGER, Channel_8 INTEGER, Channel_9 INTEGER, Channel_10 INTEGER, 
                                                    Channel_11 INTEGER, Channel_12 INTEGER, Channel_13 INTEGER, Channel_14 INTEGER, 
                                                    Channel_15 INTEGER, Channel_16 INTEGER, Channel_17 INTEGER, Channel_18 INTEGER, 
                                                    Channel_19 INTEGER , Channel_20 INTEGER)""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS metrics_data (File text, Channel INTEGER, Total_measurements INTEGER, 
                                                                        Initial_Reading INTEGER, Final_Reading INTEGER, Total_sub_Onehundred_MOhms INTEGER, 
                                                                        Total_sub_Ten_MOhms INTEGER, Total_sub_One_MOhms INTEGER, Max_consecutive_sub_One_MOhms_readings INTEGER, 
                                                                        Total_time_sub_One_MOhms INTEGER, Minimum_value INTEGER, Maximum_value INTEGER, Geomean_all_values INTEGER, 
                                                                        Geomean_last_four_values INTEGER, Geomean_first_four_values INTEGER, STDEV INTEGER)""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS summary_data (File text UNIQUE, Average INTEGER, Maximum INTEGER, Minimum INTEGER, 
                                                                    One_Mohms_passrate INTEGER, Ten_Mohms_passrate INTEGER, Onehundred_Mohms_passrate INTEGER) """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS parameters (File text UNIQUE, Total_Channels INTEGER, User text, Voltage INTEGER, duration INTEGER, Date text) """)


    def __enter__(self):
        return self
    
    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()