import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Simulate ship data
np.random.seed(42)

ship_ids = [f'SHIP_{i:03d}' for i in range(1, 21)]
arrival_dates = pd.date_range(start='2024-01-01', periods=20, freq='2D')
departure_dates = arrival_dates + pd.to_timedelta(np.random.randint(1, 5, size=20), unit='D')
cargo_types = ['Containers', 'Oil', 'Gas', 'Coal', 'General Cargo']
cargo_quantities = np.random.randint(100, 1000, size=20)
statuses = ['Docked', 'Departed']

data = {
    'ShipID': ship_ids,
    'ArrivalDate': arrival_dates,
    'DepartureDate': departure_dates,
    'CargoType': np.random.choice(cargo_types, size=20),
    'CargoQuantity': cargo_quantities,
    'Status': np.random.choice(statuses, size=20)
}

df = pd.DataFrame(data)

# Convert date columns to datetime
df['ArrivalDate'] = pd.to_datetime(df['ArrivalDate'])
df['DepartureDate'] = pd.to_datetime(df['DepartureDate'])

# Calculate the duration of stay
df['Duration'] = (df['DepartureDate'] - df['ArrivalDate']).dt.days

# Show the dataframe
print(df)

# Plotting the number of ships by cargo type
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='CargoType', palette='viridis')
plt.title('Number of Ships by Cargo Type')
plt.xlabel('Cargo Type')
plt.ylabel('Number of Ships')
plt.show()

# Plotting the total cargo quantity by type
plt.figure(figsize=(10, 6))
cargo_quantity = df.groupby('CargoType')['CargoQuantity'].sum().reset_index()
sns.barplot(data=cargo_quantity, x='CargoType', y='CargoQuantity', palette='viridis')
plt.title('Total Cargo Quantity by Type')
plt.xlabel('Cargo Type')
plt.ylabel('Total Cargo Quantity')
plt.show()

# Plotting the duration of stay of ships
plt.figure(figsize=(10, 6))
sns.histplot(df['Duration'], bins=10, kde=True, color='blue')
plt.title('Distribution of Ship Stay Duration')
plt.xlabel('Duration (days)')
plt.ylabel('Frequency')
plt.show()

# Status of ships over time
plt.figure(figsize=(14, 7))
df_sorted = df.sort_values(by='ArrivalDate')
sns.lineplot(data=df_sorted, x='ArrivalDate', y='Status', hue='Status', marker='o')
plt.title('Status of Ships Over Time')
plt.xlabel('Date')
plt.ylabel('Status')
plt.show()

# Average cargo quantity per ship
avg_cargo = df['CargoQuantity'].mean()
print(f'Average Cargo Quantity per Ship: {avg_cargo:.2f}')

# Total duration of ships docked
total_duration = df['Duration'].sum()
print(f'Total Duration of Ships Docked: {total_duration} days')

# Cargo type distribution pie chart
cargo_distribution = df['CargoType'].value_counts()
plt.figure(figsize=(8, 8))
cargo_distribution.plot.pie(autopct='%1.1f%%', colors=sns.color_palette('viridis'))
plt.title('Cargo Type Distribution')
plt.ylabel('')
plt.show()

# Monthly analysis
df['Month'] = df['ArrivalDate'].dt.to_period('M')
monthly_cargo = df.groupby('Month')['CargoQuantity'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_cargo, x='Month', y='CargoQuantity', marker='o', color='green')
plt.title('Monthly Cargo Quantity')
plt.xlabel('Month')
plt.ylabel('Total Cargo Quantity')
plt.xticks(rotation=45)
plt.show()
