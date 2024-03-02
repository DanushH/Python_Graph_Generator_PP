import PySimpleGUI as sg
import linear_layout as lin
import quadratic_layout as quad
import cubic_layout as cub

linear_graph_layout = lin.layout_linear_graph
quadratic_graph_layout = quad.layout_quadratic_graph
cubic_graph_layout = cub.layout_cubic_graph

layout = [
    [sg.TabGroup([
        [
            sg.Tab("Linear Graph", linear_graph_layout),
            sg.Tab("Quadratic Graph", quadratic_graph_layout),
            sg.Tab("Cubic Graph", cubic_graph_layout)
        ]
    ])]
]
