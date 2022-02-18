log_file = open("um-server-01.txt")# opening the file


def sales_reports(log_file):#a function
    for line in log_file:# for looping the the file
        line = line.rstrip()#stripping the blank spaces
        day = line[0:3]#selecting first 3 letters of the line
        
        if day == "Mon":#choosing the day to display
            print(line)#displaying response to the console.
    log_file.seek(0,0)

def melon_lord(log_file):
    
    for line in log_file:
        line = line.rstrip()
        split = line.split(' ')
        if float(split[2]) >=10:
            print(line)
    log_file.seek(0,0)

sales_reports(log_file)#invoking function
melon_lord(log_file)