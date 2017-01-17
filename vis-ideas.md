Visualization Ideas

* Bar Graph
* Scatter Plot

Use the README.md to import everything for everything to work.
df = pd.read_csv('Speeds.csv')
bar = Bar(df, values='Speed', label='Pokemon', sort='disabled', agg='sum', legend=False, title="Flying Pokemon Speed Data", width=2000)