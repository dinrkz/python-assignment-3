import os
import csv
import json



class FileManager:
    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")

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

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        country_counts = {}
        for row in self.students:
            country = row['country']
            country_counts[country] = country_counts.get(country, 0) + 1

        top_3_raw = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        top_3_list = [{"country": k, "count": v} for k, v in top_3_raw]

        high_gpa = list(filter(lambda s: float(s['GPA']) > 3.5, self.students))
        gpa_values = list(map(lambda s: float(s['GPA']), self.students))

        print("-" * 30)
        print(f"Students with GPA > 3.5: {len(high_gpa)}")
        print(f"First 5 GPA values: {gpa_values[:5]}")
        print("-" * 30)

        self.result = {
            "analysis": "Country Analysis",
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3_countries": top_3_list,
            "all_countries": country_counts
        }
        return self.result

    def print_results(self):
        print("==============================")
        print("ANALYSIS RESULT")
        print("==============================")
        print(f"Total countries: {self.result['total_countries']}")
        for i, item in enumerate(self.result['top_3_countries'], 1):
            print(f"{i}. {item['country']}: {item['count']}")
        print("==============================")

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving JSON: {e}")


#Main
if __name__ == "__main__":
    my_file = 'global_university_students_performance_habits_10000.csv'
    
    fm = FileManager(my_file)
    if not fm.check_file():
        print("Stopping program because file was not found.")
        exit()
    
    fm.create_output_folder()

    dl = DataLoader(my_file)
    data = dl.load()
    if data:
        dl.preview()

        analyser = DataAnalyser(data)
        analyser.analyse()
        analyser.print_results()

        saver = ResultSaver(analyser.result, 'output/result.json')
        saver.save_json()