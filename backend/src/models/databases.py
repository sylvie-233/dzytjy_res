from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///data.db"

# 数据库引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# sqlsession工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 数据库模型基类
DbModel = declarative_base()


# 依赖注入db session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# 创建所有表
def create_all_tables() -> None:
    from .filemodel import FileModel
    # 删表重建
    # metadata = MetaData()
    # metadata.reflect(bind=engine)
    # for table in metadata.tables.values():
    #     table.drop(engine)
        
    # 建表
    DbModel.metadata.create_all(engine)