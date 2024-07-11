#!/usr/bin/env python
import pandas as pd
import requests

# Load the CSV data
data = pd.read_csv('scrobbles.csv')

# Convert utc_time to datetime
data['utc_time'] = pd.to_datetime(data['utc_time'])

# Extract hour
data['hour'] = data['utc_time'].dt.hour

# Group by hour, artist, album, track, and track_mbid
grouped_data = data.groupby(['hour', 'artist', 'album', 'track', 'track_mbid']).size().reset_index(name='count')

# Sort the data by hour and count
sorted_data = grouped_data.sort_values(by=['hour', 'count'], ascending=[True, False])

# Get the top tracks for each hour
top_tracks_by_hour = sorted_data.groupby('hour').head(1)

# Function to fetch BPM from AcousticBrainz API
def fetch_bpm(track_mbid):
    url = f"https://acousticbrainz.org/api/v1/{track_mbid}/low-level"
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'rhythm' in data and 'bpm' in data['rhythm']:
            return data['rhythm']['bpm']
    return None

# Fetch BPM for each leading track
top_tracks_by_hour['bpm'] = top_tracks_by_hour['track_mbid'].apply(fetch_bpm)

# Display the result
print("Most listened tracks by hour with BPM:")
print(top_tracks_by_hour[['hour', 'artist', 'album', 'track', 'bpm']])

