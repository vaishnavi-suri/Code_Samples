# -*- coding: utf-8 -*-

from tqdm import tqdm
import numpy as np 
import pandas as pd
import os

root_train = ''
root_test = ''

def datasplit_train_test(root):
    allfiles =[]
    split=[]
    with tqdm(total=300) as pbar:
        for root, dirs, files in os.walk(root):
            data = [os.path.join(root,f) for f in files if f.endswith(".txt")]
            for file in data:
                dest = file.split("\\")  
                classification = dest[-2]
                s = "\\\\"
                dest= s.join(dest)
                frame = pd.read_csv(str(dest), delim_whitespace=True,header=0, index_col=0,skiprows=9)
                frame['classification']= classification
                frame=frame.loc[:, ~frame.columns.str.replace("(\.\d+)$", "").duplicated()]
                df = pd.DataFrame(data = frame)
                weld_data = df.drop(['Time','P-Ref+','Plasma','Error','P-Ref-','P-MW','T-Ref+','T-Ref-','T-MW','T-Raw','R-Ref+','Refl','R-Ref-','R-MW'],axis=1)
                weld1 = a[0:708]
                split.append(weld1)
                weld2 = a[708:1416]
                split.append(weld2)
                weld3 = a[1410:2118]          
                split.append(weld3)
            pbar.update()
        pbar.close()
        print("All done importing")
    return split

def labels(labelArray):
    lbl=[]
    for weld in labelArray:
        label=[]
        lbl.append(CLASSES[weld[0]])
    a = np.reshape(np.array(lbl),(-1,1))
    return a

def reshape(data):
    x = [a[['P','T','R']].to_numpy() for a in data]
    y = np.array(x)
    z = np.reshape(y,(-1,708,3))
    return z