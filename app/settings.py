

from re import DEBUG


dbinfo={
    "type":"mysql",
    "driver":"pymysql",
    "host":"localhost",
    "port":3306,
    "user":"root",
    "pwd":"root",
    "dbname":"flask"
}

def get_db_uri(dbinfo):
    return "{}+{}://{}:{}@{}:{}/{}".format(dbinfo["type"],dbinfo["driver"],dbinfo["user"],dbinfo["pwd"],dbinfo["host"],dbinfo["port"],dbinfo["dbname"])

class Config:
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=get_db_uri(dbinfo)
    SECRET_KEY="djfjdkekfed"
    SQLALCHEMY_TRACK_MODIFICATIONS=False


envs={"develop":Config}
