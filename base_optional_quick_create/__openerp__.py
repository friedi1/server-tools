# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2013 Agile Business Group sagl (<http://www.agilebg.com>)
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

{
    'name': "Optional quick create",
    'version': '0.1',
    'category': 'Tools',
    'summary': "Avoid 'quick create' on m2o fields, on a 'by model' basis",
    'description': """
This module allows to avoid to *quick create* new records, through many2one
fields, for a specific model.
You can configure which models should allow *quick create*.
When specified, the *quick create* option will always open the standard create
form.

Got the idea from https://twitter.com/nbessi/status/337869826028605441
""",
    'author': 'Agile Business Group',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": ['base'],
    "data": [
        'model_view.xml',
    ],
    "demo": [],
    'test': [],
    "installable": True
}