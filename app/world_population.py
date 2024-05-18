import csv
import charts


def find_world_population(path):
  try:
    with open(path, 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter=',')
      wp_percentage_index = len(next(reader)) - 1

      labels = []
      values = []
      for row in reader:
        labels.append(row[1])
        values.append(row[wp_percentage_index])

    return labels, values
  except Exception as error:
    print(error)
    return None, None


if __name__ == '__main__':
  labels, values = find_world_population('app/data.csv')
  charts.generate_pie_chart(labels, values)
