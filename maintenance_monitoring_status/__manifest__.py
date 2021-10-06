# Copyright 2016-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    'name': 'Monitoring: Status',
    'version': '14.0.1.0.0',
    'author': 'Vertel.se',
    'license': 'AGPL-3',
    'category': 'category',
    'description': """
       This module is maintained from: https://github.com/vertelab/odoo-maintenance/ \n 
       until https://github.com/camptocamp/odoo-cloud-platform/tree/14.0/monitoring_status has lifted it.\n
       Inspired by Camptocamp SA.\n
       
       Purpose of this module is to answer with a json object the status of the database, on or off. To query the database you need to go to the /monitoring/status url.
       Url Syntax: http ://hostname/monitoring/status?db=databasename\n
       
       In order for the database to be able to answer without being logged in on you need to change the odoo.conf and add this module to the server_wide_modules.
    """,
    'depends': ['base', 'web'],
    'website': 'https://www.camptocamp.com',
    'data': [],
    'installable': True,
}
