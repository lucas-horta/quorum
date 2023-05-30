import csv

class CSVAdapter:
    @staticmethod
    def read_csv(file_path):
        data = []
        with open(file_path, "r", newline="") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read the headers
            for row in reader:
                row_dict = dict(zip(headers, row))
                data.append(row_dict)
        return data

    @staticmethod
    def write_csv(file_path, data):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)