import csv
import re
import charts


def read_csv(path, country):
  try:
    with open(path, 'r') as csv_file:
      reader = csv.reader(csv_file, delimiter=',')

      header = next(reader)
      years = [
          column[0:4] for column in header
          if re.findall("[0-9] Population", column)
      ]

      population_by_year = {}
      for row in reader:
        if row[2] == country:
          union = zip(years, row[5:12])
          population_by_year = {key: int(value) for key, value in union}

      return list(population_by_year.keys()), list(population_by_year.values())
  except Exception as error:
    print(error)
    return None, None


if __name__ == '__main__':
  country = input('Ingrese el nombre del pais: ')
  labels, values = read_csv('./app/data.csv', country)
  charts.generate_bar_chart(labels, values)
