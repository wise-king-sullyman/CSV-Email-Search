class EmailDB:

    def __init__(self, file, category):
        self.file = file
        self.category = category
        
    #convert csv into data sets
    def csvToSets(file, category):
        import csv
        f = open(file)
        csv_f = csv.reader(f)
        rowSetter = []
        
        #create column headers
        Subject = []
        Body = []
        From_Name = []
        From_Addr = []
        To_Name = []
        To_Addr = []
        
        #create list from rows in csv
        for row in csv_f:
            rowSetter.append(row)

        #hacky as fuck way to fill columns
        for row in rowSetter:
            Subject.append(row[0])
            Body.append(row[1])
            From_Name.append(row[2])
            From_Addr.append(row[3])
            To_Name.append(row[5])
            To_Addr.append(row[6])
            
        #hacky as fuck way to convert lists to sets
        self.subject = set(Subject)
        self.body = set(Body)
        From_NameSet = set(From_Name)
        From_AddrSet = set(From_Addr)
        To_NameSet = set(To_Name)
        To_AddrSet = set(To_Addr)

#search desired data set
def categorySearch( file, searchWord, category ):
    targetEmails = []
     
    for subject in EmailDB(file, category):
        if searchWord in subject:
            targetEmails.append(subject)
                
    return targetEmails

print(categorySearch( 'Inbox.csv', 'Austin', 'body'))
