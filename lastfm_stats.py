#!/usr/bin/env python
import pandas as pd

# Load the CSV data
data = pd.read_csv('scrobbles.csv')

# Convert utc_time to datetime
data['utc_time'] = pd.to_datetime(data['utc_time'])

# Extract hour and day_of_week
data['hour'] = data['utc_time'].dt.hour
data['day_of_week'] = data['utc_time'].dt.day_name()

# Most listened albums and artists by hour
artist_hourly = data.groupby(['hour', 'artist']).size().reset_index(name='count')
artist_hourly = artist_hourly.sort_values(by=['hour', 'count'], ascending=[True, False])

album_hourly = data.groupby(['hour', 'album']).size().reset_index(name='count')
album_hourly = album_hourly.sort_values(by=['hour', 'count'], ascending=[True, False])

track_hourly = data.groupby(['hour', 'track']).size().reset_index(name='count')
track_hourly = track_hourly.sort_values(by=['hour', 'count'], ascending=[True, False])

top_artists_by_hour = artist_hourly.groupby('hour').head(1)
top_albums_by_hour = album_hourly.groupby('hour').head(1)
top_tracks_by_hour = track_hourly.groupby('hour').head(1)

print("Top artists by hour:")
print(top_artists_by_hour)

print("\nTop albums by hour:")
print(top_albums_by_hour)

print("\nTop tracks by hour:")
print(top_tracks_by_hour)

# Most listened albums and artists by day of the week
artist_daily = data.groupby(['day_of_week', 'artist']).size().reset_index(name='count')
artist_daily = artist_daily.sort_values(by=['day_of_week', 'count'], ascending=[True, False])

album_daily = data.groupby(['day_of_week', 'album']).size().reset_index(name='count')
album_daily = album_daily.sort_values(by=['day_of_week', 'count'], ascending=[True, False])

top_artists_by_day = artist_daily.groupby('day_of_week').head(1)
top_albums_by_day = album_daily.groupby('day_of_week').head(1)

print("Top artists by day of the week:")
print(top_artists_by_day)

print("\nTop albums by day of the week:")
print(top_albums_by_day)

