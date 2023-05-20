import os
import csv

cand_list = {}
break_line = "--------------------"
#open csv file
csvpath = os.path.join("..", "Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)
    total_vote = 0

#find total vote and add candidate name as key to dictionary and add votes to value 
    for row in csv_reader:
        total_vote += 1
        name = row[2]
        if name in cand_list:
            cand_list[name] += 1
        else:
            cand_list[name] = 1

print(total_vote)
print(cand_list)

#add voting results percentage to the dictionary
cand_list["Stockham Percent"] = round((cand_list["Charles Casper Stockham"]/ total_vote) * 100, 2)
cand_list["DeGette Percent"] = round((cand_list["Diana DeGette"]/ total_vote) * 100, 2)
cand_list[ "Doane Percent"] = round((cand_list["Raymon Anthony Doane"]/ total_vote) * 100, 2)

#grab the winning candidate

cand_winner = max(cand_list, key=cand_list.get)

#print the results

print("Election Results")
print(break_line)
print(f"Total Vote: {total_vote}")
print(break_line)
print(f"Charles Casper Stockham: {cand_list['Stockham Percent']}% ({cand_list['Charles Casper Stockham']})")
print(f"Diana DeGette: {cand_list['DeGette Percent']}% ({cand_list['Diana DeGette']})")
print(f"Raymon Anthony Doane: {cand_list['Doane Percent']}% ({cand_list['Raymon Anthony Doane']})")
print(break_line)
print(f"Winner: {cand_winner}")

#output the results
output_result = os.path.join("..", "Analysis", "results.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Election Results\n")
    txt_file.write(f"{break_line}\n")
    txt_file.write(f"Total Vote: {total_vote}\n")
    txt_file.write(f"{break_line}\n")
    txt_file.write(f"Charles Casper Stockham: {cand_list['Stockham Percent']}% ({cand_list['Charles Casper Stockham']})\n")
    txt_file.write(f"Diana DeGette: {cand_list['DeGette Percent']}% ({cand_list['Diana DeGette']})\n")
    txt_file.write(f"Raymon Anthony Doane: {cand_list['Doane Percent']}% ({cand_list['Raymon Anthony Doane']})\n")
    txt_file.write(f"{break_line}\n")
    txt_file.write(f"Winner: {cand_winner}\n")
