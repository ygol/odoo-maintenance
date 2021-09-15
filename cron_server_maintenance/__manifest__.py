# Copyright 2016-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    'name': 'Cron Server Maintenance',
    'version': '14.0.1.0.0',
    'author': 'Vertelab',
    'license': 'AGPL-3',
    'category': 'category',
    'description': """
       This module adds server maintenance fields to maintenance equipments
    """,
    'depends': ['maintenance', 'maintenance_monitoring_status_extension'],
    'website': 'https://www.vertelab.com',
    'data': [
        'views/maintenance_view.xml',
        'data/cron.xml'
    ],
    'installable': True,
}
