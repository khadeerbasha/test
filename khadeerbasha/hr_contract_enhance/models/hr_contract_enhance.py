from odoo import fields, models, api, _
from odoo.addons import decimal_precision as dp
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval
from odoo.tools import float_is_zero, float_compare
from odoo.addons import decimal_precision as dp
import time
from datetime import datetime, timedelta
from dateutil import relativedelta
from datetime import datetime
import babel
import datetime
from dateutil.relativedelta import relativedelta
import time
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.addons import decimal_precision as dp

import datetime
from dateutil.relativedelta import relativedelta
import time

import time
from datetime import datetime, timedelta
from dateutil import relativedelta
import babel


class hr_contract(models.Model):

    _inherit = "hr.contract"


    vacation = fields.Float('Annual Vacation Days', required=True)
    ticket = fields.Float('Eligible Employee Tickets', required=True)
    ticket_amount = fields.Float('Amount per Ticket', required=True)
    contract_years = fields.Integer('No of Years Contract', required=True)
    total_salary = fields.Float('Total Salary', required=True)
    gosiwage = fields.Float('Gosi Wage', required=True)
hr_contract()


