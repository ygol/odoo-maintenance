# Copyright 2016-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)


{
    'name': 'Maintenance equipment monitoring',
    'version': '14.0.1.0.0',
    'author': 'Vertelab',
    'license': 'AGPL-3',
    'category': 'category',
    'description': """
       The purpose of this module is to monitor other odoo databases to see the status of their server. In order to query other databases the need 
       "maintenance_monitoring_status" or "maintenance_monitoring_status_extension" installed.
       
       In order to specify which database you want to monitor you fill the  Monitor URL field on the equipment view and there is  a ping button to trigger this query.
       The url needs to look like: http ://hostname/monitoring/status?db=databasename.
       
       There is also cron job called "Ping Remote Server" that will ping every 60 minutes to all equipment that has "Is Monitored" field set to true.
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
