from sqlalchemy.orm import Session
import models, schemas

# stock table insert
def create_stock(db : Session, stock : schemas.Stock):
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

# stock table select
def get_stocks(db : Session, period_front: str, period_back:str):
    return db.query(models.Stock).filter(models.Stock.ls_dt.between(period_front, period_back)).all()


# item table insert
def create_item(db : Session, item : schemas.Item):
    db_item = models.Item(
        item_cd = item.item_cd,
        item_nm = item.item_nm,
        item_cat_nm = item.item_cat_nm,
        item_maker = item.item_maker
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# item table select
def get_items(db : Session, item_cd:str):
    if item_cd == None:
        return db.query(models.Item).all()
    else:
        return db.query(models.Item).filter(models.Item.item_cd == item_cd).all()

def get_ex_date(db : Session, today:str, ex_date : str):
    return db.query(models.Stock).filter(models.Stock.ex_dt.between(today, ex_date)).order_by(models.Stock.ex_dt).all()