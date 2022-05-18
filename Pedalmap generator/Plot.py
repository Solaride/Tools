# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

from data import X, Y

from CsvHandler import writeParameters
from GenerateMap import generateFile

# Vanad
a = 3.9642578909663806e-06
b = -0.00045170711832788447
c = 0.16729706089193364


aSlider, bSlider, cSlider = None, None, None
plot = None

x_data = np.linspace(min(X), max(X), num=513)

fig = None

def f(x, a, b, c):
    return a * x ** 2 + b * x + c

def update(val):
    global plot
    plot.set_ydata(f(x_data, aSlider.val, bSlider.val, cSlider.val))
    fig.canvas.draw_idle()

def reset(event):
    aSlider.reset()
    bSlider.reset()
    cSlider.reset()

def generate(event):
    generateFile(f(x_data, aSlider.val, bSlider.val, cSlider.val))

def saveParameters(event):
    writeParameters(aSlider.val, bSlider.val, cSlider.val)

def init(aVal, bVal, cVal):
    global a, b, c
    global fig, plot
    global aSlider, bSlider, cSlider

    a = aVal
    b = bVal
    c = cVal

    fig, ax = plt.subplots()

    plot, = plt.plot(x_data, f(x_data, a, b, c))

    ax.set_ylim([0, 1])

    ax.set_xlabel('Pedal value')
    ax.set_ylabel('Output value')

    plt.subplots_adjust(bottom=0.35)

    plt.text(0.5, -0.2, "a*x^2+b*x+c")

    aAxis = plt.axes([0.1, 0.2, 0.65, 0.03])
    aSlider = Slider(
        ax=aAxis,
        label="a",
        valmin=a - 3 * abs(a),
        valmax=a + 3 * abs(a),
        valinit=a,
    )

    bAxis = plt.axes([0.1, 0.15, 0.65, 0.03])
    bSlider = Slider(
        ax=bAxis,
        label="b",
        valmin=b - 3 * abs(b),
        valmax=b + 3 * abs(b),
        valinit=b
    )

    cAxis = plt.axes([0.1, 0.1, 0.65, 0.03])
    cSlider = Slider(
        ax=cAxis,
        label="c",
        valmin=c - 3 * abs(c),
        valmax=c + 3 * abs(c),
        valinit=c
    )

    aSlider.on_changed(update)
    bSlider.on_changed(update)
    cSlider.on_changed(update)

    resetAxis = plt.axes([0.8, 0.025, 0.1, 0.04])
    resetButton = Button(resetAxis, 'Reset', hovercolor='0.975')

    saveAxis = plt.axes([0.65, 0.025, 0.1, 0.04])
    saveButton = Button(saveAxis, 'Save', hovercolor='0.975')

    generateAxis = plt.axes([0.45, 0.025, 0.15, 0.04])
    generateButton = Button(generateAxis, 'Generate', hovercolor='0.975')

    resetButton.on_clicked(reset)
    saveButton.on_clicked(saveParameters)
    generateButton.on_clicked(generate)

    plt.show()


def update(val):
    plot.set_ydata(f(x_data, aSlider.val, bSlider.val, cSlider.val))
    fig.canvas.draw_idle()
