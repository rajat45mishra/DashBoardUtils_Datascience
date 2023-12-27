from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = """
### dashboard builder util generate all posibble stats from Dataframe for DataScience and visualisation purposes

```python
from package.dashboardutil import DashboardElementsBuilder
from package.dataclassifier import DataClassifier
import pandas as pd
df=pd.read_csv("cars.csv")
dat=DataClassifier()
visual=DashboardElementsBuilder(df,dat)
ploats=visual.build_ploats("hist",df.columns.to_list()[1:])
ploat_data=[]
for x in list(ploats):
    for z in list(x):
        ploat_data+=list(z)

```

### above data canbe visualised like below

```python
data={'slow': {'lables': [66.2, 66.4, 66.3, 71.4, 67.9], 'counts': [1, 1, 1, 3, 1]}}
from bokeh.plotting import figure, show

fruits = [str(x) for x in data['slow']['lables']]
counts = data['slow']['counts']

p = figure(x_range=fruits, height=350, title="Range",
           toolbar_location=None, tools="")

p.vbar(x=fruits, top=counts, width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)

```

### export bulk graphs for all possible conditions 

```python
from package.DashBoardsTemplates import export_graphs_hist
from bokeh.plotting import show 
# use any graph for data clustrig or analysis purposes above function using bokeh for bulk visualisation
visual=export_graphs_hist(ploat_data)
# iter visual variable or visualise one by one
show(visual[0])

```



"""
setup(
    name="DashBoardUtils-DataScience",
    version="1.14",
    author="Rajat Mishra",
    author_email="rajatsmishra@aol.com",
    description="AutoMated visualization Features Extraction For Data Scientists and data format calculater for application developers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pandas","bokeh"],
)
