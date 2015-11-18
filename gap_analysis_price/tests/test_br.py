# -*- coding: utf-8 -*-
# © <YEAR(2015)>
# <Elico Corp, contributor: Eric Caudal, Alex Duan, Xie XiaoPeng(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openerp.tests import common


@common.at_install(False)
@common.post_install(True)
class BusinessRequirementTestCase(common.TransactionCase):
    def setUp(self):
        super(BusinessRequirementTestCase, self).setUp()
        self.br = self.env['business.requirement']

    def test_get_estimated_cost_total(self):
        vals = {
            'name': ' test',
            'draft_estimation_lines': [
                (
                    0, 0,
                    {
                        'name': 'line1', 'estimated_time': 15, 'unit_price': 1,
                    }
                ),
                (
                    0, 0,
                    {
                        'name': 'line1', 'estimated_time': 25, 'unit_price': 1,
                    }
                ),
                (
                    0, 0,
                    {
                        'name': 'line1', 'estimated_time': 35, 'unit_price': 1,
                    }
                ),
                (
                    0, 0,
                    {
                        'name': 'line1', 'estimated_time': 45, 'unit_price': 1,
                    }
                ),
            ]
        }
        br = self.br.create(vals)
        cost_total = br.estimated_cost_total
        self.assertEqual(cost_total, 15 + 25 + 35 + 45)
