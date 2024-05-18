import utils, read_csv as csv
import charts

def run():
  data = csv.read_csv('./app/data.csv')
  data = list(filter(lambda x : x["Continent"] == 'South America', data))
  
  # Example Data
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

  country = input('Input Country => ')
  result = utils.population_by_country(data, country)
  
  if len(result) > 0:
    keys, values = utils.get_population(result)  
    charts.generate_bar_chart(country, keys, values)
    charts.generate_pie_chart(country, keys, values)

# Si se ejecuta desde la terminal, se ejecuta el metodo run()
if __name__ == '__main__':
  run()
