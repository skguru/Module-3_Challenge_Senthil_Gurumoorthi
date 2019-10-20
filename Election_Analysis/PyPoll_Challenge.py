#Import csv and os 
import csv
import os

#assign a variable for the file to load and path using chaining method

file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")

#create a file variable to a direct or indirect path to the file

file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt")

#initialize votes counter

total_votes = 0
total_votes_county=0
candidate_options = []
county_options = []
votes_percentage = 0

#create empty dictionary
candidate_votes ={}
county_votes = {}

#initialize variables for winning candidates and largest county

winning_candidate = ""
winning_count = 0 
winning_percentage  = 0
county_largest = ""
largest_count_county = 0
largest_percentage_county = 0

#Open the election results and read the file

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)
 #for each row in csv file after the header
    for row in file_reader:
        total_votes += 1
        total_votes_county += 1
        #read the candidate and county anmes from each row- third colum n(2), second column n(1) respectively
        candidate_name = row[2]
        county_name = row[1]
        #Track the vote count per candidate
        if candidate_name not in candidate_options:
          #add to the list
            candidate_options.append(candidate_name)
            #Begin tracking the vote count
            candidate_votes[candidate_name] = 0
        #add vote count per candidate
        candidate_votes[candidate_name] += 1
        #Track the vote count per county
        if county_name not in county_options:
            #add to the list
            county_options.append(county_name)
            #Begin tracking the vote count
            county_votes[county_name] = 0
        #add vote count per county
        county_votes[county_name] += 1

    with open(file_to_save, "w") as txt_file:
        #Print and write Total Votes to the screen and to the file respectively
        
        election_results = (f"Election Results\n"
          f"-------------------------\n" 
          f"Total Votes: {total_votes:,}\n\n"
          f"-------------------------\n" )
        print("\n")
        print(election_results)
        txt_file.write(election_results)
        
        #Print and write title texts
        txt_file.write("County Votes: \n\n")
        print("County Votes: \n\n")

        #To find the largest county turnout

        #Caclulate votes per county and its percentage turnout

        for county in county_votes:
            votes_county = county_votes[county]
            votes_county_percentage = (votes_county/total_votes_county) *100
            
            #Largest County turnout through votes per county and %votes/county
            if (votes_county > largest_count_county) and (votes_county_percentage > largest_percentage_county):
              largest_count_county = votes_county
              largest_percentage_county = votes_county_percentage
              county_largest = county

            #Write and print the total votes and percentage votes per county
            county_results = (f"{county}: {votes_county_percentage: .1f}% ({votes_county:,})\n")
            txt_file.write(county_results)
            print(county_results)

        #Write and print the largest county turnout
        largest_turnout = (f"-------------------------\n"
            f"Largest County Turnout: {county_largest}\n"
            f"-------------------------\n")
        txt_file.write(largest_turnout)
        print(largest_turnout)

        #Write and print title texts
        txt_file.write("\nCandidate Votes: \n\n")
        print("Candidate Votes: \n\n")

        #To find the winning candidate

        #Calculate votes per candidate and percentage votes per candidate
        for candidate in candidate_votes:
          votes= candidate_votes[candidate]
          vote_percentage = (votes/total_votes) *100
        
        #Write and print total votes and percentage votes per candidate
          candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes:,})\n")
          txt_file.write(candidate_results)
          print(candidate_results)

        #Winning candidate through votes per candidate and %votes/candidate
          if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            #set the winning candidate = candidates name
            winning_candidate = candidate
        
        #Write and print the largest county turnout
        winning_summary = (f"-------------------------\n"
        f"Winner: {winning_candidate}\n" 
        f"Winning Vote Count: {winning_count:,}\n" 
        f"Winning Percentage: {winning_percentage:.1f}%\n" 
        f"-------------------------\n")
        txt_file.write(winning_summary)
        print(winning_summary)
       
        





