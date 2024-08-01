import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv("C:\\Users\\User\\OneDrive\\Desktop\\repo\\cars_ds_final.csv")
mpg=data['mpg']
plt.hist(mpg,color='k',edgecolor='c')
plt.xlabel('Miles per gallon (mpg)')
plt.ylabel('Frequency')
plt.title("Frequency distribution of mpg")
plt.show()

wt=data['wt'] 
iv=range(len(data)) 
plt.scatter(iv,mpg,color='k',label='mpg') 
plt.scatter(iv,wt,color='g',label='wt') 
plt.title("Relationship b/w Weight and MPG") 
plt.legend() 
plt.show() 

c=data['am'].value_counts()
plt.xticks([0,1],['0-Automatic','1-Manual'])
plt.bar(c.index,c.values,color=('k','g'),width=0.3)
plt.xlabel("Transmission type")
plt.ylabel("Frequency")
plt.title("Frequency distribution of transmission type of cars")
plt.legend()
plt.show()

sns.boxplot(mpg,color='c')
plt.xlabel("Miles per gallon (mpg)")
plt.ylabel("Frequency")
plt.title("Frequency distribution for mpg of cars")
plt.legend()
plt.show()