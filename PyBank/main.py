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
    
    #compute for average change
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

    #assign maximum and minimum values to variables to get the required output format
    increase = new_list[-1]
    decrease = new_list[0]
    print ("Greatest Increase in Profits: " + str(increase[0]) + " " + "($" + str(increase[1]) + ")")
    print ("Greatest Increase in Profits: " + str(decrease[0]) + " " + "($" + str(decrease[1]) + ")")

    #export results to terminal and a text file
    output = open('output.txt', 'w')

    print ("Financial Analysis", file = output)
    print ("---------------------------", file = output)
    print ("Total Months: " + str(count_of_row), file = output)
    print ("Total: " + "$" + str(sum(int_prof_loss)), file = output)
    print ("Average Change: " + "$" + str(format(average, '.2f')), file = output)
    print ("Greatest Increase in Profits: " + str(increase[0]) + " " + "($" + str(increase[1]) + ")", file = output)
    print ("Greatest Increase in Profits: " + str(decrease[0]) + " " + "($" + str(decrease[1]) + ")", file = output)

    
    


    


