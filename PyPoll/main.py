import os
import csv

filepath = os.path.join("election_data.csv")

with open(filepath, "r") as in_file:
    in_csv = csv.reader(in_file)

    header = next(in_csv)

    l = list(in_csv)


    #get total number of votes cast
    count_of_row = len(l)
    
    #create a new list for candidates
    candidates = [i[2] for i in l]

    #complete list of candidates who received votes
    list_set = set(candidates) 
    unique_list = list(list_set)
   
    #get total number of votes per candidate
    count_candidate = [candidates.count(unique_list[0]), candidates.count(unique_list[1]), candidates.count(unique_list[2]), candidates.count(unique_list[3])]

    #join the list of candidates and their total number of votes
    new_l = zip(unique_list, count_candidate)
    new_list = list(new_l)

    #sort lists
    def sortlist(element2):
        return element2[1]
    new_list.sort(key=sortlist)
    count_candidate.sort()
   

    #calulate and format percentage of votes each candidate won
    percent = [format((count_candidate[i]/count_of_row * 100), '.3f') for i in range(len(count_candidate))]
    

    # return results to terminal
    print ("Election Results")
    print ("---------------------------")
    print ("Total Votes: " + str(count_of_row))
    print ("---------------------------")
    print (str(new_list[3][0]) + ": " + str(percent[3]) + "%" + " " + "(" + str(count_candidate[3]) + ")")
    print (str(new_list[2][0]) + ": " + str(percent[2]) + "%" + " " + "(" + str(count_candidate[2]) + ")")
    print (str(new_list[1][0]) + ": " + str(percent[1]) + "%" + " " + "(" + str(count_candidate[1]) + ")")
    print (str(new_list[0][0]) + ": " + str(percent[0]) + "%" + " " + "(" + str(count_candidate[0]) + ")")
    print ("---------------------------")
    print ("Winner: ", new_list[-1][0])
    print ("---------------------------")

    
    #export results to a text file
    output = open('output.txt', 'w')
    print ("Election Results", file = output)
    print ("---------------------------", file = output)
    print ("Total Votes: " + str(count_of_row), file = output)
    print ("---------------------------", file = output)
    print (str(new_list[3][0]) + ": " + str(percent[3]) + "%" + " " + "(" + str(count_candidate[3]) + ")", file = output)
    print (str(new_list[2][0]) + ": " + str(percent[2]) + "%" + " " + "(" + str(count_candidate[2]) + ")", file = output)
    print (str(new_list[1][0]) + ": " + str(percent[1]) + "%" + " " + "(" + str(count_candidate[1]) + ")", file = output)
    print (str(new_list[0][0]) + ": " + str(percent[0]) + "%" + " " + "(" + str(count_candidate[0]) + ")", file = output)
    print ("---------------------------", file = output)
    print ("Winner: ", new_list[-1][0], file = output)
    print ("---------------------------", file = output)






    

    


