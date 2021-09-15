from odoo import models, fields, api, _
import requests
import json


class Maintenance(models.Model):
    _inherit = 'maintenance.equipment'

    is_monitored = fields.Boolean(string="Is Monitored")
    monitor_url = fields.Char(string="Monitor URL")
    monitor_is_running = fields.Selection([('offline', 'Offline'), ('done', 'Running')], string='Monitor',
                                          default='offline', tracking=True)
    monitor_log = fields.Text(string="Log")

    def server_auto_sync(self):
        servers = self
        if not servers:
            servers = self.env[self._name].search([])
        for rec in servers:
            if rec.monitor_url and rec.is_monitored:
                ping_req = requests.get('http://%s/monitoring/status')
                if ping_req.status_code == 200:
                    response = json.loads(ping_req.content)
                    rec.monitor_log = response.space_availability
                    rec.monitor_is_running = 'done'



