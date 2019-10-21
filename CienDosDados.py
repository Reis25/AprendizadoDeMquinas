import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
 

V = [3, 3, 3, 9999, 5, 5, 5]
Va = [ 1, 1, 3, 1, 7, 7, 9, 9, 9, 9, 6, 6, 6, 5, 5, 2, 3]

plt.hist(a)
plt.show()

plt.hist(b)
plt.show()


print('média V: %f mediana V:%f' % (np.mean(a), np.median(a)))
print('média Va: %f mediana Va:%f' % (np.mean(b), np.median(b)))



