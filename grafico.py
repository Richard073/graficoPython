import plotly
import plotly.graph_objects as go 
fig= go.Figure(
    data=[go.Bar(x=[1,2,3],y=[1,2,3])],
    layout= go.Layout(
        title=dict(text='figura do grafico')
    )
)
fig.show()