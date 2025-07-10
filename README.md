**Test of langgraph for writing code to visualize data from a user query.**


**Tools:**


get_categories: gets information regarding the categories and type included in the data set.


save_doc: saves python script


**Agents:**
agent_node: generates python script for visualization. 


**Example interaction:**
```
You:  generate code that shows the distribution of incidents by category

Tool call: [{'name': 'get_categories', 'args': {'data': 'incident_reports'}, 'id': 'call_aogCGS2MJajS7z20SopVvmez', 'type': 'tool_call'}]


AI: Based on the given data set information, the data contains the following categories:

- `time of incident`: Integer type
- `app`: String type
- `severity`: Integer type

Since the `app` category is a string type, we will use it to show the distribution of incidents by category. Here is the Python script using Plotly to visualize this:

```python
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

Would you like to save this document?

You: yes

Tool call: [{'name': 'save_doc', 'args': {'script': 'import plotly.express as px\nimport pandas as pd\n\n# Sample data frame with incident reports\ndata = {\n    "time of incident": [1633072800, 1633076400, 1633080000, 1633083600, 1633087200],\n    "app": ["email", "browser", "email", "email", "browser"],\n    "severity": [2, 3, 1, 4, 5]\n}\n\ndf = pd.DataFrame(data)\n\n# Create the plot\nfig = px.histogram(df, x="app", title="Distribution of Incidents by Category")\n\n# Show the plot\nfig.show()\n'}, 'id': 'call_GLRixdWbbqWAqpGpW80KuS45', 'type': 'tool_call'}]


AI: The script has been saved successfully. If you need any further assistance, feel free to ask!

You: 
```
