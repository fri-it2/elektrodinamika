#!/usr/bin/python3
print('*** Animacija trčenja valov - S53MV 26.2.2023 ***')

n=1000	#Število točk (integer)
m=200	#Širina signalov (integer)

import numpy as np                  #Uporaba učinkovitih funkcij numpy
import matplotlib.pyplot as plt     #Risanje rezultata z matplotlib
z=np.linspace(0,1,n)	#Dolžinska skala
v=np.zeros(n)		#Vpadni val
o=np.zeros(n)		#Odbiti val

def signal():	#Signal pravokotni+polval
	j=0
	while j<m:
		v[j]=0.8
		o[n-j-1]=np.sin(j/m*np.pi)
		j+=1
	return

fig,ax=plt.subplots()	#Prvo risanje z normalizacijo matplotlib
ax.plot([0,1],[-3,-3],'--k')	#Črtice 0(Wm)
ax.plot([0,1],[-2,-2],'-.k')	#Pikačrta 0(i)
ax.plot([0,1],[-1,-1],'--k')	#Črtice 0(We)
ax.plot([0,1],[0,0],'-.k')	#Pikačrta 0(u)
signal()	#Prvi signal
lineu,=ax.plot(z,v+o,'-r')		#Vsota=napetost
linee,=ax.plot(z,(v+o)*(v+o)/2-1,'-m')	#Vsota^2=el.w
linei,=ax.plot(z,v-o-2,'-c')		#Razlika=tok
linem,=ax.plot(z,(v-o)*(v-o)/2-3,'-b')	#Razlika^2=mag.w
plt.title('Trčenje valov @ Rk=1')
plt.axis([0,1,-3.5,2])
plt.xticks([0.5],['z'])
plt.yticks([-3,-2,-1,0],['Wm(z)','i(z)','We(z)','u(z)'])
plt.legend([lineu,linee,linei,linem],['Napetost','El.W/l','Tok','Mag.W/l'])

while plt.waitforbuttonpress(0.01)==None:	#Zanka animacije
	v=np.roll(v,1)	#Vpadni naprej
	v[0]=0		#Ničla na začetek vpada
	o[0]=0		#Ničla na konec odboja
	o=np.roll(o,-1)	#Odbiti nazaj
	lineu.set_ydata(v+o)			#Vsota=napetost
	linee.set_ydata((v+o)*(v+o)/2-1)	#Vsota^2=el.w
	linei.set_ydata(v-o-2)			#Razlika=tok
	linem.set_ydata((v-o)*(v-o)/2-3)	#Razlika^2=mag.w
	fig.canvas.draw()	#Ponovno risanje
	if np.amax(v)<0.001:	#Nov signal?
		signal()

print('*** Konec ***')	#Izhod=pritisk tipke/miške
