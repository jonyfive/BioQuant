#!/usr/local/bin/python3
# ===============================
# Web app program:
# ----------------
# 0)MAIN: The main function.
# 1)View: Render index and login
# 2)Register: Register user 
# ===============================


# Misc---------------------------------------------------------------------
import os
# Flask--------------------------------------------------------------------
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from Classes import RegistrationForm 


# Starting flask
app = Flask(__name__)


# Function 1
@app.route('/')
def view():
	return render_template('view.html')

# Function 2
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        flash('Thanks for registering')
        # return redirect(url_for('login'))
        print(user)
    return render_template('register.html', form=form)


# MAIN==================================
if __name__ == '__main__':
	app.secret_key = 'secret'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)
# ======================================