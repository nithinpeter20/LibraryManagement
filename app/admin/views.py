# Views for admin blueprint
"""
admin/views.py
~~~~~~~~~~~~~~
Script for admin view
"""

### Libraries
# Local imports
from . import admin
from ..auth import views 

# Third-party libraries
from flask import render_template
from flask import request
from flask import flash
from flask import abort
from flask import redirect
from flask import url_for
from flask_login import current_user
from flask_login import login_required,login_user, logout_user

@admin.route('/')
@login_required
def adminpage():
    """
    To render admin-base html page 
    """
    if not current_user.is_admin:
        abort(403)
    return render_template('admin-base.html', title='Admin')


@admin.route('/admin-books', methods=['GET', 'POST'])
def admin_books():
    """
    To render admin-books html page
    """
    return render_template('admin-books.html')

@admin.route('/admin-authors', methods=['GET', 'POST'])
def admin_authors():
    """
    To render admin-authors html page
    """
    return render_template('admin-authors.html')

@admin.route('/lend-request', methods=['GET', 'POST'])
def lend_request():
    """
    To render admin-lend html page
    """
    return render_template('admin-lend.html')

@admin.route('/return-request', methods=['GET', 'POST'])
def return_request():
    """
    To render admin-return html page
    """
    return render_template('admin-return.html')