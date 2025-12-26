import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('study_data.csv')

# The CSV uses the column name exam_score, so select it explicitly
plt.scatter(data.study_hours, data.exam_score)
plt.show()