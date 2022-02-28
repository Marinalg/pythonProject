import pytest


@pytest.mark.gender
def test_check_random_gender(gender, monkeypatch):
    monkeypatch.setattr(
        "gender"
        "name"
        "count"
    )
    actual_gender = gender.get_random_gender()
    assert gender == actual_gender

    actual_gender_name = gender.get_random_gender()
    assert gender == actual_gender_name


@pytest.mark.skip()
def test_skip_check():
    ...