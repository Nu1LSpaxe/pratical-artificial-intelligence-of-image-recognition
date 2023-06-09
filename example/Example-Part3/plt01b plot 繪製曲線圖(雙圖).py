## plt01b: plot 繪製曲線圖(兩個圖)
from matplotlib import pyplot as plt #匯入 matplotlib.pyplot
#import matplotlib.pyplot as plt #同上一行
import numpy as np

plt.close('all') #關閉所有視窗
x= np.arange(0, 10, 0.1) #橫軸資料
##------------------------------
y1= x**2 #縱軸資料
fig1= plt.figure() #沒有指定編號, figure會新增, 編號+1
plt.plot(x, y1, linewidth= 4) #繪圖函式,線寬設定
plt.text(1, max(y1)*0.7,'y=x**2', fontsize=16)
plt.title('plot(x,y1)', fontsize=16) #標題
plt.xlabel('x') #橫軸標題
plt.ylabel('y1') #縱軸標題
##------------------------------
y2= x**0.5 #縱軸資料
fig2= plt.figure() #沒有指定編號, figure會新增, 編號+1
plt.plot(x, y2, lw=4, c='r') #繪圖函式,線寬(lw)設定,色彩(c)設定
plt.text(1, max(y2)*0.7,'y=x**0.5', fontsize=16)
plt.title('plot(x,y2)', fontsize=16) #標題
plt.xlabel('x') #橫軸標題
plt.ylabel('y2') #縱軸標題

plt.show() #顯示

## https://matplotlib.org/stable/api/pyplot_summary.html