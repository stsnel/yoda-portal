#!/usr/bin/env python3

__copyright__ = 'Copyright (c) 2021, Utrecht University'
__license__ = 'GPLv3, see LICENSE'

from flask import Blueprint, redirect, render_template, request, url_for

import api

deposit_bp = Blueprint('deposit_bp', __name__,
                       template_folder='templates',
                       static_folder='static/deposit',
                       static_url_path='/assets')

"""
    0 Deposit overview: /deposit/
    1. Add data:        /deposit/data/
    2. Document data:   /deposit/metadata/
    3. Submit data:     /deposit/submit/
    4. Thank you:       /deposit/thankyou/
"""


def create_new_deposit():
    """Creates a new deposit folder."""
    response = api.call('deposit_create')
    path = "/" + response['data']['deposit_path']
    return path.replace('//', '/')


@deposit_bp.route('/')
@deposit_bp.route('/browse')
def index():
    """Deposit overview"""
    path = "/deposit-pilot"
    return render_template('deposit/overview.html',
                           activeModule='deposit',
                           items=25,
                           dir=path)


@deposit_bp.route('/data')
def data():
    """Step 1: Add data"""
    path = request.args.get('dir', None)
    if path is None:
        path = create_new_deposit()
    return render_template('deposit/data.html',
                           activeModule='deposit',
                           items=25,
                           dir=path)


@deposit_bp.route('/metadata')
def metadata():
    """Step 2: Document data"""
    path = request.args.get('dir', None)
    if path is None:
        return redirect(url_for('deposit_bp.index'))
    return render_template('deposit/metadata-form.html', path=path)


@deposit_bp.route('/submit')
def submit():
    """Step 3: Submit data"""
    path = request.args.get('dir', None)
    if path is None:
        return redirect(url_for('deposit_bp.index'))
    return render_template('deposit/submit.html', path=path)


@deposit_bp.route('/thank-you')
def thankyou():
    """Step 4: Thank you"""
    return render_template('deposit/thank-you.html')
