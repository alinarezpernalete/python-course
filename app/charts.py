import matplotlib.pyplot as plt
from pathlib import Path

def generate_bar_chart(name, labels, values):
  directory = Path("./imgs")

  if not directory.exists():
      directory.mkdir(parents=True, exist_ok=True)
  
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f"./imgs/{name}.png")


def generate_pie_chart(name, labels, values):
  directory = Path("./imgs")

  if not directory.exists():
      directory.mkdir(parents=True, exist_ok=True)

  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')  # Mantiene el circulo equitativo
  plt.savefig(f"./imgs/{name}.png")


if __name__ == '__main__':
  labels = ['A', 'B', 'C']
  values = [1, 2, 3]
  #generate_bar_chart(labels, values)
  #generate_pie_chart(labels, values)
