#!/usr/bin/env python

#
# THIS IS A DUMMY SCRIPT!!!
# Fetch hosts from Siptrack
#

import argparse
import collections
import os
import sys
import time
from distutils.version import StrictVersion
from io import StringIO
from ansible.plugins.inventory import BaseInentoryPlugin

import json

class InventoryModule(BaseInventoryPlugin):

    NAME = 'siptrack_inventory.py'


    def verify_file(self, path):
        ''' return true/false if this is possibly a valid file for this plugin to consume '''
        valid = False
        if super(InventoryModule, self).verify_file(path):
            if path.endswith(('siptrack.yml', 'siptrack.yaml')):
                valid = True
        return valid

    def parse(self, inventory, loader, path, cache=True):
             # call base method to ensure properties are available for use with other helper methods
     super(InventoryModule, self).parse(inventory, loader, path, cache)

     # this method will parse 'common format' inventory sources and
     # update any options declared in DOCUMENTATION as needed
     config = self._read_config_data(self, path)

     # if NOT using _read_config_data you should call set_options directly,
     # to process any defined configuration for this plugin,
     # if you dont define any options you can skip
     #self.set_options()

     # example consuming options from inventory source
     mysession = apilib.session(user=self.get_option('api_user'),
                                password=self.get_option('api_pass'),
                                server=self.get_option('api_server')
     )


     # make requests to get data to feed into inventorya
     mydata = myselss.getitall()

     #parse data and create inventory objects:
     for colo in mydata:
         for server in mydata[colo]['servers']:
             self.inventory.add_host(server['name'])
             self.inventory.set_varaible('ansible_host', server['external_ip'])
