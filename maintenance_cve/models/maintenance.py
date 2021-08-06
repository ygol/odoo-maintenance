# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2021  (<jakob@jakob-NUC8i5BEK>)
#    All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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

from odoo import models, fields, api, exceptions, _
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate

import logging
_logger = logging.getLogger(__name__)


class MaintenanceRequest(models.Model):
    _name = 'maintenance.request'
    _inherit = ['maintenance.request', 'website.seo.metadata', 'website.published.mixin']

    website_description = fields.Html('Website Maintenance Request Full Description', strip_style=True, translate=html_translate)
    website_short_description = fields.Text('Website Maintenance Request Short Description', translate=True)

    def _compute_website_url(self):
        super(MaintenanceRequest, self)._compute_website_url()
        for cve in self:
            cve.website_url = "/security/cve/%s" % slug(cve)

class MaintenanceTeam(models.Model):
    _inherit = 'maintenance.team'
    
    is_cve = fields.Boolean(string='Is CVE', default=False)
