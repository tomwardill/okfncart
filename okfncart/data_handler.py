import csv


class DataHandler(object):

    default_target_file = './data.csv'

    def LoadProductData(self, target_file=None):
        """Load the product data from a csv file.
        Will use a default file location of './data'
        if none specified

        :param target_file: Location of an alternative data file
        :type target_file: str

        :returns: dict of the product data
        """

        product_data = {}

        # load the default if not otherwise specified
        if not target_file:
            target_file = self.default_target_file

        # load the data, assume it's valid
        # convert second parameter to float for maths
        with open(target_file) as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                product_data[row[0]] = float(row[1])

        return product_data
