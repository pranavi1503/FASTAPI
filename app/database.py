from sqlalchemy import create_engine

def database_connection():
    server = "DESKTOP-RM4N23G\\SQLEXPRESS02"
    database = "bluhealth"
    connection_string = (
        f"mssql+pyodbc://@{server}/{database}"
        f"?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )
    engine = create_engine(connection_string)
    return engine
