import csv

class CSVAdapter:
    def read_csv(self, file_path):
        data = []
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))
        return data

    def write_csv(self, file_path, data):
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)