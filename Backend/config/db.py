from sqlalchemy import create_engine, MetaData
engine  = create_engine("mysql+pymsql://root:password@localhost:3306/test.db")

meta = MetaData()

conn = engine.connect()