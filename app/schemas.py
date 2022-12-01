from pydantic import BaseModel

class Stock(BaseModel):
    ls_cd : str
    ls_dt : str
    barcode : str
    ex_dt : str
    ls_ct : int
    
    class Config:
        orm_mode = True