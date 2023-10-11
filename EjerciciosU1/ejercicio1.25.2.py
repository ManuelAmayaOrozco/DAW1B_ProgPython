date = input("Dime tu fecha de nacimiento con el siguiente formato (día/mes/año): ")
day = date[:date.find('/')]
ymonth = date[date.find('/')+1:]
month = ymonth[:ymonth.find('/')]
year = ymonth[ymonth.find('/')+1:]
print('Día', day)
print('Mes', month)
print('Año', year)