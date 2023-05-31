import csv

class CSVAdapter:
    
    # Read method appends data in dictionaries so that it's easier to work
    # with the data, observing a translator/adapter design pattern.
    
    def read_csv(self, file_path):
        data = []
        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(dict(row))
        return data

    # Write method simply writes our data to csv, but keeping the
    # csv logic abstract to the application.

    def write_csv(self, file_path, data):
        with open(file_path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for row in data:
                writer.writerow(row)