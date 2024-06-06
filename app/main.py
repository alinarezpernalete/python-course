import utils, read_csv as csv
import charts
import pandas as pd

def run():
  # Read data
  data = csv.read_csv('data.csv')
  # With pandas
  df = pd.read_csv('data.csv')

  # Filter data
  # data = list(filter(lambda x : x["Continent"] == 'South America', data))
  # With pandas
  df = df[df['Continent'] == 'Europe']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart('Europe', countries, percentages)
  
  ################## Example Data ##################
  # data = [{
  #     'Country': 'Colombia',
  #     'Population': 300
  # }, {
  #     'Country': 'Bolivia',
  #     'Population': 500
  # }]

  # keys, values = utils.get_population()
  # print(keys, values)
  # print(utils.var)
  ################### Example Data ##################

  country = input('Input Country => ')
  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    keys, values = utils.get_population(result)  
    charts.generate_bar_chart(country, keys, values)
    charts.generate_pie_chart(country, keys, values)

# Si se ejecuta desde la terminal, se ejecuta el metodo run()
if __name__ == '__main__':
  run()
