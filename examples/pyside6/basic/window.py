from PySide6.QtWidgets import QMainWindow, QFormLayout, QWidget
from pyqt_advanced_slider import Slider


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)

        # Window settings
        self.resize(360, 145)
        self.setWindowTitle('Advanced Slider Demo')

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

        # Set slider widths and heights
        self.slider_1.setMinimumWidth(100)
        self.slider_2.setMinimumWidth(100)
        self.slider_3.setMinimumWidth(100)
        self.slider_1.setFixedHeight(18)
        self.slider_2.setFixedHeight(18)
        self.slider_3.setFixedHeight(18)

        # Form layout
        form_layout = QFormLayout()
        form_layout.addRow("Slider 1:", self.slider_1)
        form_layout.addRow("Slider 2:", self.slider_2)
        form_layout.addRow("Slider 3:", self.slider_3)
        form_layout.setSpacing(20)
        form_layout.setContentsMargins(20, 20, 20, 20)

        # Set layout
        central_widget = QWidget()
        central_widget.setLayout(form_layout)
        self.setCentralWidget(central_widget)

    def slider_1_value_changed(self, value):
        # Called when slider_1 value changes
        print('[Slider 1]: ' + str(value))

    def slider_2_value_changed(self, value):
        # Called when slider_2 value changes
        print('[Slider 2]: ' + str(value))

    def slider_3_value_changed(self, value):
        # Called when slider_3 value changes
        print('[Slider 3]: ' + str(value))
