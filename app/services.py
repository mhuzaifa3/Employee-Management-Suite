from . import db
from .models import Employee


def list_employees(q=None, page=1, per_page=10):
    query = Employee.query
    if q:
        like = f"%{q}%"
        query = query.filter((Employee.name.ilike(like)) | (Employee.phone.ilike(like)))
    return query.order_by(Employee.id.desc()).paginate(page=page, per_page=per_page, error_out=False)


def create_employee(data):
    emp = Employee(**data)
    db.session.add(emp)
    db.session.commit()
    return emp


def update_employee(emp, data):
    for k, v in data.items():
        setattr(emp, k, v)
    db.session.commit()
    return emp


def delete_employee(emp):
    db.session.delete(emp)
    db.session.commit()
