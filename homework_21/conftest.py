import pytest
from homework_21.functional_approch.human import Human
from homework_21.functional_approch.race import Race



@pytest.fixture
def human(black) -> Human:
    human = Human("Dara", 39, "female", "black")
    yield human


@pytest.fixture
def black():
    yield Race("black")

@pytest.fixture
def dara_black(black) ->Human:
    yield Human("Dara", 39, "female", "black")



