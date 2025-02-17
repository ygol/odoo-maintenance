# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo SA, Open Source Management Solution, third party addon
#    Copyright (C) 2021- Vertel AB (<https://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

# Copyright 2016-2018 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Maintenance: Server Monitoring',
    'summary': 'To answer with a json object with the load/diskspace of the server.',
    'author': 'Vertel AB',
    'contributor': 'Mitchell Admin',
    'maintainer': 'Vertel AB',
    'repository': 'https://github.com/vertelab/odoo-maintenance.git',
    'category': 'Tools',
    'version': '14.0.1.0.0',
    # Version ledger: 14.0 = Odoo version. 1 = Major. Non regressionable code. 2 = Minor. New features that are regressionable. 3 = Bug fixes
    'license': 'AGPL-3',
    'website': 'https://vertel.se/apps/odoo-maintenance/maintenance_monitoring_status_extension',
    'description': """
       This module is maintained from: https://github.com/vertelab/odoo-maintenance/

       
       Purpose of the module is to answer with a json object with the load/diskspace of the server which this database is on. To query the database you need to go to the /monitoring/status url.
       Url Syntax: http ://hostname/monitoring/status?db=databasename\n
       
       In order for the database to be able to answer without being logged in on you need to change the odoo.conf and add this "maintenance_montitoring_status" to the server_wide_modules.
    """,
    'depends': ['maintenance_monitoring_status'],
    'data': [
    ],
    'installable': True,
}
