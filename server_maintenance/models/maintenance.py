from odoo import models, fields, api, _


class Maintenance(models.Model):
    _inherit = 'maintenance.equipment'

    is_monitored = fields.Boolean(string="Is Monitored")
    monitor_url = fields.Char(string="Monitor URL")
    monitor_is_running = fields.Selection([('offline', 'Offline'), ('done', 'Running')], string='Monitor',
                                          default='offline', tracking=True)
    monitor_log = fields.Text(string="Log")
