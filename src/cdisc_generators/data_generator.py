import random
import string
from datetime import datetime, timedelta

class DataGenerator:
    """
    A class for generating synthetic data based on CDISC standards.
    """
    def __init__(self, form_data):
        self.form_data = form_data

    def _generate_text(self, length=10):
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def _generate_integer(self, min_val=0, max_val=100):
        return random.randint(min_val, max_val)

    def _generate_float(self, min_val=0.0, max_val=100.0, decimal_places=2):
        return round(random.uniform(min_val, max_val), decimal_places)

    def _generate_date(self):
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2023, 12, 31)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        return (start_date + timedelta(days=random_days)).isoformat()

    def _generate_from_codelist(self, codelist):
        # This is a placeholder implementation.
        # In a real implementation, we would fetch the codelist from the CDISC Library.
        # For now, we will just return a dummy value.
        return codelist.nci_code

    def _generate_field_value(self, field):
        if field.codelist:
            return self._generate_from_codelist(field.codelist)

        datatype = field.datatype.lower()
        if datatype == "text":
            return self._generate_text()
        elif datatype == "integer":
            return self._generate_integer()
        elif datatype == "float":
            return self._generate_float()
        elif datatype == "date":
            return self._generate_date()
        else:
            return None

    def generate(self, num_subjects: int):
        """
        Generates a dataset with the given number of subjects.
        """
        dataset = []
        for i in range(num_subjects):
            subject_data = {}
            for field in self.form_data.fields:
                subject_data[field.oid] = self._generate_field_value(field)
            dataset.append(subject_data)
        return dataset
