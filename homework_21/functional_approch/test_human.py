
def test_check_age_property_return_value(human):
    assert human.age == "77"

def test_name_property_return_value(human):
    assert human.change_name("Dara") == "Karl"

def test_name_return_value(human):
    assert human.name == "Lisa"

def test_check_race_property_return_value(human):
    assert human.race == "white"

def test_validate_gender(human):
    assert human.test_gender_return_value('female') == "binary_person"
