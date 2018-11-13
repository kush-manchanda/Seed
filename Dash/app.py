import dash
import dash_core_components as dcc
import dash_html_components as html

from si7021 import get_tempC,get_humidity

from datetime import datetime
import pytz

location_india=pytz.timezone('Asia/Kolkata')
time_india=datetime.now(location_india)
timestamp='{:%H:%M:%S}'.format(time_india)


app =dash.Dash()

app.layout=html.Div(children=[
	html.H1('Dash'),
	dcc.Graph(id='Values',
		figure ={
			'data': [
			{'x':timestamp,'y':get_tempC,'type':'line', 'name':"Temperature"},
			{'x':timestamp,'y':get_humidity,'type':'line', 'name':"Humidity"},
			],
			'layout':{
			'title':PFC values
			}
		}) 
	])

if __name__ == '__main__':
	app.run_server(debug=True)
	