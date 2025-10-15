meet = {
  'name1': 10,
  'name2': 5,
  'name3': 3,
  'boss': 4
}

happiness = 0
for key, value in meet.items():

  if key == 'boss':
    happiness += (value * 2)
  else:
    happiness += value

happiness /= (len(meet) + 1)

if happiness <= 5:
  print('Get Out Now!')
else:
  print('Nice Work Champ!')
