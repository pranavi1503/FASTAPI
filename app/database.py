from sqlalchemy import create_engine

def database_connection():
    username="sql12794950"
    password="ynVgE6zW8l"
    host="sql12.freesqldatabase.com"
    port=3306
    database = "sql12794950"
    connection_string = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_string)
    return engine
