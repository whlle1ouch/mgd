# -*- coding: utf-8 -*-

from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,DateTime,Float,and_,or_,text
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


def mssql(url, disconnect_interval=-1 , show_sql=False,encode='utf-8'):
    sql_url = quote_plus(url)
    return create_engine(sql_url, pool_recycle=disconnect_interval,echo=show_sql,encoding=encode)




class MsData(object):
    def __init__(self, engine):
        self.engine = engine
        self.metadata = MetaData()
        self.base = None
        self.reflect = False

    def auto_map(self,tables):
        if tables is not None or (not isinstance(tables,list)):
            print('<{}> is not the valid type'.format(tables))
            return None
        self.metadata.reflect(bind=self.engine,only=tables)
        self.base = automap_base(metadata=self.metadata)
        self.base.prepare()
        self.reflect = True

    def table(self, col):
        if self.reflect:
            return self.base.metadata.c.get(col,None)
        else:
            return None

class TableQuery(object):
    def __init__(self, table , engine , auto_refresh=True , auto_finish=False  , information =None):
        self.table = table
        self.setup()
        Session = sessionmaker(bind=engine , autoflush=auto_refresh , autocommit=auto_finish ,  info=information)
        session = Session()
        self.queryfunc = session.query

    def setup(self):
        if self.table:
           for table,tclass in self.table.c.items():
               setattr(self.table,table,tclass)

    def query(self,*entities, **kwargs):
        return self.queryfunc(*entities, **kwargs)




