import pyodbc
import pandas as pd



class Database():
    def __init__(self,db):

        cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=DESKTOP-HTVOO3A;"
            f"Database={db};"
            "Trusted_Connection=yes;")

        self.cnxn = pyodbc.connect(cnxn_str) 
        self.cursor = self.cnxn.cursor()
        self.cursor.execute("""IF  NOT EXISTS (SELECT * FROM sys.objects 
                                    WHERE object_id = OBJECT_ID(N'[dbo].[Daily]') AND type in (N'U'))

                                BEGIN
                                        CREATE TABLE [dbo].[Daily](
                                            id INT IDENTITY NOT NULL PRIMARY KEY,
                                            start_at DATETIME DEFAULT GETDATE() NOT NULL,
                                            end_at_date DATE DEFAULT GETDATE() NOT NULL,
                                            end_at_time TIME (0) NOT NULL,
                                            labels NVARCHAR(MAX) NOT NULL,
                                            descriptions NVARCHAR(MAX),
                                        ) 

                                END
                            """)
        self.cnxn.commit()                    
    def fetch(self):

        self.cursor.execute("SELECT * FROM Daily")
        rows = self.cursor.fetchall()
        return rows
    def insert(self,end_at_date,end_at_time,labels,descriptions):

        self.cursor.execute(" INSERT INTO Daily(end_at_date,end_at_time,labels,descriptions) VALUES(?,?,?,?)",
        (end_at_date,end_at_time,labels,descriptions))
        self.cnxn.commit()
    def remove(self,id):

        self.cursor.execute("DELETE FROM Daily WHERE id=? ",(id,))
        self.cnxn.commit()
    def update(self,id,start_at,end_at_date,end_at_time,labels,descriptions):

        self.cursor.execute("""UPDATE Daily SET start_at = ? ,end_at_date = ?,
                               end_at_time = ?,labels = ?,
                               descriptions = ? WHERE id = ? """,
                               (start_at,end_at_date,end_at_time,labels,descriptions,id))
        self.cnxn.commit()
    def __del__(self):
        
        self.cnxn.close()


db = Database('ToDo')

db.insert('2021-06-11','12:03','سلام','ریاضی ۲')
db.insert('2021-06-11','12:03','سلام۳','ریاضی ۳')
db.insert('2021-06-11','12:03','سلام۴','ریاضی ۴')