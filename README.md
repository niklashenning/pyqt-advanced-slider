# pyqt-modern-slider
A clean and customizable PyQt5 slider widget for integer and float values

![pyqt-modern-slider](https://github.com/niklashenning/pyqt-modern-slider/assets/58544929/b741e06c-1efa-44c8-8c7e-e35ca1c0f348)

## Features
* Supports `int` and `float`
* Supports dynamic switching between types
* Customizable decimal places
* Customizable prefix and suffix
* Customizable decimal separator and thousands separator
* Supports keyboard and mouse wheel input
* Modern and customizable UI

## Installation
Download the **modern_slider.py** file from the **src** folder and add it to your project

## Usage
Import the `Slider` class and add it to your window like any other PyQt Widget:
```python
from PyQt5.QtWidgets import QMainWindow
from modern_slider import Slider


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        demo_slider = Slider(self)  # Add slider
        demo_slider.setRange(-50, 100)  # Set min and max
        demo_slider.setValue(25)  # Set value
        demo_slider.valueChanged.connect(self.slider_value_changed)  # Connect change event
    
    # Called every time the slider value changes
    def slider_value_changed(self, value):
        print(value)
```

You can also set the minimum and maximum of the slider individually with the `setMinimum` and `setMaximum` methods:
```python
demo_slider.setMinimum(-50)
demo_slider.setMaximum(100)
```

The `getValue` method returns the current value as an int or float while the `getValueFormatted` method returns the value as the formatted string that is being displayed on the slider:
```python
value = demo_slider.getValue()  # 2500.0
value_formatted = demo_slider.getValueFormatted()  # '~2,500.00 €'
```

> [!NOTE]
> When getting the value of the slider using the `getValue` method or by subscribing to the `valueChanged` event, it will either be an `int` or a `float`, depending on whether float values are enabled for the slider.

## Customization

* **Making the slider a float slider:**
```python
demo_slider.setFloat(True)  # Default: false
demo_slider.setDecimals(2)  # Default: 1
```

* **Adding a prefix and a suffix:**
```python
demo_slider.setPrefix('~')  # Default: empty string
demo_slider.setSuffix(' €')  # Default: empty string
```

> **EXAMPLE**: <br>The value `100` formatted with `~` as the prefix and `°` as the suffix would be shown as `~100°`


* **Customizing the formatting of the value shown on the slider:**
```python
demo_slider.setDecimalSeparator(',')  # Default: '.'
demo_slider.setThousandsSeparator('.')  # Default: empty string
```
> **EXAMPLE**: <br>The value `1052.17` formatted with `,` as the decimal separator and `.` as the thousands separator would be `1.052,17`

* **Changing how much the value is incremented or decremented on keyboard and mouse inputs:**
```python
# If left default, the single step and page step will be 1% and 5% of the slider's value range
demo_slider.setSingleStep(10)  # Default: 0
demo_slider.setPageStep(25)  # Default: 0
```

> **SINGLE STEP:** Increment or decrement of the value when the slider is scrolled or the arrow keys are pressed<br>
> **PAGE STEP:** Increment or decrement of the value when the PageUp or PageDown key is pressed

* **Hiding the value on the slider completely:**
```python
demo_slider.showValue(False)  # Default: True
```

* **Setting the text color, background color, accent color, border color, border radius, and font:**
```python
# Making corners rounded
demo_slider.setBorderRadius(3)  # Default: 0

# Setting custom colors (you can choose between rgb and hex values for each color)
demo_slider.setTextColorHex('#000000')
demo_slider.setBackgroundColorHex('#FFFFFF')
demo_slider.setAccentColorRgb(100, 100, 100)
demo_slider.setBorderColorRgb(0, 0, 0)

# Setting custom font
font = QtGui.QFont()
font.setFamily('Times')
font.setPointSize(10)
font.setBold(True)

demo_slider.setFont(font)
```

More in-depth examples can be found in the [examples](examples) folder

## License
This software is licensed under the [MIT license](LICENSE).
