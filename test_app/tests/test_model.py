from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.exceptions import ValidationError
from test_app.models import DummyData


class DummyDataModelTest(TestCase):
    # Test unique name constraint
    def test_unique_name(self):
        DummyData.objects.create(first_name="Rakibul", last_name="Hasan", age=24)

        with self.assertRaises(IntegrityError):
            DummyData.objects.create(first_name="Rakibul", last_name="Hasan", age=18)

    # Test name fields are required
    def test_name_age_field_required(self):
        # missing first_name
        dummy_data1 = DummyData(last_name="Hasan", age=24)
        # missing last_name
        dummy_data2 = DummyData(first_name="D", age=24)
        # missing both first_name and last_name
        dummy_data3 = DummyData(age=24)
        # missing age
        dummy_data4 = DummyData(first_name="D", last_name="Hasan")

        # Test missing first_name
        with self.assertRaises(ValidationError):
            dummy_data1.full_clean()

        # Test missing last_name
        with self.assertRaises(ValidationError):
            dummy_data2.full_clean()

        # Test missing both first_name and last_name
        with self.assertRaises(ValidationError):
            dummy_data3.full_clean()

        # Test missing age
        with self.assertRaises(ValidationError):
            dummy_data4.full_clean()

    ## Test Invalid Data Types
    def test_invalid_data_types(self):
        x = DummyData(first_name=65565, last_name="Hasan", age="yyhh")

        try:
            x.full_clean()
        except ValidationError as e:
            self.assertIn("age", str(e))
