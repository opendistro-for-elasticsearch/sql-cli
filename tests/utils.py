"""
Copyright 2019, Amazon Web Services Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import json
import pytest
from elasticsearch import ConnectionError, helpers, ConnectionPool

from escli.esconnection import ESConnection
from escli.utils import OutputSettings
from escli.formatter import Formatter

TEST_INDEX_NAME = "escli_test"
ENDPOINT = "http://localhost:9200"


def create_index(test_executor):
    es = test_executor.client
    es.indices.create(index=TEST_INDEX_NAME)


def delete_index(test_executor):
    es = test_executor.client
    es.indices.delete(index=TEST_INDEX_NAME)


def close_connection(es):
    ConnectionPool.close(es)


def load_file(test_executor, filename="accounts.json"):
    es = test_executor.client

    filepath = "./test_data/" + filename

    # generate iterable data
    def load_json():
        with open(filepath, "r") as f:
            for line in f:
                yield json.loads(line)

    helpers.bulk(es, load_json(), index=TEST_INDEX_NAME)


def load_data(test_executor, doc):
    es = test_executor.client
    es.index(index=TEST_INDEX_NAME, body=doc)
    es.indices.refresh(index=TEST_INDEX_NAME)


def get_connection():
    test_es_connection = ESConnection(endpoint=ENDPOINT)
    test_es_connection.set_connection()

    return test_es_connection


def run(test_executor, query, use_console=True):
    data = test_executor.execute_query(query=query, use_console=use_console)
    settings = OutputSettings(table_format="psql")
    formatter = Formatter(settings)

    if data:
        res = formatter.format_output(data)
        res = "\n".join(res)

        return res


# build client for testing
try:
    connection = get_connection()
    CAN_CONNECT_TO_ES = True

except ConnectionError:
    CAN_CONNECT_TO_ES = False

# use @estest annotation to mark test functions
estest = pytest.mark.skipif(
    not CAN_CONNECT_TO_ES, reason="Need a Elasticsearch server running at localhost:9200 accessible"
)
