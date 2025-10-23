import pandas as pd
import numpy as np

#Sample data
data = {
    'Feedback': ['Good', 'Bad', 'Better', 'Worst','Best', 'Bad', 'Better', 'Best']
}
df = pd.DataFrame(data)
print("Original Data:\n", df, "\n")

#The order
order_mapping = {
    'Worst': 1,
    'Bad': 2,
    'Good': 3,
    'Better': 4,
    'Best': 5
}

#Encoding the column using list comprehension
df['Feedback_Encoded'] = [order_mapping[val] for val in df['Feedback']]

#Encoded data
print("After Ordinal Encoding:\n", df)
