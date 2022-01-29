from homework_21.oop_approach.human_oop import Human

class TestHumanSuite:

    def setup_class(self):
        self.human = Human("Dara", 39, "female", "black")

    def setup(self):
        print("Setup was called")

    def test_check_age_property_return_value(self):
        assert self.human.age == "77"

    def test_check_race_property_return_value(self):
        assert self.human.race == "white"

    def test_name_property_return_value(self):
        self.human.name(self)
        assert self.human.change_name('Dara') == "Karl"

    def test_validate_gender(self):
        self.human.gender()
        assert self.test_gender_return_value('female') == "binary_person"

    def teardown(self):
        print("Teardown was called")