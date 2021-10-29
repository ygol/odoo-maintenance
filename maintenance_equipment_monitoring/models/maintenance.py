from odoo import models, fields, api, _
import requests
import json
from datetime import datetime


class Maintenance(models.Model):
    _inherit = 'maintenance.equipment'

    is_monitored = fields.Boolean(string="Is Monitored")
    monitor_url = fields.Char(string="Monitor URL")
    monitor_is_running = fields.Selection([('offline', 'Offline'), ('done', 'Running')], string='Monitor',
                                          default='offline', tracking=True)
    monitor_log_ids = fields.One2many('maintenance.equipment.server.log', 'maintenance_id', string="Logs",
                                      readonly=True)

    def server_auto_sync(self):
        servers = self
        if not servers:
            servers = self.env[self._name].search([])
        for rec in servers:
            if rec.monitor_url and rec.is_monitored:
                try:
                    ping_req = requests.get(rec.monitor_url)
                    if ping_req.status_code == 200:
                        response = json.loads(ping_req.content)
                        self.env['maintenance.equipment.server.log'].sudo().create({
                            'date': datetime.now(),
                            'monitor_log': response,
                            'maintenance_id': self.id
                        })
                        rec.monitor_is_running = 'done'
                    else:
                        rec.monitor_is_running = 'offline'
                except Exception:
                    # requests.get will raise errors in some cases when
                    # it can't connect.
                    rec.monitor_is_running = 'offline'

class MaintenanceLog(models.Model):
    _name = 'maintenance.equipment.server.log'
    _rec_name = 'date'

    date = fields.Datetime(string="Date")
    monitor_log = fields.Html(string="Log")
    maintenance_id = fields.Many2one('maintenance.equipment', string="Maintenance")
