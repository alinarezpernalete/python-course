# def get_population(country):
  # keys = ['col', 'bol']
  # values = [300, 500]
  # return keys, values

# var = "Hola Mundo"
import re
def get_population(country):
  population = []
  year = []
  for x in country[0]:
    if re.findall("[0-9] Population", x):
      population.append(country[0][x])
      year.append(x[0:4])

  union = zip(year, population)
  population_by_year = {key: int(value) for key, value in union}
  return list(population_by_year.keys()), list(population_by_year.values())

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result