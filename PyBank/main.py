import os
import csv

filepath = os.path.join("budget_data.csv")

with open(filepath, "r") as in_file:
    in_csv = csv.reader(in_file)

    header = next(in_csv)

    print ("Financial Analysis")
    print ("---------------------------")

    #convert data to a list
    l = list(in_csv)

    #total count
    count_of_row = len(l)
    print ("Total Months: " + str(count_of_row))
    

    #splitting the list into two lists: date and profit/losses
    date = [i[0] for i in l]
    prof_loss = [i[1] for i in l] 
    
    # using list comprehension to convert string element to integer to get the total
    int_prof_loss = [int(i) for i in prof_loss] 
    print ("Total: " + "$" + str(sum(int_prof_loss)))
    
    #compute for average change using List Comprehension
    avg_change = [int_prof_loss[i+1]-int_prof_loss[i] for i in range(len(int_prof_loss)-1)]
    def Average(lst): 
        return sum(lst) / len(lst) 
    average = Average(avg_change)
    print ("Average Change: " + "$" + str(format(average, '.2f')))

    #merging two lists into a new list starting at index 1 for date because index 0 of 
    #avg_change is null
    new_l = zip(date[1:], avg_change)
    new_list = list(new_l)
    
    #sorting the list
    def sortlist(element2):
        return element2[1]
    new_list.sort(key=sortlist)
    

    print ("Greatest Increase in Profits: " + str(new_list[-1][0]) + " " + "($" + str(new_list[-1][1]) + ")")
    print ("Greatest Increase in Profits: " + str(new_list[0][0]) + " " + "($" + str(new_list[0][1]) + ")")

    #export results to a text file
    output = open('output.txt', 'w')

    print ("Financial Analysis", file = output)
    print ("---------------------------", file = output)
    print ("Total Months: " + str(count_of_row), file = output)
    print ("Total: " + "$" + str(sum(int_prof_loss)), file = output)
    print ("Average Change: " + "$" + str(format(average, '.2f')), file = output)
    print ("Greatest Increase in Profits: " + str(new_list[-1][0]) + " " + "($" + str(new_list[-1][1]) + ")", file = output)
    print ("Greatest Increase in Profits: " + str(new_list[0][0]) + " " + "($" + str(new_list[0][1]) + ")", file = output)

    
    


    


