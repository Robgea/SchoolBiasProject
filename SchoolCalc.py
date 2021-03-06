import csv, os

schoolList = []

def addSchool(school):
  global schoolList
  if (school.isdigit()) or (len(school) <2):
    return
  else: 
    if school in schoolList:
      return
    else:
      try:
        schoolList.append(school)
      except:
        print("Can't add "  + school + ' to the list.')


for judgeRecord in os.listdir('.'):
  if not judgeRecord.endswith('.csv'):
    print('Skipping...' + judgeRecord)
    continue
  elif (judgeRecord == 'schoollistoutput.csv') or (judgeRecord == 'schoollist.csv'):
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
        school2 = entry2[:-3]
        addSchool(school1)
        addSchool(school2)


schoolList.sort()


schoolFile = open('schoollistoutput.csv', 'w', newline = '')
schoolWrite = csv.writer(schoolFile)
schoolWrite.writerow(schoolList)
