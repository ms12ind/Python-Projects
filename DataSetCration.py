import pandas as pd
import numpy as np

# Number of features
num_features = 10

# Number of records
num_records = 1000

# Generate synthetic data for the employee dataset
data = {
    "Employee_ID": [f"E{i+1:04}" for i in range(num_records)],
    "Name": [f"Employee {i+1}" for i in range(num_records)],
    "Age": np.random.randint(20, 65, size=num_records),
    "Gender": np.random.choice(["Male", "Female"], size=num_records),
    "Department": np.random.choice(["HR", "Finance", "IT", "Marketing"], size=num_records),
    "Position": np.random.choice(["Manager", "Engineer", "Analyst", "Assistant"], size=num_records),
    "Years_of_Experience": np.random.randint(0, 30, size=num_records),
    "Salary": np.random.randint(30000, 150000, size=num_records),
    "Education_Level": np.random.randint(1, 6, size=num_records),  # Assuming a scale from 1 to 5 for simplicity
    "Performance_Rating": np.random.randint(1, 6, size=num_records),  # Assuming a scale from 1 to 5 for simplicity
}

# Create DataFrame
df = pd.DataFrame(data)

# Write DataFrame to CSV file
df.to_csv("employee_dataset.csv", index=False)

