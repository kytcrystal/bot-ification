import csv
from datetime import datetime 
from datetime import timedelta 
from datetime import date 

DATE_KEY = "date"
NUM_COMMIT_KEY = "number of commits"
INPUT_FILE = 'crystal-github.csv'
OUTPUT_FILE = "commit_dates.csv"


def main() -> None:

    commit_bool_reader = csv.reader(open(INPUT_FILE))
    
    commit_bool = list(commit_bool_reader)
    start_date_string = commit_bool[0][0]
    start_date = datetime.strptime(start_date_string, "%Y-%m-%d").date()
    
    commit_bool[0][0] = ""
    commit_bool_transpose = list(map(list, zip(*commit_bool)))
    
    commit_dict = extract_commit_dates(start_date, commit_bool_transpose)
    
    write_csv(OUTPUT_FILE, commit_dict) 
    

def extract_commit_dates(start_date, commit_bool_transpose):
    commit_dict = []
    commit_date = start_date
    for row in range(1,len(commit_bool_transpose)):
        for commit in commit_bool_transpose[row]:
            if commit == "0":
                commit_amount = "1-4"
            else:
                commit_amount = "more than 5"
            commit_dict.append({DATE_KEY: commit_date, NUM_COMMIT_KEY: commit_amount})
            commit_date = commit_date + timedelta(days=1) 
    return commit_dict


def write_csv(filename, commit_dict):
    fields = [DATE_KEY, NUM_COMMIT_KEY]
    
    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        writer.writerows(commit_dict)   
            

if __name__ == '__main__':
    main()