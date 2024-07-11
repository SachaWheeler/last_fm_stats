#!/usr/bin/env python
import pandas as pd

# Load the CSV data
data = pd.read_csv('scrobbles.csv')

# Convert utc_time to datetime
data['utc_time'] = pd.to_datetime(data['utc_time'])

# Extract hour
data['hour'] = data['utc_time'].dt.hour

# Group by hour, artist, album, and track
grouped_data = data.groupby(['hour', 'artist', 'album', 'track']).size().reset_index(name='count')

# Sort the data by hour and count
sorted_data = grouped_data.sort_values(by=['hour', 'count'], ascending=[True, False])

# Get the top tracks for each hour
top_tracks_by_hour = sorted_data.groupby('hour').head(3)

# Display the result
print("Most listened tracks by hour:")
print(top_tracks_by_hour[['hour', 'artist', 'album', 'track']].to_string())
