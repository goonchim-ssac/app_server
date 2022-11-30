from sqlalchemy.orm import Session
import models, schemas

def create_stock(db : Session, stock : schemas.CreateStock):
    db_stock = models.Stock(
        ls_cd = stock.ls_cd,
        ls_dt = stock.ls_dt,
        barcode = stock.barcode,
        ex_dt = stock.ex_dt,
        ls_ct = stock.ls_ct
        )
    db.add(db_stock)
    db.commit()
    db.refresh(db_stock)
    return db_stock