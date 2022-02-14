import csv
with open('D:\sql_parsing_data.csv','r') as fp:
    #reader=csv.reader(fp,delimiter=",")
    #header=next(reader)
    #print(header)
    #func_id=0
    #index = header.index("ROll No")
    #sum_of_roll=0
    #for row in reader:
    #        if len(row)>0:
    #            sum_of_roll += int(row[index])
    #print(sum_of_roll)

    reader=csv.DictReader(fp,delimiter=',')

    s=''
    sum=0
    for row in reader:
        sum+=float(row[s])
    print(sum)

