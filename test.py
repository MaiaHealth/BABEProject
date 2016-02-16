import matplotlib.pyplot as plt
import numpy as np

sheetRooms=[1, 2, 9, 10, 12, 13, 14, 15, 19, 21, 26, 27, 29, 30, 31, 32, 34, 39]
roomDict={1: 30.518518518518519, 2: 69.796875, 3: 11.365853658536585, 33: 53.350000000000001, 7: 3.7142857142857144, 13: 37.18181818181818, 14: 5.0, 34: 10.388888888888889, 19: 8.4285714285714288, 21: 5.0, 25: 53.666666666666664, 26: 1.0, 29: 5.117647058823529}
sheetDict={32: 3.4268292682926829, 1: 1.7142857142857142, 2: 3.4186046511627906, 39: 1.375, 15: 1.25, 9: 2.0, 10: 2.1546391752577319, 12: 4.7735849056603774, 34: 2.8333333333333335, 14: 1.0, 13: 1.8, 19: 2.2777777777777777, 21: 3.7619047619047619, 26: 1.2857142857142858, 27: 1.927710843373494, 29: 1.8245614035087718, 30: 1.6515151515151516, 31: 1.0}

combinedRooms = []
combinedSensor = []
combinedSheet = []
for x in sheetRooms:
	if (x in roomDict):
		combinedRooms.append(x);
		combinedSensor.append(roomDict[x])
		combinedSheet.append(sheetDict[x])

ind = np.arange(len(combinedRooms))
width = 0.4

fig, ax = plt.subplots()
rects1 = ax.bar(ind, combinedSensor, width, color='r')
rects2 = ax.bar(ind + width, combinedSheet, width, color='y')


ax.set_ylabel('Room Usage')
ax.set_title('Lactation room usage')
ax.set_xticks(ind + width)
ax.set_xticklabels(combinedRooms)

ax.legend((rects1[0], rects2[0]), ('Sensor', 'Log-in Sheet'))

plt.show()


