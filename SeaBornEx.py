import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")

print(tips.head())

sns.set_style("whitegrid")
sns.countplot(x="sex", data=tips)
plt.show()

