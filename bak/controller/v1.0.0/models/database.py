from sqlmodel import Field, SQLModel
from enum import Enum

class DbType(Enum):
    Postgres = "postgres"
    MySQL = "mysql"
    MSSQL = "mssql"
    Mongo = "monogo"
    Sqlite = "slqite"
    Maria = "maria"

    def IsDbType(dbtype: str) -> bool:
        return dbtype in DbType._value2member_map_

class Database(SQLModel, table=True):
    db_id: int = Field(primary_key=True)
    type: DbType
    port: int
    user: str   
    password: str