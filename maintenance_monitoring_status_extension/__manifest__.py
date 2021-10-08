# Copyright 2016-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    'name': 'Server Monitoring',
    'version': '14.0.1.0.0',
    'author': 'Vertelab',
    'license': 'AGPL-3',
    'category': 'category',
    'description': """
       This module is maintained from: https://github.com/vertelab/odoo-maintenance/

       
       Purpose of the module is to answer with a json object with the load/diskspace of the server which this database is on. To query the database you need to go to the /monitoring/status url.
       Url Syntax: http ://hostname/monitoring/status?db=databasename\n
       
       In order for the database to be able to answer without being logged in on you need to change the odoo.conf and add this "maintenance_montitoring_status" to the server_wide_modules.
    """,
    'depends': ['maintenance_monitoring_status'],
    'website': 'https://www.vertelab.com',
    'data': [
    ],
    'installable': True,
}
