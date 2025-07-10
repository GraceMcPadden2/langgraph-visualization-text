import plotly.express as px
import pandas as pd

# Sample data frame with incident reports
data = {
    "time of incident": [1633072800, 1633076400, 1633080000, 1633083600, 1633087200],
    "app": ["email", "browser", "email", "email", "browser"],
    "severity": [2, 3, 1, 4, 5]
}

df = pd.DataFrame(data)

# Create the plot
fig = px.histogram(df, x="app", title="Distribution of Incidents by Category")

# Show the plot
fig.show()
