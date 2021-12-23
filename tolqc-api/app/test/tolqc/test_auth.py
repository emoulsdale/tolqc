# SPDX-FileCopyrightText: 2021 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from test.tolqc import TolqcTestCase
from main.model import db


class TestAuthentication(TolqcTestCase):
    def test_api_key_auth(self):
        db.engine.execute("ALTER SEQUENCE centre_id_seq RESTART WITH 1;")

        good_api_key = {"Authorization": self.api_key}
        false_api_key = {"Authorization": "IamAhacker"}

        # no api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "data": {
                    "type": "centres",
                    "attributes": {
                        "name": "David",
                        "hierarchy_name": "Hierarchy Tester"
                    }
                },
            }
        )
        self.assert401(response)

        # incorrect api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "data": {
                    "type": "centres",
                    "attributes": {
                        "name": "David",
                        "hierarchy_name": "Hierarchy Tester"
                    }
                },
            },
            headers=false_api_key
        )
        self.assert401(response)

        # correct api key
        response = self.client.open(
            '/api/v1/centres',
            method='POST',
            json={
                "data": {
                    "type": "centres",
                    "attributes": {
                        "name": "David",
                        "hierarchy_name": "Hierarchy Tester"
                    }
                },
            },
            headers=good_api_key
        )
        self.assert201(response)
        expect_data = {
            "data": {
                "type": "centres",
                "attributes": {
                    "hierarchy_name": "Hierarchy Tester",
                    "name": "David",
                    "created_at": response.json['data']['attributes']['created_at'],
                },
                "id": response.json['data']['id'],
                "relationships": {
                    "creator": {
                        "data": {
                            "id": "100",
                            "type": "user"
                        },
                        "links": {
                            "related": "/user/100"
                        }
                    }
                }
            }
        }
        self.assertEqual(expect_data, response.json)

        # GET data without api key
        response = self.client.open(
            '/api/v1/centres/1',
            method='GET',
        )
        self.assert200(response)
        self.assertEqual(expect_data, response.json)

        # GET data with api key
        response = self.client.open(
            '/api/v1/centres/1',
            method='GET',
            headers=good_api_key
        )
        self.assert200(response)
        self.assertEqual(expect_data, response.json)
