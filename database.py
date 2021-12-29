from dotenv import load_dotenv
load_dotenv()
from app.models import Menu, MenuItem, MenuItemType, Table
# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee


with app.app_context():
    db.drop_all()
    db.create_all()

    employee = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee)
    db.session.commit()

    beverages = MenuItemType(name="Beverages")
    entrees = MenuItemType(name="Entrees")
    sides = MenuItemType(name="Sides")

    dinner = Menu(name="Dinner")

    fries = MenuItem(name="French fries", price=3.50, menu_item_types=sides, menus=dinner)
    drp = MenuItem(name="Dr. Pepper", price=1.0, menu_item_types=beverages, menus=dinner)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, menu_item_types=entrees, menus=dinner)
    db.session.add_all([dinner, beverages, entrees, sides, fries, drp, jambalaya])
    db.session.commit()

    table1 = Table(number=1, capacity=6)
    table2 = Table(number=2, capacity=4)
    table3 = Table(number=3, capacity=8)
    table4 = Table(number=4, capacity=2)
    table5 = Table(number=5, capacity=6)
    table6 = Table(number=6, capacity=4)
    table7 = Table(number=7, capacity=8)
    table8 = Table(number=8, capacity=2)
    table9 = Table(number=9, capacity=6)
    table10 = Table(number=10, capacity=6)
    db.session.add_all([table1,table2, table3, table4, table5, table6, table7, table8, table9, table10])
    db.session.commit()
