# SPDX-FileCopyrightText: 2022 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.base import BaseTestCase


class TestRelationListGetEnum(BaseTestCase):
    def test_sort_by_J_on_enum_I(self):
        # add two I's 
        self.add_I(id=4857, name='fun')
        self.add_I(id=2384, name='also fun')

        # add two and three J's respectively
        self.add_J(id=29348, I='fun')
        self.add_J(id=587, I='fun')
        self.add_J(id=4857, I='also fun')
        self.add_J(id=23487, I='also fun')
        self.add_J(id=8394789, I='also fun')

        # sort by I ascending
        response = self.client.open(
            '/api/v1/J?sort_by=I',
            method='GET'
        )
        self.assert200(
            response,
            f'Response body is : {response.data.decode("utf-8")}'
        )
