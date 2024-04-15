from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary sample employee list
employees = [{'id': 0, 'name': 'John Doe', 'address': '123 Main St', 'phone_number': '555-1234', 'salary': 50000},
             {'id': 1, 'name': 'Jane Smith', 'address': '456 Elm St', 'phone_number': '555-5678', 'salary': 60000}]

# Define routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        phone_number = request.form['phone_number']
        salary = request.form['salary']
        employees.append({'id': len(employees), 'name': name, 'address': address, 'phone_number': phone_number, 'salary': salary})
        return redirect(url_for('view_employees'))
    return render_template('add_employee.html')


@app.route('/view')
def view_employees():
    return render_template('view_employees.html', employees=employees)


@app.route('/update', methods=['GET', 'POST'])
def update_employee():
    if request.method == 'POST':
        name = request.form['name']
        new_address = request.form['new_address']
        new_phone_number = request.form['new_phone_number']
        new_salary = request.form['new_salary']

        # Find the employee with the given name and update their information
        for employee in employees:
            if employee['name'] == name:
                employee['address'] = new_address
                employee['phone_number'] = new_phone_number
                employee['salary'] = int(new_salary)
                break

        return redirect(url_for('view_employees'))

    return render_template('update_employee.html')


@app.route('/delete', methods=['GET', 'POST'])
def delete_employee():
    if request.method == 'POST':
        name_to_delete = request.form['name']
        employee_found = False
        for employee in employees:
            if employee['name'] == name_to_delete:
                employees.remove(employee)
                employee_found = True
                break
        if employee_found:
            return redirect('/view')
        else:
            return "Employee not found"
    else:
        return render_template('delete_employee.html')


if __name__ == '__main__':
    app.run(debug=True)
