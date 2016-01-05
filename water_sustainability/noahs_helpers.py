from bokeh.charts import Bar, output_file, show
from bokeh.plotting import figure, show, output_file, hplot, vplot
from bokeh.models.widgets import CheckboxButtonGroup
from bokeh.models import Callback,ColumnDataSource,Slider,Range1d
from bokeh.io import output_file, show, vform
import numpy as np
N = 1000
x = np.linspace(0,4,N)
y1 = np.cos(x)
y2 = np.sinc(x)
y3 = np.exp(-x)
t = x[0]
y0 = [0,0,0]
source = ColumnDataSource(data=dict(x=x,y0=y0, y1=y1,y2=y2,y3=y3,points = [y1[t],y2[t],y3[t]],num = [1,2,3],color = ['red','green','blue'], t = [t,t,t]))



p1 = figure(title='Value at Current Time',tools="save",
       background_fill="#E8DDCB", width=500, height=500)

p1.circle('num', 'points', color='color', size=20, source=source)
p1.segment('num', 'y0', 'num','points', source = source,line_width=5, line_color='color')
output_file("bar.html")

p1.y_range = Range1d(-1.2, 1.2)
p2 = figure(title="Test Plots",tools="save",
       background_fill="#E8DDCB", width=500, height=500)
#p2.line(x,y1,line_color="red", line_width=8, alpha=0.7, legend="linear")
#p2.line(x,y2,line_color="blue", line_width=8, alpha=0.7, legend="squared")
#p2.line(x,y3,line_color="green", line_width=8, alpha=0.7, legend="exponential")
p2.circle('t', 'points', color='color', size=10, source=source)
p2.line('x', 'y1', source=source, line_width=3, line_alpha=0.6, line_color = 'red', legend = 'Cosine')
p2.line('x', 'y2', source=source, line_width=3, line_alpha=0.6, line_color = 'green', legend = 'Sinc')
p2.line('x', 'y3', source=source, line_width=3, line_alpha=0.6, line_color = 'blue', legend = 'Exponential')
p2.xaxis.axis_label = 't'
p2.yaxis.axis_label = 'f(t)'

cb = Callback(args=dict(source=source), code="""
        var data = source.get('data');
        var f = cb_obj.get('value')
        x = data['x']
        y1 = data['y1']
        y2 = data['y2']
        y3 = data['y3']
        t = data['t']
        points = data['points']
        points[0] = y1[f]
        points[1] = y2[f]
        points[2] = y3[f]
        t[0] = x[f]
        t[1] = x[f]
        t[2] = x[f]
        x = data['x']
        source.trigger('change');
    """)
slider = Slider(start=0, end=N-1, value=0, step=1, title="Time", callback=cb)

radbg = CheckboxButtonGroup(labels=["Cosine", "Sinc", "Exponential"], active=[1,1,1])
print(radbg.active)
show(vplot(slider,radbg,hplot(p2,p1)))
