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

line1 = print(f"------------------------------------------")
line2 = print(f"Election Results")
line3 = print(f"------------------------------------------")
line4 = print(f'Total votes cast: {nvotes}')
line5 = print(f"------------------------------------------")
line6 = print(f'Khan: {khan} ({perkhan}%)')
line7 = print(f'Correy: {correy} ({percorrey}%)')
line8 = print(f'Li: {li} ({perli}%) ')
line9 = print(f'OTooley: {otooley} ({perotooley}%)')
line10 = print(f"------------------------------------------")
line11 = print(f'Winner: {winner}')
line12 = print(f"------------------------------------------")

summary = [line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12]

with open("election-summary","ElectionSummary.txt", "w+") as output:

    print(f"------------------------------------------", file=output)
    print(f"Election Results", file=output)
    print(f"------------------------------------------", file=output)
    print(f'Total votes cast: {nvotes}', file=output)
    print(f"------------------------------------------", file=output)
    print(f'Khan: {khan} ({perkhan}%)', file=output)
    print(f'Correy: {correy} ({percorrey}%)', file=output)
    print(f'Li: {li} ({perli}%)', file=output)
    print(f'OTooley: {otooley} ({perotooley}%)', file=output)
    print(f"------------------------------------------", file=output)
    print(f'Winner: {winner}', file=output)
    print(f"------------------------------------------", file=output)

output.close()