import PySimpleGUI as sg

table_data = []
layout_linear_graph = [
    [
        sg.Text(
            "Linear Equation (y = mx + c)",
            expand_x=True,
            font="Georgia 20",
            justification="center",
            pad=(20, 20),
        )
    ],
    [
        sg.Text("m = ", pad=(20, 0)),
        sg.Input(key="-INPUT_M-", size=(5, 1)),
        sg.Text("c = "),
        sg.Input(key="-INPUT_C-", size=(5, 1)),
        sg.Text("First x value = "),
        sg.Input(key="-INPUT_X_START-", size=(5, 1)),
        sg.Text("Last x value = "),
        sg.Input(key="-INPUT_X_END-", size=(5, 1)),
    ],
    [
        sg.Button(
            "Generate Table",
            key="-CREATE_TABLE_LINEAR-",
            pad=(20, 10),
            size=(15, 1)
        ),
        sg.Button(
            "Clear",
            key="-CLEAR_TABLE_LINEAR-",
            pad=(20, 10),
            size=(10, 1)
        ),
    ],
    [
        sg.Table(
            key="-TABLE_LINEAR-",
            headings=["X", "Y"],
            values=table_data,
            justification="center",
            expand_x=True,
            background_color="white",
            text_color="black",
            pad=(20, 10)
        )
    ],
    [
        sg.Button("Generate Graph", key="-CREATE_GRAPH_LINEAR-", pad=(20, 5))
    ],
    [
        sg.Canvas(key="-GRAPH_LINEAR-", pad=(20, 5))
    ]
]
