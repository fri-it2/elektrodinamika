#!/usr/bin/python3
print('*** Animacija zvonjenja voda - S53MV 25.2.2023 ***')

Gamag=-1	#Odbojnost generatorja @z=0
Gamab=1		#Odbojnost bremena @z=l
n=33	#Število točk (integer)
m=28	#Število ponavljanj (integer)

import numpy as np                  #Uporaba učinkovitih funkcij numpy
import matplotlib.pyplot as plt     #Risanje rezultata z matplotlib

w=0	#Števec animacij
d=-2.5	#Odmik časovne skale
z=np.linspace(0,1,n)	#Dolžinska skala
v=np.zeros(n)		#Vpadni val
o=np.zeros(n)		#Odbiti val
t=np.linspace(0,1,n*m)	#Časovna skala
u=np.full(n*m,-99.0)	#Neveljaven izhod

fig,ax=plt.subplots()	#Prvo risanje z normalizacijo matplotlib
ax.plot([0,1],[d,d],'-.k')	#Pikačrta 0(t)
ax.plot([0,1],[d+1,d+1],':k')	#Pikice 1(t)
ax.plot([0,1],[0,0],'-.k')	#Pikačrta 0(z)
ax.plot([0,1],[1,1],':k')	#Pikice 1(z)
lines,=ax.plot(z,v+o,'-y',lw=1)	#Vsota valov=rumena
lineo,=ax.plot(z,o,'-c')	#Odbiti val=zelen
linev,=ax.plot(z,v,'-r')	#Vpadni val=rdeč
linec,=ax.plot(z,o,'--c')	#Odbiti črtkani
lineu,=ax.plot(t,u,'-b')	#U(t,z=l) izhod=moder
plt.title(r'Zvonjenje voda pri  $\Gamma_g=$'+str(Gamag)+'  $\Gamma_b=$'+str(Gamab))
plt.axis([0,1,-2.7,2.2])
plt.xticks([0,1],['Vir','Breme'])
plt.yticks([d,d+1,d+2,0,1,2],['0','Ug','2Ug','0','Ug','2Ug'])
plt.legend([lines,lineo,linev,lineu],['Vsota valov','Odbiti val','Vpadni val','Izhod(t,z=l)'])

while w<n*m and plt.waitforbuttonpress(0.01)==None:	#Zanka animacije
	v=np.roll(v,1)			#Vpadni naprej
	oo=o[0]				#Stari odbiti
	o[0]=Gamab*v[0]			#Odboj na koncu voda
	u[w]=v[0]+o[0]+d		#U(t,z=l)
	v[0]=(1-Gamag)/2+oo*Gamag	#Generator+odboj na začetku
	o=np.roll(o,-1)			#Odbiti nazaj
	lines.set_ydata(v+o)	#Vsota valov
	lineo.set_ydata(o)	#Odbiti val
	linev.set_ydata(v)	#Vpadni val
	linec.set_ydata(o)	#Odbiti črtkani
	lineu.set_ydata(u)	#U(t,z=l) izhod
	w+=1			#Povečaj števec animacij
	fig.canvas.draw()	#Ponovno risanje

plt.show()		#Slika ostane na zaslonu
print('*** Konec ***')	#Izhod=pritisk tipke/miške
