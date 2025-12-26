import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('datasets/Salary_dataset.csv')

# SImple csv data loading
plt.scatter(data.YearsExperience, data.Salary, color='blue')
# plt.title('Experience vs Salary')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.show()

def loss_function(m, b, points): # same as "mean square error", 
    # tell us how much we're off from the actual value
    # we don't actually use it in the final optimization process,
    # what we're actually intersted in is minimizng it
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].YearsExperience
        y = points.iloc[i].Salary
        total_error += (y - (m * x + b)) ** 2
    total_error / float(len(points))

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)