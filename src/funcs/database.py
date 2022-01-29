import sqlite3

class Database(object):
    
    DB_LOCATION = "dummy.db"

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

        self.cur.execute('SELECT DISTINCT File FROM raw_data')
        result = self.cur.fetchall()

        return result

    def create_table(self):
        """create a database table if it does not exist already"""
        self.cur.execute("""CREATE TABLE IF NOT EXISTS raw_data (File text ,Time number, Channel_1 number, Channel_2 number, 
                                                    Channel_3 number, Channel_4 number, Channel_5 number, Channel_6 number, 
                                                    Channel_7 number, Channel_8 number, Channel_9 number, Channel_10 number, 
                                                    Channel_11 number, Channel_12 number, Channel_13 number, Channel_14 number, 
                                                    Channel_15 number, Channel_16 number, Channel_17 number, Channel_18 number, 
                                                    Channel_19 number , Channel_20 number)""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS metrics_data (File text, Channel number, Total_measurements number, 
                                                                        Initial_Reading number, Final_Reading number, Total_sub_Onehundred_MOhms number, 
                                                                        Total_sub_Ten_MOhms number, Total_sub_One_MOhms number, Max_consecutive_sub_One_MOhms_readings number, 
                                                                        Total_time_sub_One_MOhms number, Minimum_value number, Maximum_value number, Geomean_all_values number, 
                                                                        Geomean_last_four_values number, Geomean_first_four_values number, STDEV number)""")

        self.cur.execute("""CREATE TABLE IF NOT EXISTS summary_data (File text UNIQUE, Average number, Maximum number, Minimum number, 
                                                                    One_Mohms_passrate number, Ten_Mohms_passrate number, Onehundred_Mohms_passrate number) """)

        self.cur.execute("""CREATE TABLE IF NOT EXISTS parameters (File text UNIQUE, Total_Channels number, User text, Voltage number, duration number, Date text) """)


    def __enter__(self):
        return self
    
    def __exit__(self, ext_type, exc_value, traceback):
        self.cur.close()
        if isinstance(exc_value, Exception):
            self.connection.rollback()
        else:
            self.connection.commit()
        self.connection.close()