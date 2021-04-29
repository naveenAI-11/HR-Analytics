import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%pwd
f_train=pd.read_csv('Downloads/archive/aug_train.csv')
f_test=pd.read_csv('Downloads/archive/aug_test.csv')

list(f_train.columns)
list(f_test.columns)

f_train.isnull().sum().sort_values(ascending=False)
f_train.shape
f_train.head()

f_train.dropna(axis=0,how="any",inplace=True)

looking_for_job=f_train["target"].value_counts()
looking_for_job

gender1=f_train[(f_train['target']==1)]
gender1.head()

gender2=gender1['gender'].value_counts()
gender2.plot.pie(figsize = (6,6) ,autopct='%1.2f%%' ,  colors = ["red" , "green" , "yellow" ] , 
                title = 'Gender looking for a new job')
plt.show()

gender3=gender1['relevent_experience'].value_counts()
gender3.plot.pie(figsize = (6,6),autopct='%1.2f%%',colors=["red" , "green"],title = 'Experienced professionals looking for a new job')
plt.show()

enroled_university=gender1['enrolled_university'].value_counts()
enroled_university.plot.bar(title='Enrolled in university',color=['red','black','blue'])
plt.ylabel('number of people')

import matplotlib.gridspec as gridspec
import seaborn as sns
figure,axes=plt.subplots(nrows=2,ncols=2,figsize=(14,14))

#topleft
tl=gender1['education_level'].value_counts()
tl1=tl.to_dict()
labels = list(tl1.keys())
values = list(tl1.values())
axes[0,0].pie(values, labels=labels,autopct='%1.1f%%',startangle=160)
axes[0,0].set_title('Education_Level')

#topright
exp=gender1['experience'].value_counts()
exp1=exp.to_dict()
n=list(exp1.keys())
v=list(exp1.values())
my_colors = 'rgbkymc'
axes[0,1].bar(n,height=v,color=my_colors)
axes[0,1].set_ylabel('number_of_people')
axes[0,1].set_title('Experience')

#bottomleft
sns.distplot(gender1["training_hours"] ,rug=True, color = 'green' , ax = axes[1,0],norm_hist=True,axlabel=False)
for i in ["bottom", "left" ]:
    axes[1,0].spines[i].set_visible(True)
    axes[1,0].set_title('Training_Hours')
    axes[1,0].set_ylabel('Density')
plt.show()

#bottomright
new=tolist()
axes[1,1].scatter(x = gender1['last_new_job'], y = gender1['experience'])
axes[1,1].xlabel("experience")
axes[1,1].ylabel("last new job")
plt.show()

sns.set(rc={'figure.figsize':(30,30)})
sns.relplot(data=gender1,x="major_discipline", y="company_type", col="last_new_job",style="relevent_experience")

