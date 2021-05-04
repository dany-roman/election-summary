# import os and csv modules
import os
import csv

# create a reference to the csv file location
csvpath = os.path.join('election-summary','Test Data','election_data.csv')

#create empty lists for total votes and candidate votes
votes = []
khanvotes = []
correyvotes = []
livotes = []
otooleyvotes = []

# open the csv file to collect data

with open(csvpath) as csvfile:

# create read csv file and separated data using comma 
    csvreader = csv.reader(csvfile, delimiter=',')

# create a loop to collect vote data based on candidate

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

# calculate the total number of votes and votes for each candidate
nvotes = len(votes)
khan = len(khanvotes)
correy = len(correyvotes)
li = len(livotes)
otooley = len(otooleyvotes)

# calculate the percentage of votes per candidate
perkhan = round((khan/nvotes * 100), 1)
percorrey = round((correy/nvotes * 100), 1)
perli = round((li/nvotes * 100), 1)
perotooley = round((otooley/nvotes * 100), 1)

# identify the winner using a series of conditional statements
if (khan > correy) and (khan > li) and (khan > otooley):
    winner = "Khan"
elif (correy > khan) and (correy > li) and (correy > otooley):
    winner = "Correy"
elif (li > khan) and (li > correy) and (li > otooley):
    winner = "Li"
elif (otooley > khan) and (otooley > correy) and (otooley > li):
    winner = "OTooley"

# display results on terminal
print(f"------------------------------------------")
print(f"Election Results")
print(f"------------------------------------------")
print(f'Total votes cast: {nvotes}')
print(f"------------------------------------------")
print(f'Khan: {khan} ({perkhan}%)')
print(f'Correy: {correy} ({percorrey}%)')
print(f'Li: {li} ({perli}%)')
print(f'OTooley: {otooley} ({perotooley}%)')
print(f"------------------------------------------")
print(f'Winner: {winner}')
print(f"------------------------------------------")

# create an election summary file and write the results into it. Close at the end
with open("ElectionSummary.txt", "w+") as output:

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