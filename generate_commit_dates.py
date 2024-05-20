import csv
from datetime import datetime 
from datetime import timedelta 
from datetime import date 

def main() -> None:

    csv_file = 'crystal-github.csv'
    commit_bool_reader = csv.reader(open(csv_file))
    
    commit_bool = list(commit_bool_reader)
    starting_date_string = commit_bool[0][0]
    starting_date = datetime.strptime(starting_date_string, "%Y-%m-%d").date()
    
    commit_bool[0][0] = ""
    
    commit_bool_transpose = list(map(list, zip(*commit_bool)))
    
    commit_dict = []
    commit_date = starting_date
    for row in range(1,len(commit_bool_transpose)):
        for commit in commit_bool_transpose[row]:
            if commit == "0":
                commit_amount = "1-4"
            else:
                commit_amount = "more than 5"
            commit_dict.append({"date": commit_date, "number of commits": commit_amount})
            commit_date = commit_date + timedelta(days=1) 
    
    fields = ["date", "number of commits"]
    
    filename = "commit_dates.csv"
    
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(commit_dict)    
            

if __name__ == '__main__':
    main()