import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import numpy as np
from typing import *
from scipy.interpolate import make_interp_spline

def empirical_distr_func(p: Axes, data: List[float]) -> None:
  r"""
  This function draws an emperical distribution function using pyplot from matplotlib.

  Parameters
  ----------

  p: pyplot Axes
  data: List[float]

  Returns
  -------

  Nothing
  """

  plt.title('Выборочная функция распределения')
  plt.xlabel('$x$', fontsize=20)
  plt.ylabel('$F(x)$', fontsize=20)

  p.margins(0.02)

  hist, edges = np.histogram(data, bins=10)
  Y = hist.cumsum() / len(data)

  plt.xticks(edges)
  plt.yticks(Y)

  # Draw support lines (vertical)
  for i in range(len(Y)):
    p.plot([edges[i], edges[i]], [Y[i], 0], linestyle='--', color='gray')
  
  # Draw support lines (horisontal)
  for i in range(len(Y)):
    p.plot([edges[i], min(data)], [Y[i], Y[i]], linestyle='--', color='gray')

  # Draw dashes
  for i in range(len(Y)):
    p.step([edges[i], edges[i+1]],[Y[i], Y[i]], c="red")

  # Draw excluded & included dots
  for i in range(len(Y)):
    p.plot([edges[i]], [Y[i]], marker='.', markeredgecolor='red', markerfacecolor='red', linestyle='none', markersize='8', markeredgewidth=0.5)
    if (i != len(Y)-1):
      p.plot([edges[i+1]], [Y[i]], marker='.', markeredgecolor='red', markerfacecolor='white', linestyle='none', markersize='8', markeredgewidth=0.5)

def histogram_graph(p: Axes, data: List[float]):
  r"""
  This function draws relative frequences histogram and density function using pyplot from matplotlib.

  Parameters
  ----------

  p: pyplot Axes
  data: List[float]

  Returns
  -------

  Nothing
  """
  plt.title('Гистограмма частот')
  plt.xlabel('$x_i$', fontsize=20)
  plt.ylabel('$P_i$', fontsize=20)

  p.margins(0.02)

  densities, bins, _ = p.hist(data, bins=10, color='red', density=True)
  plt.xticks(bins)

  x = np.linspace(bins[0], bins[-1], 10)

  # Draw density function graph using spline-based interpolation
  xnew = np.linspace(x.min(), x.max(), 100)
  spl = make_interp_spline(x, densities, k=3)
  y_smooth = spl(xnew)
  p.plot(xnew, y_smooth)

def freq_polygon(p: Axes, data: List[float]):
  r"""
  This function draws relative frequences polygon using pyplot from matplotlib.

  Parameters
  ----------

  p: pyplot Axes
  data: List[float]

  Returns
  -------

  Nothing
  """
  plt.title('Полигон относительных частот')
  plt.xlabel('$x_i*$', fontsize=20)
  plt.ylabel('$P_i*$', fontsize=20)

  hist, bins = np.histogram(data, bins=10)
  mids = [ (bins[i-1] + bins[i])/2 for i in range(1, len(bins)) ]
  hist = hist / len(data)

  plt.xticks(mids)
  plt.yticks(hist)
  
  p.plot(mids, hist, color='red')