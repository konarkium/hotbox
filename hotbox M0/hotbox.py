import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib as mpl


#fix font to 14 and make it so it's editable PDF
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['font.size'] = 14

#grab data
filename = 'hotbox.csv'
df = pd.read_csv(filename)

#pull data from CSV
xPt = df['Pt'].dropna()
yPhb = df['Phb'].dropna()
yPcb = df['Pcb'].dropna()

xPMt = df['PMt'].dropna()
yPMhb = df['PMhb'].dropna()
yPMcb = df['PMcb'].dropna()

xPEMt = df['PEMt'].dropna()
yPEMhb = df['PEMhb'].dropna()
yPEMcb = df['PEMcb'].dropna()

#Set the limits of the plot
xmin = 0
xmax = 130

fig = plt.figure(1, figsize=(5,5))

plt.xlim([xmin,xmax])

PP, = plt.plot(xPt, yPhb, label = 'PP', marker = 's', markersize = 0, c = 'black', linestyle = 'dotted')
plt.plot(xPt, yPhb, label = 'PP hot box', c = 'red', linestyle = 'dotted')
plt.plot(xPt, yPcb, label = 'PP cold box', c = 'blue', linestyle = 'dotted')

PM, = plt.plot(xPMt, yPMhb, label = 'PM', marker = 's', markersize = 0, c = 'black', linestyle = 'dashed')
plt.plot(xPMt, yPMhb, label = 'PM hot box', c = 'red', linestyle = 'dashed')
plt.plot(xPMt, yPMcb, label = 'PM cold box', c = 'blue', linestyle = 'dashed')

PEM, = plt.plot(xPEMt, yPEMhb, label = 'PEM', marker = 's', markersize = 0, c = 'black')
plt.plot(xPEMt, yPEMhb, label = 'PEM hot box', c = 'red')
plt.plot(xPEMt, yPEMcb, label = 'PEM cold box', c = 'blue')

plt.axhline(y=55, color = 'black', linestyle = '-.', alpha = 0.5)
plt.text(50,49,'SA melting point')

plt.minorticks_on()
plt.tick_params(which='minor', direction='in', length=5, 
                bottom=True, top=False, left=True, right=False)
plt.tick_params(which='major', direction='in', length=10, 
                bottom=True, top=False, left=True, right=False)
plt.tick_params(labelbottom=True, labeltop=False, 
                labelright=False, labelleft=True)

#first auto legend
red_patch = mpatches.Patch(color='red', label='hot chamber')
blue_patch = mpatches.Patch(color='blue', label='cold chamber')
leg1 = plt.legend(handles =[red_patch, blue_patch], bbox_to_anchor =(1,0.75))
plt.gca().add_artist(leg1)

plt.legend((PP,PM,PEM),['PP','PM','PEM'], bbox_to_anchor =(1,0.55))


plt.xlabel('Time (min)')
plt.ylabel('Temperature ($^o$C)')

plt.savefig('hotbox.png', dpi=300,bbox_inches="tight")




















