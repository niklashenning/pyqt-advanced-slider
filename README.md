# pyqt-modern-slider
A clean and customizable PyQt5 slider widget for integers and floats

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

```python
...
```

```python
...
```

## Customization
```python
demo_slider.setFloat(True)
demo_slider.setDecimals(2)
```

```python
demo_slider.setPrefix('~')
demo_slider.setSuffix(' €')
```

```python
demo_slider.setDecimalSeparator(',')
demo_slider.setThousandsSeparator('.')
```

```python
demo_slider.setSingleStep(10)
demo_slider.setPageStep(25)
```

```python
demo_slider.setBorderRadius(3)
...
```

## License
This software is licensed under the [MIT license](LICENSE).
