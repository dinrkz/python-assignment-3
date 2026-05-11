class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        country_counts = {}
        for row in self.students:
            country = row.get('country', 'Unknown')
            country_counts[country] = country_counts.get(country, 0) + 1

        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]

        self.result = {
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": top_3,
            "all_countries": country_counts
        }
        return self.result

    def print_results(self):
        print("COUNTRY ANALYSIS REPORT")
        print("==============================")
        super().print_results()
        print("==============================")

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"


# Дополнительный класс просто для демонстрации Полиморфизма (Task 5)
class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        self.result = {
            "total_students": len(self.students),
            "mock_message": "This is just for polymorphism demo"
        }
        return self.result

    def print_results(self):
        print("GPA ANALYSIS REPORT")
        print("==============================")
        super().print_results()
        print("==============================")

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"