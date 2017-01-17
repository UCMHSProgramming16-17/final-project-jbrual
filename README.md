# Final Project - Intro to Programming 2016-2017

## Setup:

* Accept the invitation for the git repository
* Clone to your computer
* Create 'readme.md'
* Commit and push - this way I can see who's having trouble setting up git
* Activate your 'data' environment using ```source activate data```

## Overview:

Your final project is to visualize data using Python and Bokeh. You may use any data you wish, as long as it is appropriate for school. I will help with sample data.

## Technical Skills Involved

* Accessing an API and/or reading from a published dataset
* Assessing data
* Creating visualizations

## Expectations

* Visualizations are relevant and helpful in understanding data
* Multiple visualizations should be present, unless a particularly challenging and informative individual visualization merits including only one
* Your work should challenge you
* Git is used appropriately

## Deliverables

* Python programs that created your visualizations (ie ```chart1.py```, ```bargraph.py```, or any other appropriately named python files)
* Copies of your data
* The visualizations created by your program

# Process

## Step 1 - Find Data

If you need help sourcing data, let me know. I can help

## Step 2 - How are you planning to visualize the data?

* Take a look around the [Bokeh Gallery](http://bokeh.pydata.org/en/latest/docs/gallery.html#gallery)
* In a file called ```vis-ideas.md```, list some ideas for how you want to visualize your data
* You won't necessarily get to all of them, but that's okay
* Try to include some you might not necessarily know how to do yet
* To create a bulleted list, use an asterisk at the start of the line, and have a blank line before the list

## Step 3 - Start experimenting

* You might want to start with some testing in interactive mode
* You have examples in the .ipynb file I've included in this repo
* The [Bokeh User Guide](http://bokeh.pydata.org/en/latest/docs/user_guide.html) and [Bokeh Reference](http://bokeh.pydata.org/en/latest/docs/reference.html) are very helpful

Remember imports. You might not need numpy, but you'll almost certainly need pandas

```python
import pandas as pd
import numpy as np
```

Importing bokeh will depend heavily on what you're doing with it

```python
# For basic plotting of symbols
from bokeh.plotting import figure, output_file, save

# For Line charts
from bokeh.charts import Line, output_file, save
# If you want a different type of chart, replace Line with the type you want
```

To create a DataFrame named ```df``` from a csv file named ```data.csv```:

```python
df = pd.read_csv('data.csv')
```

To create a DataFrame named ```df2``` from an excel file named ```datal.xls```:

```python
df2 = pd.read_excel('data1.xls')
```