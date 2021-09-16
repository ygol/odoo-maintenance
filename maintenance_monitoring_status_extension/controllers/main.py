import logging
import json
from odoo import models, api, _, http

import werkzeug
import os
from odoo.addons.monitoring_status.controllers.main import Monitoring
from datetime import datetime


class ServerMonitoring(Monitoring):

    def get_status(self):
        info = {'status': 1}
        info.update({
            'ping_date': str(datetime.now()),
            'space_availability': os.popen('df -h').read(),
            'load': os.popen('cat /proc/loadavg ; top').read()
        })
        return info

