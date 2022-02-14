import csv
class Parsing:


    def __init__(self):
        query = input("Enter the Query:")
        reg1 = r'[a-zA-Z]{6}\s[a-zA-z_*0-9]+\s[a-zA-z]{4}\s[a-zA-Z0-9"=_]+'


        self.text = list(query.split(" "))


        self.dict_name = {
            'type': ['select'],
            'FROM': ['from'],
            'WHERE': ['where']

        }
        if self.text[2] != 'as':
            self.type = self.text[0]
            self.table = self.text[3]
            self.column = self.text[1]
            self.condition = self.text[-1]


        else:
            self.type = self.text[0]
            self.table = self.text[4]
            self.column = self.text[1]
            self.condition = self.text[-1]

        try:
            self.type == self.dict_name[type]
        except Exception as e:
            print('Error in the Query')

    def Parsing_def(self):
        file_name = 'D:\{}.csv'.format(table)
        try:
            with open(file_name, 'r') as fp:
                if self.type == 'select':
                    if self.column != "*":
                        if self.table != self.condition:
                            self.lst = ['>=', '<=', '!=', '==', '<', '>']
                            self.operator = list(filter(lambda j: self.condition.split("{}".format(j))[0] != self.condition[:], lst))
                            key, value = tuple(self.condition.split("{}".format(self.operator[0])))

                            self.reader = csv.DictReader(fp, delimiter=',')
                            self.lst = []
                            for row in reader:
                                if row[key] == value[1:len(value) - 1]:
                                    self.lst.append(row[key])
                                else:
                                    pass
                            print(self.lst)
                        else:
                            reader = csv.DictReader(fp, delimiter=',')
                            for row in reader:
                                print(row[self.column])
                    else:
                        if self.table != self.condition:
                            self.lst = ['>=', '<=', '!=', '==']
                            self.operator = list(filter(lambda j: self.condition.split("{}".format(j))[0] != self.condition[:], lst))
                            self.key, self.value = tuple(self.condition.split("{}".format(self.operator[0])))

                            reader = csv.DictReader(fp, delimiter=',')
                            self.lst = []
                            for row in reader:
                                if row[self.key] == self.value[1:len(self.value) - 1]:
                                    self.lst.append(row)
                                else:
                                    pass

                            print(self.lst)
                        else:
                            reader = csv.DictReader(fp, delimiter=',')
                            self.lst = []
                            for row in reader:
                                for value in row.values():
                                    self.lst.append(value)
                            print(self.lst)

        except Exception as e:
            print("here is error")




obj1=Parsing()








