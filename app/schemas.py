from pydantic import BaseModel

class Stock(BaseModel):
    ls_cd : str
    ls_dt : str
    barcode : str
    ex_dt : str
    ls_ct : int
    
    class Config:
        orm_mode = True  
        
class Deliver(BaseModel):
    ld_cd : str
    ld_dt : str
    barcode : str
    ex_dt : str
    ld_ct : int
    
    class Config:
        orm_mode = True
class Item(BaseModel):
    item_cd : str
    item_nm : str
    barcode : str
    use_yn : str
    
    class Config:
        orm_mode = True