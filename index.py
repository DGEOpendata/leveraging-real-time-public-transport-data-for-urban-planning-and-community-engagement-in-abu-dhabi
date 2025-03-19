python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load the dataset
transport_data = pd.read_csv('abu_dhabi_transport_usage.csv')

# Convert 'date' column to datetime format
transport_data['date'] = pd.to_datetime(transport_data['date'])

# Filter data for peak hours (7-9 AM and 5-7 PM)
peak_hours_data = transport_data[(transport_data['date'].dt.hour >= 7) & (transport_data['date'].dt.hour <= 9) |
                                  (transport_data['date'].dt.hour >= 17) & (transport_data['date'].dt.hour <= 19)]

# Aggregate data by route
route_usage = peak_hours_data.groupby('route')['passenger_count'].sum().reset_index()

# Plot the data
plt.figure(figsize=(10, 6))
plt.bar(route_usage['route'], route_usage['passenger_count'], color='skyblue')
plt.title('Passenger Count by Route During Peak Hours')
plt.xlabel('Route')
plt.ylabel('Passenger Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Recommendation based on data
most_used_route = route_usage.loc[route_usage['passenger_count'].idxmax()]
print(f"Recommendation: Increase frequency and capacity on Route {most_used_route['route']} due to high passenger count.")
