import os
import csv
from pprint import pprint


filepath = os.path.join("budget_data.csv")

with open(filepath, "r") as in_file:
    in_csv = csv.reader(in_file)

    header = next(in_csv)


    l = list(in_csv)

    print ("Financial Analysis")
    print ("---------------------------")

    count_of_row = len(l)
    print ("Total Months: " + str(count_of_row))

    #splitting the list into two lists: date and profit/losses
    date = [i[0] for i in l]
    prof_loss = [i[1] for i in l] 
    
    # using list comprehension to perform convert string element to integer to get the total
    int_prof_loss = [int(i) for i in prof_loss] 
    print ("Total: " + "$" + str(sum(int_prof_loss)))

    #merging two lists into one list
    new_l = zip(date, int_prof_loss)
    new_list = list(new_l)
    
    #compute for average change
    avg_change = [int_prof_loss[i+1]-int_prof_loss[i] for i in range(len(int_prof_loss)-1)]
    def Average(lst): 
        return sum(lst) / len(lst) 
    average = Average(avg_change)
    print ("Average Change: " + "$" + str(format(average, '.2f')))

    #merging two lists into one list
    new_l = zip(date[1:], avg_change)
    new_list = list(new_l)
    
    #sorting the list
    def sortlist(element2):
        return element2[1]
    new_list.sort(key=sortlist)

    increase = new_list[-1]
    decrease = new_list[0]

    print ("Greatest Increase in Profits: " + str(increase[0]) + " " + "($" + str(increase[1]) + ")")
    print ("Greatest Increase in Profits: " + str(decrease[0]) + " " + "($" + str(decrease[1]) + ")")

    
    


    


