Test of langgraph for writing code to visualize data from a user query.

Tools:
get_categories: gets information regarding the categories and type included in the data set.

Agents:
agent_node: generates python script for visualization. 

Example interaction:
```

You: generate code that shows the distribution of incidents by category

Tool call: [{'name': 'get_categories', 'args': {'data': 'incident_reports'}, 'id': 'call_HIbEBTvfclsMMiW8uLhluHi1', 'type': 'tool_call'}]


AI: Based on the data set information, the categories we have are 'time of incident', 'app', and 'severity'. To show the distribution of incidents by category, it makes sense to visualize the distribution of incidents by 'app', since it is a categorical variable. Here is the code to achieve that using Plotly:

python
import pandas as pd
import plotly.express as px

# Sample data assuming you have incident data as a CSV file
data = {
    'time of incident': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'app': ['App A', 'App B', 'App A', 'App C', 'App B', 'App A', 'App C', 'App B', 'App A', 'App C'],
    'severity': [2, 3, 2, 4, 2, 1, 5, 3, 4, 3]
}

df = pd.DataFrame(data)

# Plotting the distribution of incidents by app category
fig = px.histogram(df, x='app', title='Distribution of Incidents by App Category', labels={'app':'App Category', 'count':'Number of Incidents'}, color='app')

fig.show()


This code snippet assumes you have incident data which includes 'time of incident', 'app', and 'severity'. Adjust the sample data loading mechanism as per your actual data source.

You: 
```
