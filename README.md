# PyQt Advanced Slider

[![PyPI](https://img.shields.io/badge/pypi-v1.1.0-blue)](https://pypi.org/project/pyqt-advanced-slider/)
[![Python](https://img.shields.io/badge/python-3.7+-blue)](https://github.com/niklashenning/pyqt-advanced-slider)
[![Build](https://img.shields.io/badge/build-passing-neon)](https://github.com/niklashenning/pyqt-advanced-slider)
[![Coverage](https://img.shields.io/badge/coverage-100%25-green)](https://github.com/niklashenning/pyqt-advanced-slider)
[![License](https://img.shields.io/badge/license-MIT-green)](https://github.com/niklashenning/pyqt-advanced-slider/blob/master/LICENSE)

A clean and customizable int and float slider widget for PyQt and PySide

![pyqt-advanced-slider](https://github.com/niklashenning/pyqt-modern-slider/assets/58544929/b741e06c-1efa-44c8-8c7e-e35ca1c0f348)

## Features
* Supports `int` and `float`
* Supports dynamic switching between types
* Customizable decimal places
* Customizable prefix and suffix
* Customizable decimal separator and thousands separator
* Supports keyboard and mouse wheel inputs
* Modern and customizable UI
* Works with `PyQt5`, `PyQt6`, `PySide2`, and `PySide6`

## Installation
```
pip install pyqt-advanced-slider
```

## Usage
Import the `Slider` class and add it to your window like any other PyQt Widget:
```python
from PyQt6.QtWidgets import QMainWindow
from pyqt_advanced_slider import Slider


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        slider = Slider(self)  # Add slider
        slider.setRange(-50, 100)  # Set min and max
        slider.setValue(25)  # Set value
        slider.valueChanged.connect(self.slider_value_changed)  # Connect change event
    
    # Called every time the slider value changes
    def slider_value_changed(self, value):
        print(value)
```

You can also set the minimum and maximum of the slider individually with the `setMinimum()` and `setMaximum()` methods:
```python
slider.setMinimum(-50)  # Default: 0
slider.setMaximum(100)  # Default: 10
```

The `getValue()` method returns the current value while the `getValueFormatted()` method returns the value as the formatted string that is being displayed on the slider:
```python
value = slider.getValue()  # 2500.0
value_formatted = slider.getValueFormatted()  # e.g. '~2,500.00 €'
```

> **NOTE:** <br>When getting the value of the slider using the `getValue()` method or by subscribing to the `valueChanged` event, it will either be an `int` or a `float`, depending on whether float values are enabled or disabled for the slider.

## Customization

* **Making the slider a float slider:**
```python
slider.setFloat(True)  # Default: False
slider.setDecimals(2)  # Default: 1
```

* **Adding a prefix and a suffix:**
```python
slider.setPrefix('~')   # Default: empty string
slider.setSuffix(' €')  # Default: empty string
```

> **EXAMPLE:** <br>The value `100` formatted with `~` as the prefix and `°` as the suffix would be shown as `~100°`


* **Customizing the formatting of the value shown on the slider:**
```python
slider.setDecimalSeparator(',')    # Default: '.'
slider.setThousandsSeparator('.')  # Default: empty string
```
> **EXAMPLE:** <br>The value `1052.17` formatted with `,` as the decimal separator and `.` as the thousands separator would be `1.052,17`

* **Changing how much the value is incremented or decremented on keyboard and mouse inputs:**
```python
# If left default, the single step and page step will be 1% and 5% of the slider's value range
slider.setSingleStep(10)  # Default: 0
slider.setPageStep(25)    # Default: 0
```

> **SINGLE STEP:** Increment or decrement of the value when the slider is scrolled or the arrow keys are pressed<br>
> **PAGE STEP:** Increment or decrement of the value when the PageUp or PageDown key is pressed

* **Hiding the value on the slider completely:**
```python
slider.showValue(False)  # Default: True
```

* **Enabling or disabling keyboard and mouse wheel input:**
```python
slider.setKeyboardInputEnabled(False)    # Default: True
slider.setMouseWheelInputEnabled(False)  # Default: True
```

* **Setting custom colors:**
```python
slider.setTextColor(QColor('#0F0F0F'))                # Default: #000000
slider.setBackgroundColor(QColor('#FFFFFF'))          # Default: #D6D6D6
slider.setAccentColor(QColor.fromRgb(100, 100, 100))  # Default: #0078D7
slider.setBorderColor(QColor.fromRgb(0, 0, 0))        # Default: #D1CFD3
```

* **Making the corners rounded:**
```python
slider.setBorderRadius(3)  # Default: 0
```

* **Setting a custom font:**
```python
# Init font
font = QFont()
font.setFamily('Times')
font.setPointSize(10)
font.setBold(True)

# Set font
slider.setFont(font)
```

Examples for PyQt5, PyQt6, and PySide6 can be found in the [examples](examples) folder.

## Tests
Installing the required test dependencies [pytest](https://github.com/pytest-dev/pytest), [pytest-qt](https://github.com/pytest-dev/pytest-qt), [coveragepy](https://github.com/nedbat/coveragepy), and [PyQt6](https://pypi.org/project/PyQt6):
```
pip install pytest pytest-qt coverage PyQt6
```

To run the tests with coverage, clone this repository, go into the main directory and run:
```
coverage run -m pytest
coverage report --ignore-errors -m
```

## License
This software is licensed under the [MIT license](LICENSE).
