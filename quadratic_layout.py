import PySimpleGUI as sg

table_data = []
layout_quadratic_graph = [
    [
        sg.Text(
            "Quadratic Equation (y = ax² +bx + c)",
            expand_x=True,
            font="Georgia 20",
            justification="center",
            pad=(20, 20),
        )
    ],
    [
        sg.Text("a = ", pad=(20, 0)),
        sg.Input(key="-INPUT_A-", size=(5, 1)),
        sg.Text("b = ", pad=(20, 0)),
        sg.Input(key="-INPUT_B-", size=(5, 1)),
        sg.Text("c = "),
        sg.Input(key="-INPUT_C_QUAD-", size=(5, 1)),
        sg.Text("First x value = "),
        sg.Input(key="-INPUT_X_START_QUAD-", size=(5, 1)),
        sg.Text("Last x value = "),
        sg.Input(key="-INPUT_X_END_QUAD-", size=(5, 1))
    ],
    [
        sg.Button(
            "Generate Table",
            key="-CREATE_TABLE_QUADRATIC-",
            pad=(20, 10),
            size=(15, 1)
        ),
        sg.Button(
            "Clear",
            key="-CLEAR_TABLE_QUADRATIC-",
            pad=(20, 10),
            size=(10, 1)
        ),
    ],
    [
        sg.Table(
            key="-TABLE_QUADRATIC-",
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
        sg.Button(
            "Generate Graph",
            key="-CREATE_GRAPH_QUADRATIC-",
            pad=(20, 5)
        )
    ],
    [
        sg.Canvas(key="-GRAPH_QUADRATIC-", pad=(20, 5))
    ]
]
