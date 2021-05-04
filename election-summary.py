import os
import csv
csvpath = os.path.join('election-summary','Test Data','election_data.csv')

votes = []
khanvotes = []
correyvotes = []
livotes = []
otooleyvotes = []
county = []
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
        county.append(row[1])
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
