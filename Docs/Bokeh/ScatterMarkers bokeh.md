
## Scatter markers

Bokeh includes a large variety of markers for creating scatter plots. For example, to render circle scatter markers on a plot, use the circle() method of Figure:

```python
from bokeh.plotting import figure, output_file, show

# output to static HTML file
output_file("line.html")

p = figure(width=400, height=400)

# add a circle renderer with a size, color, and alpha
p.circle([1, 2, 3, 4, 5], \
         [6, 7, 2, 4, 5], \
         size= 20, \
         color= "navy", \
         alpha= 0.5)

# show the results
show(p)
```
`#figuresize` `#mark` `#annotation`

