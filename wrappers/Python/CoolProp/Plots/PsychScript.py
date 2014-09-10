
import numpy, matplotlib
from CoolProp.HumidAirProp import HAPropsSI
from CoolProp.Plots.Plots import InlineLabel 

p = 101325
Tdb = numpy.linspace(-10,60,100)+273.15

#Make the figure and the axes
fig=matplotlib.pyplot.figure(figsize=(10,8))
ax=fig.add_axes((0.1,0.1,0.85,0.85))

# Saturation line
w = [HAPropsSI('W','T',T,'P',p,'R',1.0) for T in Tdb]
ax.plot(Tdb-273.15,w,lw=2)

# Humidity lines
RHValues = [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
for RH in RHValues:
    w = [HAPropsSI('W','T',T,'P',p,'R',RH) for T in Tdb]
    ax.plot(Tdb-273.15,w,'r',lw=1)

# Humidity lines
for H in [-20000, -10000, 0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]:
    #Line goes from saturation to zero humidity ratio for this enthalpy
    T1 = HAPropsSI('T','H',H,'P',p,'R',1.0)-273.15
    T0 = HAPropsSI('T','H',H,'P',p,'R',0.0)-273.15
    w1 = HAPropsSI('W','H',H,'P',p,'R',1.0)
    w0 = HAPropsSI('W','H',H,'P',p,'R',0.0)
    ax.plot(numpy.r_[T1,T0],numpy.r_[w1,w0],'r',lw=1)

ax.set_xlim(Tdb[0]-273.15,Tdb[-1]-273.15)
ax.set_ylim(0,0.03)
ax.set_xlabel(r"Dry bulb temperature [$^{\circ}$C]")
ax.set_ylabel(r"Humidity ratio ($m_{water}/m_{dry\ air}$) [-]")

xv = Tdb #[K]
for RH in [0.05, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]:
    yv = [HAPropsSI('W','T',T,'P',p,'R',RH) for T in Tdb]
    y = HAPropsSI('W','P',p,'H',65.000000,'R',RH)
    T_K,w,rot = InlineLabel(xv, yv, y=y, axis = ax)
    string = r'$\phi$='+str(RH*100)+'%'
    bbox_opts = dict(boxstyle='square,pad=0.0',fc='white',ec='None',alpha = 0.5)
    ax.text(T_K-273.15,w,string,rotation = rot,ha ='center',va='center',bbox=bbox_opts)

matplotlib.pyplot.show()
