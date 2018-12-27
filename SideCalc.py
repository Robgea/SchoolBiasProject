import csv
from judging import school_dict, counting_dict, ignore_list
import os



#three outputs. CSV results, Ignore List Rounds, unread rounds.

# start this off
results_csv = open('Side_Bias_Results.csv', 'w', newline='')
results_write = csv.writer(results_csv)
header_list = ["name",]
for key in counting_dict.keys():
    header_list.append(key)

results_write.writerow(header_list)

ignore_doc = open('ignored_rounds.txt', 'a')
error_doc = open('error_rounds.txt', 'a')




def side_bias_calc(schools, count, ignore):
  for judgeRecord in os.listdir('.'):
    if not judgeRecord.endswith('.csv'):
      print('Skipping...' + judgeRecord)
      continue
    elif judgeRecord == 'Side_Bias_Results.csv':
      continue
    else:
      print("Counting judge record for..." + judgeRecord)
      csvFileObj = open(judgeRecord)
      recordReader = csv.reader(csvFileObj)
      recordlist = list(recordReader)
      recordEntry = judgeRecord[:-4]
      judgeoutput = [recordEntry,]

      for value in count.values():
        value = 0


      #go through each row, do two checks, one for Aff and one for Neg. Increase each one as appropros.


      for row in recordlist:
        row[4] = aff_team
        row[5] = neg_team
        aff_team = aff_team[:-3]
        neg_team = neg_team[:-3]
        if row[2] == 'Event':
          continue
        else:
          if aff_team in ignore:
            ignore_doc.write(f'{recordEntry} has a bad round in {row[0]} with {aff_team}.\n')
          elif aff_team in schools:
            if row[6].startswith('AFF'):
                try:
                  count[str(schools[aff_team] + ' Aff Total')] += 1
                  count[str(schools[aff_team] + ' Aff Wins')] += 1
                  count['Aff Wins'] += 1
                  count['Aff Total'] += 1
                except:
                  print('Something Fucky happened')
            elif row[6].startswith('NEG')
                try:
                  count[str(schools[aff_team] + ' Aff Total')] += 1
                  count['Aff Total'] += 1
                except:
                  print('Something Fucky happened.')
            else:
                print(f"No winner for {recordEntry} in {row[0]} with {aff_team}?")
          else:
            print("Error! We caught it!")
            error_doc.write(f"Team {aff_team} not in the records, please advise!\n")
          if neg_team in ignore:
            ignore_doc.write(f'{recordEntry} has a bad round in {row[0]} with {neg_team}.\n')
          elif neg_team in schools:
            if row[6].startswith('NEG'):
              try:
                count[str(schools[neg_team] + ' Neg Total')] += 1
                count[str(schools[neg_team] + ' Neg Wins')] += 1
                count['Neg Wins'] += 1
                count['Neg Total'] += 1
              except:
                print('Something negatively fucky went on.')
            elif row[6].startswith('AFF'):
              try:
                count[str(schools[neg_team] + ' Neg Total')] += 1
                count['Neg Total'] += 1
              except:
                print('Something negatievly fucky happened!')
            else:
              print("We should have caught this last time, right?")
          else:
            print('Error! We caught it!')
            error_doc.write(f'Team {neg_team} not in the records, please advise!\n')
      for value in count.values():
        judgeoutput.append(str(value))
      results_write.writerow(judgeoutput)










          
#write two functions, Aff Check and Neg Check. 



side_bias_calc(school_dict, counting_dict, ignore_list)