# -*- coding: utf-8 -*-

# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""
test_bifrost
----------------------------------

Tests for `bifrost` module.
"""

from bifrost import inventory
from bifrost.tests import base


class TestBifrostInventory(base.TestCase):

    def test_inventory_preparation(self):
        (groups, hostvars) = inventory._prepare_inventory()
        self.assertIn("baremetal", groups)
        self.assertIn("localhost", groups)
        self.assertDictEqual(hostvars, {})
        localhost_value = dict(hosts=["127.0.0.1"])
        self.assertDictEqual(groups['localhost'], localhost_value)

    def test__val_or_none(self):
        array = ['no', '', 'yes']
        self.assertEqual(inventory._val_or_none(array, 0), 'no')
        self.assertEqual(inventory._val_or_none(array, 1), None)
        self.assertEqual(inventory._val_or_none(array, 2), 'yes')
        self.assertEqual(inventory._val_or_none(array, 4), None)