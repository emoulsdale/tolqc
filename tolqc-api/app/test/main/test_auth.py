# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from . import BaseTestCase
from main.model import db


api_key = {"Authorization": "AnyThingBecAuseThIsIsATEST567890"}
false_api_key = {"Authorization": "IamAhacker"}


class TestAuthentication(BaseTestCase):
    def test_api_key_auth(self):
        db.engine.execute("ALTER SEQUENCE centre_id_seq RESTART WITH 1;")

        # no api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "name": "David",
                "hierarchy_name": "Hierarchy Tester"
            },
        )
        self.assert401(response)

        # incorrect api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "name": "David",
                "hierarchy_name": "Hierarchy Tester"
            },
            headers=false_api_key
        )
        self.assert401(response)

        # correct api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "name": "David",
                "hierarchy_name": "Hierarchy Tester"
            },
            headers=api_key
        )
        expect = {
            "data": {
              "type": "centre",
              "attributes": {
                "hierarchy_name": "Hierarchy Tester",
                "name": "David"
              },
              "id": 1
            }
        }
        self.assert200(response)
        self.assertEqual(expect, response.json)

        # GET data without api key
        response = self.client.open(
            '/api/v1/centres/1',
            method='GET',
        )
        expect = {
            "data": {
              "type": "centre",
              "attributes": {
                "hierarchy_name": "Hierarchy Tester",
                "name": "David"
              },
              "id": 1
            }
        }
        self.assert200(response)
        self.assertEqual(expect, response.json)

        # GET data with api key
        response = self.client.open(
            '/api/v1/centres/1',
            method='GET',
            headers=api_key
        )
        expect = {
            "data": {
              "type": "centre",
              "attributes": {
                "hierarchy_name": "Hierarchy Tester",
                "name": "David"
              },
              "id": 1
            }
        }
        self.assert200(response)
        self.assertEqual(expect, response.json)
