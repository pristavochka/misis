import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv(r'dataset.csv',sep=';')

df['price']=df['price'].str.replace(',','.')
df['price']=df['price'].astype(float)

plt.scatter(df.area,df.price,color='red')
plt.xlabel('площадь(кв.м.)')
plt.ylabel('стоимость(млн.руб)')
plt.show()

reg = linear_model.LinearRegression()
reg.fit(df[['area']],df.price)

plt.scatter(df.area,df.price,color='red')
plt.xlabel('площадь(кв.м.)')
plt.ylabel('стоимость(млн.руб)')
plt.plot(df.area, reg.predict(df[['area']]))
plt.show()

pred=pd.read_csv(r'prediction_price.csv',sep=';')

p = reg.predict(pred)
pred['predicted prices'] = p

print(pred)

pred.to_excel('new.xlsx', index=False)