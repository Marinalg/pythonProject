from typing import List
import pytest
from homework_27.core.config.config_gender import Config
from homework_27.core.config.config_nationalize import Config
from homework_27.services.nationalities.nationalities import NationalitiesServices


@pytest.fixture
def config():
    yield Config()


@pytest.fixture
def facts_service(config):
    yield NationalitiesServices(config)


@pytest.fixture
def fact() -> NationalitiesServices:
    yield NationalitiesServices.from_response_json(
        {"data": [{"fact": "test", "length": 50}]}
    )

@pytest.fixture
def facts_service(config):
    yield GenderServices(config)


@pytest.fixture
def fact() -> GenderServices:
    yield NationalitiesServices.from_response_json(
        {"data": [{"fact": "test", "length": 50}]}
    )