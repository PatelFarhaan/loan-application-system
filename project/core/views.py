import datetime
from project import db
from project.models import Application
from flask import render_template, Blueprint, request


core_blueprint = Blueprint('core', __name__, template_folder='templates')

@core_blueprint.route('/loanapp', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form.get('phone', None)
        email = request.form.get('email', None)
        amount = request.form.get('amount', None)
        address = request.form.get('address', None)
        gender = request.form.get('gridRadios', None)
        dob = request.form.get('date_of_birth', None)
        last_name = request.form.get('last_name', None)
        first_name = request.form.get('first_name', None)
        attachment = request.files.get('attachment', None)
        reason_text = request.form.get('reason_text', None)
        middle_name = request.form.get('middle_name', None)

        if email is None or email == '':
            return render_template('loanapp.html', warning='Email cannot be Empty')

        if first_name is None or first_name == '':
            return render_template('loanapp.html', warning='First name cannot be Empty')

        if last_name is None or last_name == '':
            return render_template('loanapp.html', warning='Last name cannot be Empty')

        if phone is None or phone == '':
            return render_template('loanapp.html', warning='Phone number cannot be Empty')

        if amount is None or amount == '':
            return render_template('loanapp.html', warning='Amount cannot be Empty')

        if address is None or address == '':
            return render_template('loanapp.html', warning='Address cannot be Empty')

        if reason_text is None or reason_text == '':
            return render_template('loanapp.html', warning='Reason cannot be Empty')

        if gender is None:
            return render_template('loanapp.html', warning='Gender cannot be Empty')

        if dob is None or dob == '':
            return render_template('loanapp.html', warning='Date of Birth cannot be Empty')

        new_appl_obj = Application(email=email,
                                   gender=gender,
                                   amount=amount,
                                   telephone=phone,
                                   address=address,
                                   last_name=last_name,
                                   purpose=reason_text,
                                   first_name=first_name,
                                   middle_name=middle_name,
                                   dob=datetime.datetime.strptime(dob, '%m/%d/%Y'))
        db.session.add(new_appl_obj)
        db.session.commit()

        # Can use S3 object storage for storing application file
    return render_template('loanapp.html')