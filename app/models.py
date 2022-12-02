from sqlalchemy import Column, Integer, String
from database import Base

class Stock(Base):
    '''
    입고일자, 유효기간, 바코드 번호, 수량
    '''
    __tablename__ = "stock"
    
    ls_cd = Column(String(26), primary_key=True)
    ls_dt = Column(String(10))
    barcode = Column(String(13))
    ex_dt = Column(String(10))
    ls_ct = Column(Integer)
    
class Item(Base):
    __tablename__ = "item"
    
    item_cd = Column(String(50), primary_key=True)
    item_nm = Column(String(100))
    barcode = Column(String(13))
    use_yn = Column(String(1))
    
class Deliver(Base):
    __tablename__ = "deliver"
    
    ld_cd = Column(String(26), primary_key=True)
    ld_dt = Column(String(10))
    barcode = Column(String(13))
    ex_dt = Column(String(10))
    ld_ct = Column(Integer)
     
    
    