"""
This module contains the DataGenerator class, which is responsible for generating synthetic data
based on a given CDISC standard form definition.
"""
import random
import string
from datetime import datetime, timedelta

class DataGenerator:
    """
    A class for generating synthetic data based on CDISC standards.

    This class takes a form data definition and generates synthetic data
    that conforms to the specified fields and their data types.
    """
    def __init__(self, form_data):
        """
        Initializes the DataGenerator.

        Args:
            form_data: An object containing the definition of the form,
                       including its fields and their properties.
        """
        self.form_data = form_data

    def _generate_text(self, length=10):
        """
        Generates a random string of text.

        Args:
            length (int): The length of the string to generate.

        Returns:
            str: A random string of uppercase letters and digits.
        """
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def _generate_integer(self, min_val=0, max_val=100):
        """
        Generates a random integer within a specified range.

        Args:
            min_val (int): The minimum value of the random integer (inclusive).
            max_val (int): The maximum value of the random integer (inclusive).

        Returns:
            int: A random integer.
        """
        return random.randint(min_val, max_val)

    def _generate_float(self, min_val=0.0, max_val=100.0, decimal_places=2):
        """
        Generates a random float within a specified range.

        Args:
            min_val (float): The minimum value of the random float (inclusive).
            max_val (float): The maximum value of the random float (inclusive).
            decimal_places (int): The number of decimal places for the float.

        Returns:
            float: A random float.
        """
        return round(random.uniform(min_val, max_val), decimal_places)

    def _generate_date(self):
        """
        Generates a random date in ISO format.

        The date will be between January 1, 2020, and December 31, 2023.

        Returns:
            str: A random date in ISO 8601 format.
        """
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2023, 12, 31)
        delta = end_date - start_date
        random_days = random.randint(0, delta.days)
        return (start_date + timedelta(days=random_days)).date().isoformat()

    def _generate_from_codelist(self, codelist):
        """
        Generates a value from a codelist.

        Note: This is a placeholder implementation. In a real implementation,
        this method would fetch the codelist from the CDISC Library and select
        a value from it. For now, it returns a dummy value.

        Args:
            codelist: The codelist object.

        Returns:
            str: The NCI code of the codelist.
        """
        # This is a placeholder implementation.
        # In a real implementation, we would fetch the codelist from the CDISC Library.
        # For now, we will just return a dummy value.
        return codelist.nci_code

    def _generate_field_value(self, field):
        """
        Generates a value for a given field based on its data type.

        Args:
            field: The field object for which to generate a value.

        Returns:
            The generated value, or None if the data type is unknown.
        """
        if field.codelist:
            return self._generate_from_codelist(field.codelist)

        datatype = field.datatype.lower()
        if datatype == "text":
            length = field.length if field.length is not None else 10
            return self._generate_text(length)
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
        Generates a dataset with a given number of subjects.

        This method iterates through the specified number of subjects and, for each,
        generates data for all fields in the form.

        Args:
            num_subjects (int): The number of subjects to generate data for.

        Returns:
            list: A list of dictionaries, where each dictionary represents a subject's data.
        """
        dataset = []
        for i in range(num_subjects):
            subject_data = {}
            for field in self.form_data.fields:
                subject_data[field.cdash_var] = self._generate_field_value(field)
            dataset.append(subject_data)
        return dataset
