import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib as mpl
from decimal import *
def plot_eq(f_name,equation,title,col_1="",col_2="",flipped=False,couple=False,num_ticks=5):
    temp = np.loadtxt(f_name,skiprows=4,delimiter=',')
    #print(temp)
    #print(temp.shape)
    
    in_signal = np.vstack((temp[:,0],temp[:,1]))
    out_signal = np.vstack((temp[:,0],temp[:,2]))
    if(couple==True):
        out_signal[1]*=10
    equation_data = np.zeros(in_signal.shape[1])
    i=0;
    for x in in_signal[0,:]:
            equation_data[i]=equation(x)
            #print(x)
            i+=1

            
        #print(x)
    if(flipped==True):
        in_signal= np.vstack((temp[:,0],temp[:,2]))
        out_signal= np.vstack((temp[:,0],temp[:,1]))
    #print(temp[:,1])
    
    fig, ax1 = plt.subplots()
    ax1.set_xlabel("time (s)")
    ax1.set_ylabel("Input signal (V)",color="tab:blue")
    ax1.plot(in_signal[0],in_signal[1],label=col_1,color="tab:blue")
    
    
    ax2=ax1.twinx()
    ax2.plot(out_signal[0],out_signal[1],label=col_2,color="tab:red")
    plt.xlim(min(in_signal[0,:]),max(in_signal[0,:]))
    ticks_dist = -(min(in_signal[0])-max(in_signal[0]))/num_ticks
    plt.xticks(np.arange(min(in_signal[0]),max(in_signal[0]),ticks_dist))
    ax2.set_ylabel("Voltage over Resistor (V)",color="tab:red")
    
    
    
    ax2.plot(out_signal[0],equation_data,color="tab:orange")
    ax2.set_ylim(1.25*min(out_signal[1]),1.25*max(out_signal[1]))
    #plt.xlabel("Seconds")
    #plt.ylabel("Volts")
    plt.title(title)
    #legend = plt.legend()
    
    fig.tight_layout()
    plt.show()
def under_damped(R,L,C,t,v0,debug=False):
    t=Decimal(t)
    R = Decimal(R)
    L = Decimal(L)
    C = Decimal(C)
    v0=Decimal(v0)
    a=R/(Decimal(2)*L)
    w0=Decimal(1)/Decimal.sqrt(L*C)
    wd=Decimal.sqrt(w0*w0-a*a)
    B1=v0/R
    B2=(a*v0)/(wd*R)
    if(debug):
        print(format(B1,".4f")+"e^(-"+format(a,'.4f')+
              "t)*cos("+format(wd,".4f")+"*t)+"+format(B2,".4f")+"e^(-"+format(a,".4f")+"t)*sin("+format(wd,".4f")+"*t)")
    return B1*Decimal.exp(-a*t)*Decimal(math.cos(wd*t))+\
        B2*Decimal.exp(-a*t)*Decimal(math.sin(wd*t))
def eq(t):
    return float(under_damped(1398,0.088,99.6e-9,t-0.00048,-0.5))
plot_eq("scope_14.csv",eq,"Underdamped Response",couple=True,num_ticks=7)
