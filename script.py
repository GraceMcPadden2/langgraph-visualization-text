import plotly.express as px
import pandas as pd

# Sample data
data = {
    "time of incident": [20200101, 20200102, 20200103, 20200104, 20200105],
    "app": ["App1", "App2", "App1", "App3", "App2"],
    "severity": [1, 3, 2, 4, 1]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Converting 'time of incident' to a datetime object
df['time of incident'] = pd.to_datetime(df['time of incident'], format='%Y%m%d')

# Plotting
fig = px.line(df, x='time of incident', y='severity', title='Incident Reports Over Time',
              labels={'time of incident': 'Time of Incident', 'severity': 'Severity'})

fig.show()
