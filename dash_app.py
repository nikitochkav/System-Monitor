from dash import Dash, dcc, callback, Input, Output, html
import plotly.graph_objs as go
from monitor import (update_monitor_data, cpu_history, ram_history, disk_history, net_stat_history, temp_history, CPU_COUNT_MONITOR, processor_info, cpu_freq_info, cpu_quantity, memory_info, disk_partitions_info, packets_info)

dash_app = Dash(__name__, requests_pathname_prefix="/dash/", title="System Online")

temperature_sensors_count = len(temp_history)

dash_app.layout = html.Div(
    [
        html.Div(children=processor_info),
        html.Div(children=cpu_freq_info),
        html.Div(children=cpu_quantity),
        dcc.Graph(id="cpu_graph"),
        html.Div(children=memory_info),
        dcc.Graph(id="ram_swap"),
        html.Div(children=disk_partitions_info),
        dcc.Graph(id="disks"),
        html.Div(children=packets_info),
        dcc.Graph(id="net_stat"),
        html.Div([
            html.Div(children=f"Температура системы ({temperature_sensors_count} датчиков)"),
            dcc.Graph(id="temp_graph")
        ]),
        dcc.Interval(id="timer", interval=100),
    ]
)

@callback(
    Output("cpu_graph", "figure"),
    Output("ram_swap", "figure"),
    Output("disks", "figure"),
    Output("net_stat", "figure"),
    Output("temp_graph", "figure"),  
    Input("timer", "n_intervals"),
)
def update(n):
    update_monitor_data()

    cpu_traces = []
    for i in range(CPU_COUNT_MONITOR):
        cpu_traces.append(
            go.Scatter(x=list(range(100)), y=cpu_history[i], mode='lines', name=f"CPU {i}")
        )

    ram_traces = [
        go.Scatter(x=list(range(100)), y=ram_history[0], mode='lines', name="RAM"),
        go.Scatter(x=list(range(100)), y=ram_history[1], mode='lines', name="Swap"),
    ]

    disk_traces = [
        go.Scatter(x=list(range(100)), y=disk_history[0], mode='lines', name="Disk Read"),
        go.Scatter(x=list(range(100)), y=disk_history[1], mode='lines', name="Disk Write"),
    ]

    net_traces = [
        go.Scatter(x=list(range(100)), y=net_stat_history[0], mode='lines', name="Network Sent"),
        go.Scatter(x=list(range(100)), y=net_stat_history[1], mode='lines', name="Network Received"),
    ]

    temp_traces = []
    for i in range(len(temp_history)):
        temp_traces.append(
            go.Scatter(x=list(range(100)), y=temp_history[i], mode='lines', name=f"Temp {i}")
        )

    return {"data": cpu_traces}, {"data": ram_traces}, {"data": disk_traces}, {"data": net_traces}, {"data": temp_traces}
