# Copyright 2016-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    'name': 'Maintenance equipment monitoring',
    'version': '14.0.1.0.0',
    'author': 'Vertelab',
    'license': 'AGPL-3',
    'category': 'category',
    'description': """
       This module adds server maintenance fields to maintenance equipments and also a cron job
       This done in order to monitor other odoo servers that has the "maintenance_monitoring_status" or "maintenance_equipment_monitoring_extension" module installed.
       To query a another odoo server use a url like "http :// hostname/monitoring/status?db=databasename".
    """,
    'depends': ['maintenance', 'maintenance_monitoring_status_extension'],
    'website': 'https://www.vertelab.com',
    'data': [
        'security/ir.model.access.csv',
        'views/maintenance_view.xml',
        'data/cron.xml'
    ],
    'installable': True,
}
