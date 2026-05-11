import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, mode='r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except Exception as e:
            print(f"Error loading data: {e}")
            return []

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for row in self.students[:n]:
            sid = row.get('student_id', 'N/A')
            cnt = row.get('country', 'N/A')
            gpa = row.get('GPA', 'N/A')
            print(f"{sid} | {cnt} | GPA: {gpa}")
        print("-" * 30)