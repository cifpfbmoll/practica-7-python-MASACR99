def reformatDate(date):
    date = date.split("/")
    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    return str(date[0]) + " of " + months[int(date[1])-1] + " of " + str(date[2])

date = input("Input the date(use / to separate): ")
print(reformatDate(date))