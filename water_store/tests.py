from django.test import TestCase
import requests


def test_oro_data_integrity(test):
    client = requests.get("http://cdec.water.ca.gov/cgi-progs/queryDaily?ORO&d=11-June-2016+09:35&span=365days")
    data = client._content

    second_client = requests.get("http://waterlogproject.org/rest/?dam_id=oro&start_date=2015-01-01&end_date=2015-12-31")
    second_data_set = second_client._content

