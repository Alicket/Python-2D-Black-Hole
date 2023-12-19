import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from scipy.integrate import odeint

## 参数设置
# 事件视界半径
R0 = 2
# 光线数量
rays = 36
# 参数
k = 10
# 初始速度
speed = 1

## 绘制黑洞的事件视界
fig,ax=plt.subplots()
EvtHor = patches.Circle((0,0),R0,fill = True,color = 'black')
ax.add_patch(EvtHor)
ax.set_xlim(-30,30)
ax.set_ylim(-15,15)
ax.set_aspect(1)
ax.grid(True)

## 定义二阶常微分方程
def Func(u, t, k):
	x, y, dx, dy = u
	r = np.sqrt(x**2 + y**2)	# 模
	dXdt=-k*x*(1/r**4)
	dYdt=-k*y*(1/r**4)
	if r<= R0:	# 当r<R0时认为落入事件视界，停止计算
		return [0,0,0,0]
	return [dx, dy,dXdt,dYdt]

## on_click 当鼠标点击时触发
def on_click(event):
	if event.button == 1:
		## 每次点击时清除上一次的结果
		ax.cla()
		## 重新绘制事件视界
		EvtHor = patches.Circle((0,0),2,fill = True,color = 'black')
		ax.add_patch(EvtHor)
		ax.set_xlim(-30,30)
		ax.set_ylim(-15,15)
		ax.set_aspect(1)
		ax.grid(True)
		plt.title('Gravitational Lensing in Schwarzschild Black Hole')
		## 获取点击处的坐标
		x0=event.xdata
		y0=event.ydata
		#print(event.xdata,event.ydata)
		## 对于每一条光线：
		for j in range(0,rays):
			# 将初始点划分，发出光线簇
			alpha  = float(j)*np.pi/(rays/2)
			v0=[speed*np.cos(alpha),speed*np.sin(alpha)]
			#print(v0[0],v0[1])
			# 初始条件
			u0 = [x0, y0, v0[0], v0[1]]
			#u0 = [x0, y0, 0.1, 0.1]
	
			# 时间分割
			t = np.linspace(0, 100, 1000)

			# 求解
			u = odeint(Func, u0, t, args=(k, ))

			## 绘制光线
			plt.plot(u[:, 0], u[:, 1],'b',linewidth = 1)
		## 每次点击时绘制新的图像
		fig.canvas.draw()

## 绑定on_click
cid = fig.canvas.mpl_connect('button_press_event',on_click)
plt.title('Gravitational Lensing in Schwarzschild Black Hole')
plt.show()





