from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import CountryAnalyser, GpaAnalyser

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

        print('\n--- Task 5: Polymorphism ---') 
        analysers = [CountryAnalyser(data[:10]), GpaAnalyser(data[:10])]
        
        print('Running all analysers:')
        for a in analysers:
            print(a)
            a.analyse()
            a.print_results()
            print()

        print('\n--- Task 4: Association (Report) ---')
        main_analyser = CountryAnalyser(data)
        saver = ResultSaver(main_analyser.result, 'output/result.json')
        report = Report(main_analyser, saver)
        report.generate()