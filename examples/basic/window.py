from PyQt5.QtWidgets import QMainWindow, QLabel
from src.modern_slider import Slider


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        # Window settings
        self.setFixedSize(360, 145)
        self.setWindowTitle('Modern Slider Demo')

        # Add labels for the hotkey pickers
        self.label_1 = QLabel(self)
        self.label_1.setText('Slider 1:')
        self.label_1.move(48, 16)

        # Label for slider 2
        self.label_2 = QLabel(self)
        self.label_2.setText('Slider 2:')
        self.label_2.move(48, 53)

        # Label for slider 3
        self.label_3 = QLabel(self)
        self.label_3.setText('Slider 3:')
        self.label_3.move(48, 90)

        # Slider 1
        self.slider_1 = Slider(self)
        self.slider_1.setRange(100, 500)  # Set slider min and max
        self.slider_1.setValue(375)  # Set slider value
        self.slider_1.valueChanged.connect(self.slider_1_value_changed)  # Connect change event

        # Slider 2
        self.slider_2 = Slider(self)
        self.slider_2.setRange(-500.0, 2500.0)  # Set slider min and max
        self.slider_2.setValue(100.0)  # Set slider value
        self.slider_2.setFloat(True)  # Change to float slider
        self.slider_2.setDecimals(2)  # Show 2 decimal places
        self.slider_2.setPrefix('~')  # Add slider value prefix
        self.slider_2.setSuffix(' €')  # Add slider value suffix
        self.slider_2.setThousandsSeparator(',')  # Add thousands separator
        self.slider_2.setSingleStep(50)  # Set custom single step value
        self.slider_2.setPageStep(250)  # Set custom page step value
        self.slider_2.valueChanged.connect(self.slider_2_value_changed)  # Connect change event

        # Slider 3
        self.slider_3 = Slider(self)
        self.slider_3.setRange(-1.0, -0.1)  # Set slider min and max
        self.slider_3.setValue(-0.552)  # Set slider value
        self.slider_3.setFloat(True)  # Change to float slider
        self.slider_3.setDecimals(3)  # Show 3 decimal places
        self.slider_3.setSuffix('°')  # Add slider value suffix
        self.slider_3.valueChanged.connect(self.slider_3_value_changed)  # Connect change event

        # Using fixed size and position for simplicity since this is just a demo
        self.slider_1.setFixedSize(200, 18)
        self.slider_1.move(110, 23)
        self.slider_2.setFixedSize(200, 18)
        self.slider_2.move(110, 60)
        self.slider_3.setFixedSize(200, 18)
        self.slider_3.move(110, 97)

    def slider_1_value_changed(self, value):
        # Called when slider_1 value changes
        print('[Slider 1]: ' + str(value))

    def slider_2_value_changed(self, value):
        # Called when slider_2 value changes
        print('[Slider 2]: ' + str(value))

    def slider_3_value_changed(self, value):
        # Called when slider_3 value changes
        print('[Slider 3]: ' + str(value))
