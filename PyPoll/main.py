
import os
import csv

file_path = os.path.join("Resources","election_data.csv")

# read files to input specific info to list for further analysis
voter_list = []
candidate_list = []

with open (file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)

    for row in csvreader:
        voter_list.append(row[0])
        candidate_list.append(row[2])

total_votes = len(voter_list)
candidate_list_uni = list(set(candidate_list))

print("Election Results")
print("------------------------------------------")
print(f"Total Votes: {total_votes}")
print("------------------------------------------")

# define functions to account for calculations of each candidate
# function for counting total No
def candidate_count(candidate_name):
    count = 0
    for candidate in candidate_list:
        if candidate == candidate_name:
            count += 1
    return count
# function for summary of each candidate 
def candidate_output(candidate_name):
    candidate_total = candidate_count(candidate_name)
    candidate_per = round((candidate_total/total_votes)*100,3)
    candidate_sum = (f"{candidate}: {candidate_per}% ({candidate_total})\n")
    return candidate_sum

# output results of candidate summary into terminal
for candidate in candidate_list_uni:
    print(candidate_output(candidate))

print("------------------------------------------")

# output results of winner into terminal
candidate_total_list = [candidate_count(candidate) for candidate in candidate_list_uni]
winner = candidate_list_uni[candidate_total_list.index(max(candidate_total_list))]
print(f"Winner: {winner}")

print("------------------------------------------")

# output into txt file
result_path = "C:/Users/Eva/Documents/GitHub/python-challenge/PyPoll/analysis/Result.txt"

with open(result_path,"w") as results:
    results.write("Election Results\n")
    results.write("------------------------------------------\n")
    results.write(f"Total Votes: {total_votes}\n")
    results.write("------------------------------------------\n")

    for candidate in candidate_list_uni:
        output = candidate_output(candidate)
        results.write(output)

    results.write("------------------------------------------\n")
    results.write(f"Winner: {winner}\n")
    
    results.close()



