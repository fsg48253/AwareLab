import pandas as pd
import FFix as ff
import os
from pathlib import Path
import csv


pp="ppanda"
ff.fol_prep(pp)

def ppandas(nf=pp, rd="FixedData", globf="*.csv"):
   [print(path) for path in Path(rd).glob(globf)]
   for path in Path(rd).glob(globf):
       data=pd.read_csv(path, names=("EnemyNumber","Time","AngleToEnemy", "DistanceToEnemy"), index_col=False)
       print(data[data["EnemyNumber"]==1])

    #    print(data)

ppandas()