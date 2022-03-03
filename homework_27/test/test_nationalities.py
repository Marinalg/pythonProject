import pytest

@pytest.mark.nationalities
def test_check_random_nationalities(nationalities, monkeypatch):
    monkeypatch.setattr(
        "nationalities"
        "name"
        "country"
    )
    actual_nationalities = nationalities.get_random_name()
    assert nationalities == actual_nationalities

    actual_country = nationalities.get_random_country()
    assert nationalities == actual_country




@pytest.mark.skip()
def test_skip_check():
    ...