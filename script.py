import pandas as pd
import plotly.express as px

# Sample incident data, replace it with your actual data
data = {
 'severity': [1, 2, 2, 3, 3, 3, 4, 5, 1, 2, 3, 4, 5] # Example severity levels
}

# Creating DataFrame
df = pd.DataFrame(data)

# Creating histogram for incident severity distribution
fig = px.histogram(df, x='severity', title='Incident Severity Distribution')

# Display the plot
fig.show()