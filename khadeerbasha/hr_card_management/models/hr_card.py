from odoo import fields, api, _, models
from odoo.exceptions import Warning
import logging
import math
from datetime import timedelta
from werkzeug import url_encode

from odoo import api, fields, models
from odoo.exceptions import UserError, AccessError, ValidationError
from openerp.tools import float_compare
from odoo.tools.translate import _
from datetime import timedelta
from werkzeug import url_encode

from odoo import api, fields, models
from odoo.exceptions import UserError, AccessError, ValidationError
from openerp.tools import float_compare
from odoo.tools.translate import _
from openerp import models, fields, api
from openerp.exceptions import except_orm, Warning, RedirectWarning
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from openerp import models, fields, api
from openerp.exceptions import except_orm, Warning, RedirectWarning
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
import time

class hr_employee(models.Model):
    _inherit = 'hr.employee'
    
    iqama_no = fields.Char('Iqama No.')
    iqama_location = fields.Char('Iqama Release Place')
    iqama_start_date = fields.Date(string="Iqama Date")
    iqama_expiry_date = fields.Date(string="Iqama Expiry Date")
    iqama_note = fields.Char('Note')
    
    passport_no = fields.Char('Passport No.')
    passport_location = fields.Char('Passport Release Place')
    passport_start_date = fields.Date(string="Passport Date")
    passport_expiry_date = fields.Date(string="Passport Expiry Date")
    passport_note = fields.Char('Note')
    
    driving_no = fields.Char('Driving License No.')
    driving_location = fields.Char('License Release Place')
    driving_start_date = fields.Date(string="Driving License Date")
    driving_expiry_date = fields.Date(string="License Expiry Date")
    driving_note = fields.Char('Note')
    
    car_no = fields.Char('Car Insurance No.')
    car_location = fields.Char('Car Insurance Place')
    car_start_date = fields.Date(string="Car Insurance Date")
    car_expiry_date = fields.Date(string="Car Insurance Expiry Date")
    car_note = fields.Char('Note')
    
    medical_no = fields.Char('Medical ID No.')
    medical_location = fields.Char('Medical ID Place')
    medical_start_date = fields.Date(string="Medical ID Date")
    medical_expiry_date = fields.Date(string="Medical ID Expiry Date")
    medical_note = fields.Char('Note')
    
    permit_no = fields.Char('Work Permit No.')
    permit_location = fields.Char('Work Permit Place')
    permit_start_date = fields.Date(string="Work Permit Date")
    permit_expiry_date = fields.Date(string="Permit Expiry Date")
    permit_note = fields.Char('Note')
    
    aramco_no = fields.Char('Aramco Card No.')
    aramco_location = fields.Char('Place')
    aramco_start_date = fields.Date(string="Aramco Card Date")
    aramco_expiry_date = fields.Date(string="Aramco Card Expiry Date")
    aramco_note = fields.Char('Note')
    
    
