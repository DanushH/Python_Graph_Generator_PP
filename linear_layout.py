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
        sg.Column(
            [
                [
                    sg.Text("m = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_M_LINEAR-", size=(5, 1))],
                [
                    sg.Text("c = ", pad=(22, 0)),
                    sg.Input(key="-INPUT_C_LINEAR-", size=(5, 1))],
                [
                    sg.Text("First x value = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_X_START_LINEAR-", size=(5, 1))],
                [   
                    sg.Text("Last x value = ", pad=(20, 0)),
                    sg.Input(key="-INPUT_X_END_LINEAR-", size=(5, 1))],
    
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
                        background_color="black",
                        text_color="white",
                        pad=(20, 10),
                        size=(40,20)
                    )
                ]
            ]
        ),
        sg.VSeparator(),
        sg.Column(
            [
                [
                    sg.Button(
                        "Generate Graph",
                        key="-CREATE_GRAPH_LINEAR-",
                        pad=(20, 5)
                    ),
                    sg.Button(
                        "Clear Graph",
                        key="-CLEAR_GRAPH_LINEAR-",
                        pad=(20, 5)
                    )
                ],
                [
                    sg.Canvas(key="-GRAPH_LINEAR-", pad=(20, 5))
                ]
            ]
        )
    ]
]
