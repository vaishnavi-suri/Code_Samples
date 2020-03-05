import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

test_data = pd.read_csv("")

test_data = test_data[["rTargetPosX","rTargetPosY","errorPosX", "errorPosY"]]
df = test_data[test_data['rTargetPosX'].astype(str).str.contains('211')]
indexNames = df[ (df['rTargetPosX'] <= 209)].index
df.drop(indexNames)
df['Distance'] = np.sqrt( (df.rTargetPosX-(df.rTargetPosX - df.errorPosX))**2 + (df.rTargetPosY-(df.rTargetPosY - df.errorPosY))**2)
df.reset_index()

x = df["rTargetPosX"].mean()
y = df["rTargetPosY"].mean()
j = df["errorPosX"].mean()
k = df["errorPosY"].mean()
a = df["errorPosX"].max()
b = df["errorPosY"].max()
c = df["Distance"].std()

with open(r'', 'r') as data_file:
    reader = csv.reader(data_file)
    for fieldnames in reader:
        break

# add row to CSV file
with open(r'', 'a', newline='') as csvfile:
    writer = csv.DictWriter(data_file, fieldnames=fieldnames)
    writer.writerow({'rTargetPosX':x, 'rTargetPosY':y,'errorPosX':j, 'errorPosY':k, 'Max_errorX':a,'Max_errorY':b, 'Distance_Std_Deviation':c})

def main():
    df_quiver = pd.read_csv(" ")
    scale = 1
    fig, axs =plt.subplots(dpi=1200)
    plt.rcParams["legend.fontsize"] = 10
    
    axs.axis('equal')
    axs.set_xlabel("X (mm)")
    axs.set_ylabel("Y (mm)")
    axs.set_xlim(0,215)
    axs.set_ylim(0,130)
    
    for i in range(0, len(df_quiver)):
        axs.quiver(
        [df_quiver["rTargetPosX"][i]],
        [df_quiver["rTargetPosY"][i]],
        df_quiver["errorPosX"][i],
        df_quiver["errorPosY"][i],
        width=0.008,
        scale_units="inches",
        scale=scale, 
        pivot='tip')
             
        
    for _, sample in df_quiver.iterrows():
        x = sample["rTargetPosX"] + sample["errorPosX"] / scale
        y = sample["rTargetPosY"] + sample["errorPosY"] / scale
        
        axs.add_patch(mpl.patches.Circle(
            (x, y), sample["Distance_Std_Deviation"] * 50,
            alpha=0.7, zorder=-1, color='b'))

    plt.savefig(r" ", dpi=1200, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    main()