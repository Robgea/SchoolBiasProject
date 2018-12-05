import csv, os


schoolList = []
maybeList = []

for judgeRecord in os.listdir('.'):
  if not judgeRecord.endswith('.csv'):
    print('Skipping...' + judgeRecord)
    continue
  elif (judgeRecord == 'schoollistoutput.csv') or (judgeRecord == 'maybelistoutput.csv'):
    continue
  else:
    csvObj = open(judgeRecord)
    recordReader = csv.reader(csvObj)
    for row in recordReader:
      if row[1] == 'Date':
        continue
      else:
        entry1 = row[4]
        entry2 = row[5]
        school1 = entry1[:-3]
        if school1.isdigit():
          continue
        elif school1.isalpha():
          if school1 in schoolList:
            continue
          else:
            try: 
              schoolList.append(school1)
            except:
              print("Can't add "  + school1 + ' to the list.')
              continue
        else: 
          if school1 in maybeList:
            continue
          else:
            try:
              maybeList.append(school1)
            except:
              print("Can't add " + school1 + ' to error list.')
              continue
        school2 = entry2[:-3]
        if school2.isdigit():
          continue
        elif school2.isalpha():
          if school2 in schoolList:
            continue
          else:
            try:
              schoolList.append(school2)
            except: 
              print("Can't add " + school2 + ' to the list.')

        else:
          if school2 in maybeList:
            continue
          else:
            try:
              maybeList.append(school2)
            except:
              print("Can't add " + school2 + ' to the Error List.')


#sort the list

#for loop through the lists, and put that shit into rows. 

schoolList.sort()
maybeList.sort()

schoolFile = open('schoollistoutput.csv', 'w', newline = '')
schoolWrite = csv.writer(schoolFile)
schoolWrite.writerow(schoolList)

maybeFile = open('maybelistoutput.csv', 'w', newline = '')
maybeWrite = csv.writer(maybeFile)
maybeWrite.writerow(maybeList)
