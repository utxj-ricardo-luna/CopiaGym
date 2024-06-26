from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import meta,engine
from sqlalchemy.sql import func

users = Table("users", meta,
                 Column("id", Integer, primary_key=True),
                 Column("usuario", String(255)),
                 Column("password",String(255)),
                 Column("created_at", DateTime(timezone=True), default=func.now()),
                 Column("estatus", Boolean(False)),
                 Column("Id_persona", Integer)
                 )

meta.create_all(engine)