from sqlmodel import Field, SQLModel
from enum import Enum
from typing import Optional

# Enum for Database Types
class DbType(Enum):
    POSTGRES = "postgres"
    MYSQL = "mysql"
    MSSQL = "msql"
    MONGO = "mongo"
    SQLITE = "sqlite"
    MARIA = "maria"

# Containers
class Container(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    container_name: str
    container_type: str
    network: Optional[str] = None
    bind_mount: Optional[str] = None
    config_files: Optional[str] = None

# Databases
class Database(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    database_name: str
    database_type: DbType
    version: Optional[str] = None
    primary_replica: Optional[str] = None
    container_id: int = Field(foreign_key="container.id")

# Backups
class Backup(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    container_id: int = Field(foreign_key="container.id")
    database_id: int = Field(foreign_key="database.id")
    backup_date: str
    backup_size: int
    backup_type: str

# Backup Policy
class BackupPolicy(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    container_id: int = Field(foreign_key="container.id")
    database_id: int = Field(foreign_key="database.id")
    policy_type: str
    frequency: str
    retention_period: int

# Rollbacks
class Rollback(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    backup_id: int = Field(foreign_key="backup.id")
    rollback_date: str
    rollback_reason: str
