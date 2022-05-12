import csv
import random


with open('tester_table.csv') as file:
    csvfile = csv.DictReader(file)
    fields = [field for field in csvfile.fieldnames[1::]]
    unclear_csv_dict = dict()
    for row in csvfile:
        unclear_csv_dict[row['index']] = row['question_type'], row['date'], row['name'], row['connection'], row['partitipants'], row['misc']

csv_dict = dict()
for i in unclear_csv_dict.items():
    if i[1][0] != '' :
        csv_dict[i[0]] = i[1]


def question_war():
    rand_inx = random.choice(list(csv_dict.keys()))
    qs_types = {'personality' : 'When {} lived?',
                'battle' : 'When {} took place?'}

    war_qs = qs_types[csv_dict[rand_inx][fields.index('question_type')]].format(csv_dict[rand_inx][fields.index('name')])
    answer = csv_dict[rand_inx][fields.index('date')]


    print(war_qs)
    res = input('Your answer:')
    if answer == res: print('Success!!!')
    else: print('Fail(')


for i in range(3):
    question_war()
