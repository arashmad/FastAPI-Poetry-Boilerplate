#!/usr/bin/env python

"""Tests for `data_provider` package."""

from fastapi.testclient import TestClient

from fastapi_poetry_boilerplate.core import setting
from fastapi_poetry_boilerplate.create_app import app

SERVICE_NAMESPACE = setting.SERVICE_NAMESPACE


class TestDataEndpointsHome():
    """Test the home endpoint."""

    @classmethod
    def setup_class(cls):
        """Set up test fixtures."""
        cls.app = TestClient(app)
        cls.endpoint_prefix = SERVICE_NAMESPACE

    @classmethod
    def teardown_class(cls):
        """Tear down test fixtures."""
        print("teardown_class called once for the class")

    @classmethod
    def setup_method(cls):
        """Setup method."""
        print("setup_method called for every method")

    @classmethod
    def teardown_method(cls):
        """Tear down method."""
        print("teardown_method called for every method")

    def test_api_home_200(self):
        """Test the home endpoint."""
        response = self.app.get(f"{self.endpoint_prefix}/")
        assert response.status_code == 200

    def test_api_home_404_url_not_found(self):
        """Test the home endpoint with a non existing url."""
        response = self.app.get(f"{self.endpoint_prefix}/NotFound")
        assert response.status_code == 404
