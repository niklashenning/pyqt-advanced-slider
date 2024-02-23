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

> [!NOTE]
> When getting the value of the slider using the `getValue` method or by subscribing to the `valueChanged` event, it will either be an int if the slider is currently an int slider, or a float if the slider is currently a float slider.

## Customization

* To make the slider a float slider, use the `setFloat` method and optionally specify the number of decimal places with the `setDecimals` method:
```python
demo_slider.setFloat(True)  # Default: false
demo_slider.setDecimals(2)  # Default: 1
```

* You can add a prefix and a suffix to the value shown on the slider by using the `setPrefix` and `setSuffix` methods:
```python
demo_slider.setPrefix('~')  # Default: empty string
demo_slider.setSuffix(' €')  # Default: empty string
```

* To customize how the value shown on the slider is formatted, you can use the `setDecimalSeparator` and `setThousandsSeparator` methods:
```python
demo_slider.setDecimalSeparator(',')  # Default: '.'
demo_slider.setThousandsSeparator('.')  # Default: empty string
```
> **Example**: <br>The value `1052.17` formatted with `,` as the decimal separator and `.` as the thousands separator would be `1.052,17`

* To change how much the value is incremented or decremented when the slider is scrolled or the arrow keys are pressed (single step) or the PageUp and PageDown keys are pressed (page step), you can use the `setSingleStep` and `setPageStep` methods:
```python
# If left default, the single step and page step will be 1% and 5% of the slider's value range
demo_slider.setSingleStep(10)  # Default: 0
demo_slider.setPageStep(25)  # Default: 0
```

* If you want to hide the value on the slider completely, you can disable it with the `showValue` method:
```python
demo_slider.showValue(False)  # Default: True
```

* To customize the slider further, you can change the **text color**, **background color**, **accent color**, and **border color** by providing either rgb or hex values, make the corners rounded by setting a **border radius**, and add a custom **font**:
```python
# Make corners rounded
demo_slider.setBorderRadius(3)  # Default: 0

# Set custom colors (you can choose between rgb and hex values for each color)
demo_slider.setTextColorHex('#000000')
demo_slider.setBackgroundColorHex('#FFFFFF')
demo_slider.setAccentColorRgb(100, 100, 100)
demo_slider.setBorderColorRgb(0, 0, 0)

# Set custom font
font = QtGui.QFont()
font.setFamily('Times')
font.setPointSize(10)
font.setBold(True)

demo_slider.setFont(font)
```

## License
This software is licensed under the [MIT license](LICENSE).
