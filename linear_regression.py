import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('datasets/Salary_dataset.csv')

# SImple csv data loading
plt.scatter(data.YearsExperience, data.Salary, color='blue')
# plt.title('Experience vs Salary')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.show()

def loss_function(): # same as "mean square error"
    pass