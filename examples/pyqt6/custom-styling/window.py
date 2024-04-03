import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor, QColor
from PyQt6.QtWidgets import QMainWindow, QLabel, QWidget, QPushButton
from pyqt_advanced_slider import Slider


class Window(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)

        # Needed for window drag functionality
        self.offset = None

        # Frameless transparent window
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setFixedSize(360, 200)

        # Widget as window so everything can be customized
        self.window = QWidget(self)
        self.window.setFixedSize(self.size())
        self.window.setObjectName('window')

        # Window title bar
        self.window_bar = QWidget(self)
        self.window_bar.setFixedSize(360, 32)
        self.window_bar.move(0, 1)
        self.window_bar.setObjectName('window_bar')

        # Window title
        self.window_title = QLabel(self)
        self.window_title.setText('Advanced Slider Demo')
        self.window_title.setFixedSize(150, 20)
        self.window_title.move(125, 6)
        self.window_title.setObjectName('window_title')

        # Close button
        self.close_button = QPushButton(self)
        self.close_button.setText('✕')
        self.close_button.setFixedSize(22, 22)
        self.close_button.move(331, 5)
        self.close_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.close_button.setObjectName('close_button')
        self.close_button.clicked.connect(self.close_button_pressed)

        # Label for slider 1
        self.label_1 = QLabel(self)
        self.label_1.setText('Slider 1:')
        self.label_1.move(40, 51)
        self.label_1.setObjectName('label_1')

        # Label for slider 2
        self.label_2 = QLabel(self)
        self.label_2.setText('Slider 2:')
        self.label_2.move(40, 83)
        self.label_2.setObjectName('label_2')

        # Label for slider 3
        self.label_3 = QLabel(self)
        self.label_3.setText('Slider 3:')
        self.label_3.move(40, 114)
        self.label_3.setObjectName('label_3')

        # Label for slider 4
        self.label_4 = QLabel(self)
        self.label_4.setText('Slider 4:')
        self.label_4.move(40, 145)
        self.label_4.setObjectName('label_4')

        # Slider 1
        self.slider_1 = Slider(self)
        self.slider_1.setValue(6)  # Set slider value
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
        self.slider_2.setBorderRadius(3)  # Rounded corners
        self.slider_2.setAccentColor(QColor('#f0921f'))  # Orange accent color
        self.slider_2.valueChanged.connect(self.slider_2_value_changed)  # Connect change event

        # Slider 3
        self.slider_3 = Slider(self)
        self.slider_3.setRange(-1.0, -0.1)  # Set slider min and max
        self.slider_3.setValue(-0.552)  # Set slider value
        self.slider_3.setFloat(True)  # Change to float slider
        self.slider_3.setDecimals(3)  # Show 3 decimal places
        self.slider_3.setSuffix('°')  # Add slider value suffix
        self.slider_3.setBorderRadius(5)  # Rounded corners
        self.slider_3.setAccentColor(QColor('#a033e8'))  # Purple slider color
        self.slider_3.valueChanged.connect(self.slider_3_value_changed)  # Connect change event

        # Slider 4
        self.slider_4 = Slider(self)
        self.slider_4.setRange(-150.0, 300.0)  # Set slider min and max
        self.slider_4.setValue(12.5)  # Set slider value
        self.slider_4.setFloat(True)  # Change to float slider
        self.slider_4.setBorderRadius(3)  # Rounded corners
        self.slider_4.setAccentColor(QColor('#666666'))  # Dark gray accent color
        self.slider_4.setBorderColor(QColor('#999999'))  # Gray border color
        self.slider_4.valueChanged.connect(self.slider_4_value_changed)  # Connect change event

        # Using fixed size and position for simplicity since this is just a demo
        self.slider_1.setFixedSize(200, 16)
        self.slider_1.move(110, 59)
        self.slider_2.setFixedSize(200, 18)
        self.slider_2.move(110, 89)
        self.slider_3.setFixedSize(200, 18)
        self.slider_3.move(110, 120)
        self.slider_4.setFixedSize(200, 18)
        self.slider_4.move(110, 151)

    def slider_1_value_changed(self, value):
        # Called when slider_1 value changes
        print('[Slider 1]: ' + str(value))

    def slider_2_value_changed(self, value):
        # Called when slider_2 value changes
        print('[Slider 2]: ' + str(value))

    def slider_3_value_changed(self, value):
        # Called when slider_3 value changes
        print('[Slider 3]: ' + str(value))

    def slider_4_value_changed(self, value):
        # Called when slider_4 value changes
        print('[Slider 4]: ' + str(value))

    def close_button_pressed(self):
        # Exit application on close button press
        sys.exit()

    def mousePressEvent(self, event):
        # Window drag functionality
        if event.button() == Qt.MouseButton.LeftButton and self.window_bar.geometry().contains(event.pos()):
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        # Window drag functionality
        if self.offset is not None and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        # Window drag functionality
        self.offset = None
        super().mouseReleaseEvent(event)
