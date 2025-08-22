from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Employee
from .services import list_employees, create_employee, update_employee, delete_employee

bp = Blueprint("employees", __name__, template_folder="templates")


@bp.get("/")
def index():
    q = request.args.get("q", "").strip() or None
    page = int(request.args.get("page", 1))
    pagination = list_employees(q=q, page=page, per_page=10)
    return render_template("employees/index.html", pagination=pagination, q=q)


@bp.get("/new")
def new():
    return render_template("employees/new.html")


@bp.post("/")
def create():
    name = (request.form.get("name") or "").strip()
    if not name:
        flash("Name is required.", "danger")
        return redirect(url_for("employees.new"))
    data = {
        "name": name,
        "phone": request.form.get("phone", "").strip(),
        "address": request.form.get("address", "").strip(),
        "salary": float(request.form.get("salary") or 0),
    }
    create_employee(data)
    flash("Employee created.", "success")
    return redirect(url_for("employees.index"))


@bp.get("/<int:emp_id>/edit")
def edit(emp_id):
    emp = Employee.query.get_or_404(emp_id)
    return render_template("employees/edit.html", emp=emp)


@bp.post("/<int:emp_id>")
def update(emp_id):
    emp = Employee.query.get_or_404(emp_id)
    name = (request.form.get("name") or "").strip()
    if not name:
        flash("Name is required.", "danger")
        return redirect(url_for("employees.edit", emp_id=emp.id))
    data = {
        "name": name,
        "phone": request.form.get("phone", "").strip(),
        "address": request.form.get("address", "").strip(),
        "salary": float(request.form.get("salary") or 0),
    }
    update_employee(emp, data)
    flash("Employee updated.", "success")
    return redirect(url_for("employees.index"))


@bp.post("/<int:emp_id>/delete")
def destroy(emp_id):
    emp = Employee.query.get_or_404(emp_id)
    delete_employee(emp)
    flash("Employee deleted.", "info")
    return redirect(url_for("employees.index"))
