staff = {
  'name1': 'accounts',
  'name2': 'finance',
  'name3': 'canteen',
  'name4': 'regulation'
}

bordem = {
  'accounts' : 1,
  'finance' : 2,
  'canteen' : 10,
  'regulation' : 3,
  'trading' : 6,
  'change' : 6,
  'IS' : 8,
  'retail' : 5,
  'cleaning' : 4,
  'pissing about' : 25
}

cumulative_score = 0

for value in staff.values():
  if value in bordem:
    cumulative_score += bordem[value]

if cumulative_score <=80:
  print('kill me now')
elif cumulative_score < 100: 
  print('i can handle this')
else: 
  print('party time!!')
