import os
import csv
csvpath = os.path.join('election-summary','Test Data','election_data.csv')

votes = []
khanvotes = []
correyvotes = []
livotes = []
otooleyvotes = []
# candidates = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    print(csvreader)

#     prev_row = 0
#     delta = 0

    for row in csvreader:
        votes.append(row[0])
        if row[2] == "Khan":
            khanvotes.append(row[0])
        elif row[2] == "Correy":
            correyvotes.append(row[0])
        elif row[2] == "Li":
            livotes.append(row[0])
        elif row[2] == "O'Tooley":
            otooleyvotes.append(row[0])    

    nvotes = len(votes)
    khan = len(khanvotes)
    correy = len(correyvotes)
    li = len(livotes)
    otooley = len(otooleyvotes)
    perkhan = round((khan/nvotes * 100), 1)
    percorrey = round((correy/nvotes * 100), 1)
    perli = round((li/nvotes * 100), 1)
    perotooley = round((otooley/nvotes * 100), 1)
    
    if (khan > correy) and (khan > li) and (khan > otooley):
        winner = "Khan"
    elif (correy > khan) and (correy > li) and (correy > otooley):
        winner = "Correy"
    elif (li > khan) and (li > correy) and (li > otooley):
        winner = "Li"
    elif (otooley > khan) and (otooley > correy) and (otooley > li):
        winner = "OTooley"
# find the winner using if statements

print("------------------------------------------")
print("Election Results")
print("------------------------------------------")
print(f'Total votes cast: {nvotes}')
print("------------------------------------------")
print(f'Khan: {khan} ({perkhan}%)')
print(f'Correy: {correy} ({percorrey}%) ')
print(f'Li: {li} ({perli}%) ')
print(f'OTooley: {otooley} ({perotooley}%) ')
print("------------------------------------------")
print(f'Winner: {winner}')
print("------------------------------------------")
