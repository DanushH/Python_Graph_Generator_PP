import PySimpleGUI as sg
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import layouts
import validate_user_input as val

sg.theme("DarkBlack")
sg.set_options(font="Georgia 10")

window = sg.Window(
    "Graph Generator", layouts.layout, finalize=True, size=(800, 650)
)

fig_linear = plt.figure(figsize=(8, 5))
fig_linear.add_subplot(111).grid(True)
figure_canvas_linear = FigureCanvasTkAgg(
    fig_linear, window["-GRAPH_LINEAR-"].TKCanvas)
figure_canvas_linear.draw()
figure_canvas_linear.get_tk_widget().pack()

fig_quadratic = plt.figure(figsize=(8, 5))
fig_quadratic.add_subplot(111).grid(True)
figure_canvas_quadratic = FigureCanvasTkAgg(
    fig_quadratic, window["-GRAPH_QUADRATIC-"].TKCanvas)
figure_canvas_quadratic.draw()
figure_canvas_quadratic.get_tk_widget().pack()

while True:
    event, values = window.read()

    m = values["-INPUT_M-"]
    c = values["-INPUT_C-"]
    x_start = values["-INPUT_X_START-"]
    x_end = values["-INPUT_X_END-"]

    a = values["-INPUT_A-"]
    b = values["-INPUT_B-"]
    c_quad = values["-INPUT_C_QUAD-"]
    x_start_quad = values["-INPUT_X_START_QUAD-"]
    x_end_quad = values["-INPUT_X_END_QUAD-"]

    if event == sg.WIN_CLOSED:
        break

    # linear graph functionality
    if event == "-CREATE_TABLE_LINEAR-":
        # clear previous data
        table_data = []
        window["-TABLE_LINEAR-"].update(table_data)

        if m and c and x_start and x_end:
            x_values, y_values = val.validate_linear(m, c, x_start, x_end)
            table_data.extend([[x, y] for x, y in zip(x_values, y_values)])
            window["-TABLE_LINEAR-"].update(table_data)

    if event == "-CREATE_GRAPH_LINEAR-":
        if m and c and x_start and x_end:
            for ax in fig_linear.axes:
                ax.clear()
            figure_canvas_linear.draw()
            figure_canvas_linear.get_tk_widget().pack()
            x_values, y_values = val.validate_linear(m, c, x_start, x_end)
            axes = fig_linear.axes
            axes[0].grid(True)
            axes[0].plot(x_values, y_values, "g-o")
            figure_canvas_linear.draw()
            figure_canvas_linear.get_tk_widget().pack()

    if event == "-CLEAR_TABLE_LINEAR-":
        window["-INPUT_M-"].update("")
        window["-INPUT_C-"].update("")
        window["-INPUT_X_START-"].update("")
        window["-INPUT_X_END-"].update("")
        window["-TABLE_LINEAR-"].update([])
        for ax in fig_linear.axes:
            ax.clear()
        figure_canvas_linear.draw()
        figure_canvas_linear.get_tk_widget().pack()

    # quadratic graph functionality
    if event == "-CREATE_TABLE_QUADRATIC-":
        # clear previous data
        table_data = []
        window["-TABLE_QUADRATIC-"].update(table_data)

        x_values, y_values = val.validate_quadratic(
            a, b, c_quad, x_start_quad, x_end_quad
        )
        table_data.extend([[x, y] for x, y in zip(x_values, y_values)])
        window["-TABLE_QUADRATIC-"].update(table_data)

    if event == "-CREATE_GRAPH_QUADRATIC-":
        if m and c and x_start and x_end:
            # reomve previous graph
            for ax in fig_quadratic.axes:
                ax.clear()
            figure_canvas_linear.draw()
            figure_canvas_linear.get_tk_widget().pack()

            x_values, y_values = val.validate_quadratic(
                a, b, c_quad, x_start_quad, x_end_quad
            )
            axes = fig_quadratic.axes
            axes[0].grid(True)
            axes[0].plot(x_values, y_values, "g-o")
            figure_canvas_quadratic.draw()
            figure_canvas_quadratic.get_tk_widget().pack()

    if event == "-CLEAR_TABLE_QUADRATIC-":
        window["-INPUT_A-"].update("")
        window["-INPUT_B-"].update("")
        window["-INPUT_C_QUAD-"].update("")
        window["-INPUT_X_START_QUAD-"].update("")
        window["-INPUT_X_END_QUAD-"].update("")
        window["-TABLE_QUADRATIC-"].update([])
        for ax in fig_quadratic.axes:
            ax.clear()
        figure_canvas_quadratic.draw()
        figure_canvas_quadratic.get_tk_widget().pack()

window.close()
