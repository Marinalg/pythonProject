from homework_21.oop_approach.human_oop import Human

class TestHuman:
    def setup_class(self):
        self.human = Human("Dara", 39, "female", "black")

class TestCheckHumanAge(TestHuman):
    def test_check_age_property_return_value(self):
        assert self.human.age == "77"

class TestCheckHumanNameProperty(TestHuman):
    def test_name_property_return_value(self):
        assert self.human.change_name("Dara") == "Karl"

class TestCheckHumanName(TestHuman):
    def test_name_return_value(self):
        assert self.human.name == "Lisa"

class TestCheckHumanRace(TestHuman):
    def test_check_race_property_return_value(self):
        assert self.human.race == "white"

class TestCheckGender(TestHuman):
    def test_validate_gender(self):
        assert self.test_gender_return_value('female') == "binary_person"

    def teardown(self):
        print("Teardown was called")


    def teardown_class(self):
        print("class teardown was called")

