from pylab import figure, show
import numpy as np
import matplotlib.pyplot as plt

people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos_hist = np.arange(len(people))
performance = 10*np.random.rand(len(people))

x_for_line = np.linspace(0,10)
y_for_line = np.cos(x_for_line)

fig = figure()
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()



ax2.barh(y_pos_hist, performance, alpha=0.2)
#alpha = 0.2 is what changes the opacity of the bars

plt.yticks(y_pos_hist, people)

plt.show()