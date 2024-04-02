import matplotlib.pyplot as plt
from argparse import ArgumentParser
from util.io import read_csv
from util.stat import *

parser = ArgumentParser()
parser.add_argument('-t', '--type', dest='type', default='none', help="""
  This command selects the current program mode (possible: distr-func, hist or freq-polygon)
""", required=True)
parser.add_argument('-f', '--file', dest='filename', help="""
  This command specifies file to read the dataset from
""", required=True)

"""
  Application entrypoint
"""
if __name__ == '__main__':  
  args = parser.parse_args()
  
  try:
    source = read_csv(args.filename)
    ax = plt.subplot()

    match args.type:
      case 'distr-func': empirical_distr_func(ax, source)
      case 'hist': histogram_graph(ax, source)
      case 'freq-polygon': freq_polygon(ax, source)
      case _: exit('Inappropriate graph type (possible: distr-func, hist or freq-polygon)')

    plt.show() 
  except Exception as e:
    print(e.args[0])
    exit()
