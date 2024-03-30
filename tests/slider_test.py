from PyQt6.QtCore import Qt, QPoint, QPointF, QEvent, QRect
from PyQt6.QtGui import QFont, QColor, QWheelEvent, QPaintEvent
from PyQt6.QtTest import QTest
from pytestqt.qt_compat import qt_api


from src.pyqt_modern_slider.modern_slider import Slider


def test_initial_values(qtbot):
    """Test initial values after instantiating"""

    slider = Slider()
    qtbot.addWidget(slider)

    default_font = QFont()
    default_font.setFamily('Arial')
    default_font.setPointSize(9)
    default_font.setBold(True)

    assert slider.getMinimum() == 0
    assert slider.getMaximum() == 10
    assert slider.getRange() == (0, 10)
    assert slider.isFloat() == False
    assert slider.getDecimals() == 1
    assert slider.getSingleStep() == 0
    assert slider.getPageStep() == 0
    assert slider.getThousandsSeparator() == ''
    assert slider.getDecimalSeparator() == '.'
    assert slider.getPrefix() == ''
    assert slider.getSuffix() == ''
    assert slider.isShowingValue() == True
    assert slider.getTextColor() == QColor('#000000')
    assert slider.getBackgroundColor() == QColor('#D6D6D6')
    assert slider.getAccentColor() == QColor('#0078D7')
    assert slider.getBorderColor() == QColor('#D1CFD3')
    assert slider.getBorderRadius() == 0
    assert slider.isKeyboardInputEnabled() == True
    assert slider.isMouseWheelInputEnabled() == True
    assert slider.getFont() == default_font
    assert slider.getValue() == 0


def test_set_range_min_max(qtbot):
    """Test setting the range, minimum, and maximum"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-20, 50)

    assert slider.getMinimum() == -20
    assert slider.getMaximum() == 50
    assert slider.getRange() == (-20, 50)

    slider.setMinimum(-10)
    slider.setMaximum(30)

    assert slider.getMinimum() == -10
    assert slider.getMaximum() == 30
    assert slider.getRange() == (-10, 30)


def test_set_float(qtbot):
    """Test setting the slider to a float slider"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setFloat(True)

    assert slider.isFloat() == True
    assert type(slider.getValue()) == float

    slider.setFloat(False)

    assert slider.isFloat() == False
    assert type(slider.getValue()) == int


def test_set_decimals(qtbot):
    """Test setting the decimal places"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setDecimals(3)
    slider.setFloat(True)
    slider.setValue(10)

    assert slider.getValue() == 10.000
    assert slider.getValueFormatted() == '10.000'


def test_set_single_step(qtbot):
    """Test setting the single step"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setSingleStep(3)
    assert slider.getSingleStep() == 3


def test_set_page_step(qtbot):
    """Test setting the page step"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setPageStep(5)
    assert slider.getPageStep() == 5


def test_set_thousands_separator(qtbot):
    """Test setting the thousands separator"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(0, 10000)
    slider.setValue(5000)
    slider.setThousandsSeparator('.')

    assert slider.getThousandsSeparator() == '.'
    assert slider.getValueFormatted() == '5.000'


def test_set_decimal_separator(qtbot):
    """Test setting the decimal separator"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setValue(5)
    slider.setFloat(True)
    slider.setDecimalSeparator(',')

    assert slider.getDecimalSeparator() == ','
    assert slider.getValueFormatted() == '5,0'


def test_set_prefix(qtbot):
    """Test setting the prefix"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setValue(5)
    slider.setPrefix('~')

    assert slider.getPrefix() == '~'
    assert slider.getValueFormatted() == '~5'


def test_set_suffix(qtbot):
    """Test setting the suffix"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setValue(5)
    slider.setSuffix('€')

    assert slider.getSuffix() == '€'
    assert slider.getValueFormatted() == '5€'


def test_show_value(qtbot):
    """Test enabling and disabling the value"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.showValue(False)
    assert slider.isShowingValue() == False

    slider.showValue(True)
    assert slider.isShowingValue() == True


def test_set_text_color(qtbot):
    """Test setting the text color"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setTextColor(QColor('#FFFFFF'))
    assert slider.getTextColor() == QColor('#FFFFFF')


def test_set_background_color(qtbot):
    """Test setting the background color"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setBackgroundColor(QColor('#000000'))
    assert slider.getBackgroundColor() == QColor('#000000')


def test_set_accent_color(qtbot):
    """Test setting the accent color"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setAccentColor(QColor('#008000'))
    assert slider.getAccentColor() == QColor('#008000')


def test_set_border_color(qtbot):
    """Test setting the border color"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setBorderColor(QColor('#2B2B2B'))
    assert slider.getBorderColor() == QColor('#2B2B2B')


def test_set_border_radius(qtbot):
    """Test setting the border radius"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setBorderRadius(5)
    assert slider.getBorderRadius() == 5


def test_set_keyboard_input_enabled(qtbot):
    """Test enabling and disabling keyboard input"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setKeyboardInputEnabled(False)
    assert slider.isKeyboardInputEnabled() == False

    slider.setKeyboardInputEnabled(True)
    assert slider.isKeyboardInputEnabled() == True


def test_set_mouse_wheel_input_enabled(qtbot):
    """Test enabling and disabling mouse wheel input"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setMouseWheelInputEnabled(False)
    assert slider.isMouseWheelInputEnabled() == False

    slider.setMouseWheelInputEnabled(True)
    assert slider.isMouseWheelInputEnabled() == True


def test_set_font(qtbot):
    """Test setting a font"""

    slider = Slider()
    qtbot.addWidget(slider)

    font = QFont()
    font.setFamily('Times')
    font.setPointSize(14)
    font.setBold(True)
    slider.setFont(font)

    assert slider.getFont() == font


def test_set_value(qtbot):
    """Test setting a value"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setValue(5)
    assert slider.getValue() == 5

    # Setting value greater than maximum
    slider.setRange(-100, 100)
    slider.setValue(500)
    assert slider.getValue() == 100

    # Setting value less than minimum
    slider.setValue(-500)
    assert slider.getValue() == -100


def test_get_value_formatted(qtbot):
    """Test getting the formatted value"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setFloat(True)
    slider.setRange(0, 10000)
    slider.setValue(7512.24)
    slider.setDecimals(2)
    slider.setThousandsSeparator(',')
    slider.setPrefix('~')
    slider.setSuffix('€')

    assert slider.getValueFormatted() == '~7,512.24€'


def test_key_press_home(qtbot):
    """Test pressing the home key"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)
    QTest.keyPress(slider, Qt.Key.Key_Home)

    assert slider.getValue() == -50


def test_key_press_end(qtbot):
    """Test pressing the end key"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)
    QTest.keyPress(slider, Qt.Key.Key_End)

    assert slider.getValue() == 50


def test_key_press_default_single_step(qtbot):
    """Test the single step with default value"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)

    # Pressing left arrow key once
    QTest.keyPress(slider, Qt.Key.Key_Left)
    assert slider.getValue() == 4

    # Pressing left arrow key twice
    QTest.keyPress(slider, Qt.Key.Key_Left)
    QTest.keyPress(slider, Qt.Key.Key_Left)
    assert slider.getValue() == 2

    # Pressing down arrow key once
    QTest.keyPress(slider, Qt.Key.Key_Down)
    assert slider.getValue() == 1

    # Pressing down arrow key twice
    QTest.keyPress(slider, Qt.Key.Key_Down)
    QTest.keyPress(slider, Qt.Key.Key_Down)
    assert slider.getValue() == -1

    # Pressing right arrow key once
    QTest.keyPress(slider, Qt.Key.Key_Right)
    assert slider.getValue() == 0

    # Pressing right arrow key twice
    QTest.keyPress(slider, Qt.Key.Key_Right)
    QTest.keyPress(slider, Qt.Key.Key_Right)
    assert slider.getValue() == 2

    # Pressing up arrow key once
    QTest.keyPress(slider, Qt.Key.Key_Up)
    assert slider.getValue() == 3

    # Pressing up arrow key twice
    QTest.keyPress(slider, Qt.Key.Key_Up)
    QTest.keyPress(slider, Qt.Key.Key_Up)
    assert slider.getValue() == 5


def test_key_press_custom_single_step(qtbot):
    """Test the single step with custom value"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setSingleStep(3)
    slider.setValue(5)

    # Pressing left arrow key once
    QTest.keyPress(slider, Qt.Key.Key_Left)
    assert slider.getValue() == 2

    # Pressing left arrow key twice
    QTest.keyPress(slider, Qt.Key.Key_Left)
    QTest.keyPress(slider, Qt.Key.Key_Left)
    assert slider.getValue() == -4

    # Pressing down arrow key once
    QTest.keyPress(slider, Qt.Key.Key_Down)
    assert slider.getValue() == -7

    # Pressing down arrow key twice
    QTest.keyPress(slider, Qt.Key.Key_Down)
    QTest.keyPress(slider, Qt.Key.Key_Down)
    assert slider.getValue() == -13

    # Pressing right arrow key once
    QTest.keyPress(slider, Qt.Key.Key_Right)
    assert slider.getValue() == -10

    # Pressing right arrow key twice
    QTest.keyPress(slider, Qt.Key.Key_Right)
    QTest.keyPress(slider, Qt.Key.Key_Right)
    assert slider.getValue() == -4

    # Pressing up arrow key once
    QTest.keyPress(slider, Qt.Key.Key_Up)
    assert slider.getValue() == -1

    # Pressing up arrow key twice
    QTest.keyPress(slider, Qt.Key.Key_Up)
    QTest.keyPress(slider, Qt.Key.Key_Up)
    assert slider.getValue() == 5


def test_key_press_default_page_step(qtbot):
    """Test the single page with default value"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)

    # Pressing page down key once
    QTest.keyPress(slider, Qt.Key.Key_PageDown)
    assert slider.getValue() == 0

    # Pressing page down key twice
    QTest.keyPress(slider, Qt.Key.Key_PageDown)
    QTest.keyPress(slider, Qt.Key.Key_PageDown)
    assert slider.getValue() == -10

    # Pressing page up key once
    QTest.keyPress(slider, Qt.Key.Key_PageUp)
    assert slider.getValue() == -5

    # Pressing page up key twice
    QTest.keyPress(slider, Qt.Key.Key_PageUp)
    QTest.keyPress(slider, Qt.Key.Key_PageUp)
    assert slider.getValue() == 5


def test_key_press_custom_page_step(qtbot):
    """Test the single page with custom value"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)
    slider.setPageStep(10)

    # Pressing page down key once
    QTest.keyPress(slider, Qt.Key.Key_PageDown)
    assert slider.getValue() == -5

    # Pressing page down key twice
    QTest.keyPress(slider, Qt.Key.Key_PageDown)
    QTest.keyPress(slider, Qt.Key.Key_PageDown)
    assert slider.getValue() == -25

    # Pressing page up key once
    QTest.keyPress(slider, Qt.Key.Key_PageUp)
    assert slider.getValue() == -15

    # Pressing page up key twice
    QTest.keyPress(slider, Qt.Key.Key_PageUp)
    QTest.keyPress(slider, Qt.Key.Key_PageUp)
    assert slider.getValue() == 5


def test_key_press_keyboard_inputs_disabled(qtbot):
    """Test key presses with keyboard inputs disabled"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)
    slider.setKeyboardInputEnabled(False)

    QTest.keyPress(slider, Qt.Key.Key_Down)
    assert slider.getValue() == 5

    QTest.keyPress(slider, Qt.Key.Key_Up)
    assert slider.getValue() == 5

    QTest.keyPress(slider, Qt.Key.Key_Left)
    assert slider.getValue() == 5

    QTest.keyPress(slider, Qt.Key.Key_Right)
    assert slider.getValue() == 5

    QTest.keyPress(slider, Qt.Key.Key_PageDown)
    assert slider.getValue() == 5

    QTest.keyPress(slider, Qt.Key.Key_PageUp)
    assert slider.getValue() == 5


def test_mouse_press_minimum(qtbot):
    """Test pressing the mouse button on the minimum of the slider"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)

    # Left mouse button should change the value
    QTest.mousePress(slider, Qt.MouseButton.LeftButton, pos=QPoint(0, 1))
    assert slider.getValue() == -50

    # Nothing should happen when right or middle mouse buttons are pressed
    slider.setValue(5)
    QTest.mousePress(slider, Qt.MouseButton.MiddleButton, pos=QPoint(0, 1))
    assert slider.getValue() == 5

    slider.setValue(10)
    QTest.mousePress(slider, Qt.MouseButton.RightButton, pos=QPoint(0, 1))
    assert slider.getValue() == 10


def test_mouse_press_maximum(qtbot):
    """Test pressing the mouse button on the maximum of the slider"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)

    # Left mouse button should change the value
    QTest.mousePress(slider, Qt.MouseButton.LeftButton, pos=QPoint(slider.width(), 1))
    assert slider.getValue() == 50

    # Nothing should happen when right or middle mouse buttons are pressed
    slider.setValue(5)
    QTest.mousePress(slider, Qt.MouseButton.MiddleButton, pos=QPoint(slider.width(), 1))
    assert slider.getValue() == 5

    slider.setValue(10)
    QTest.mousePress(slider, Qt.MouseButton.RightButton, pos=QPoint(slider.width(), 1))
    assert slider.getValue() == 10


def test_mouse_press_middle(qtbot):
    """Test pressing the mouse on the exact middle of the slider"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(0, 50)
    slider.setValue(5)

    # Left mouse button should change the value
    QTest.mousePress(slider, Qt.MouseButton.LeftButton, pos=QPoint(int(slider.width() / 2), 1))
    assert slider.getValue() == 25

    # Nothing should happen when right or middle mouse buttons are pressed
    slider.setValue(5)
    QTest.mousePress(slider, Qt.MouseButton.MiddleButton, pos=QPoint(int(slider.width() / 2), 1))
    assert slider.getValue() == 5

    slider.setValue(10)
    QTest.mousePress(slider, Qt.MouseButton.RightButton, pos=QPoint(int(slider.width() / 2), 1))
    assert slider.getValue() == 10


def test_mouse_press_move(qtbot):
    """Test pressing and moving the mouse to the left and right of the slider"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)

    # Left mouse button should change the value
    QTest.mousePress(slider, Qt.MouseButton.LeftButton, pos=QPoint(slider.width(), 1))
    QTest.mouseMove(slider, pos=QPoint(-100, 1))
    assert slider.getValue() == -50

    QTest.mousePress(slider, Qt.MouseButton.LeftButton, pos=QPoint(0, 1))
    QTest.mouseMove(slider, pos=QPoint(slider.width() + 100, 1))
    assert slider.getValue() == 50

    # Nothing should happen when right or middle mouse buttons are pressed
    QTest.mouseRelease(slider, Qt.MouseButton.LeftButton, pos=QPoint(slider.width() + 100, 1))
    slider.setValue(5)
    QTest.mousePress(slider, Qt.MouseButton.MiddleButton, pos=QPoint(slider.width(), 1))
    QTest.mouseMove(slider, pos=QPoint(-100, 1))
    assert slider.getValue() == 5

    slider.setValue(10)
    QTest.mousePress(slider, Qt.MouseButton.RightButton, pos=QPoint(0, 1))
    QTest.mouseMove(slider, pos=QPoint(slider.width() + 100, 1))
    assert slider.getValue() == 10


def test_mouse_release(qtbot):
    """Test releasing the mouse to the left and right of the slider"""

    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)

    # Left mouse button should change the value
    QTest.mouseRelease(slider, Qt.MouseButton.LeftButton, pos=QPoint(-100, 1))
    assert slider.getValue() == -50

    QTest.mouseRelease(slider, Qt.MouseButton.LeftButton, pos=QPoint(slider.width() + 100, 1))
    assert slider.getValue() == 50

    # Nothing should happen when right or middle mouse buttons are pressed
    slider.setValue(5)
    QTest.mouseRelease(slider, Qt.MouseButton.MiddleButton, pos=QPoint(-100, 1))
    assert slider.getValue() == 5

    slider.setValue(10)
    QTest.mouseRelease(slider, Qt.MouseButton.RightButton, pos=QPoint(slider.width() + 100, 1))
    assert slider.getValue() == 10


def test_wheel_event_scroll_up_default_single_step(qtbot):
    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)

    # Simulate mouse wheel event
    wheel_event = QWheelEvent(QPointF(0, 0), slider.mapToGlobal(QPointF(0, 0)),
                              QPoint(10, 10), QPoint(10, 10), Qt.MouseButton.NoButton,
                              Qt.KeyboardModifier.NoModifier, Qt.ScrollPhase.NoScrollPhase, False)
    qt_api.QtWidgets.QApplication.instance().postEvent(slider, wheel_event)

    # Wait for event to be handled by slider before asserting
    QTest.qWait(250)

    assert slider.getValue() == 6


def test_wheel_event_scroll_up_custom_single_step(qtbot):
    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)
    slider.setSingleStep(5)

    # Simulate mouse wheel event
    wheel_event = QWheelEvent(QPointF(0, 0), slider.mapToGlobal(QPointF(0, 0)),
                              QPoint(10, 10), QPoint(10, 10), Qt.MouseButton.NoButton,
                              Qt.KeyboardModifier.NoModifier, Qt.ScrollPhase.NoScrollPhase, False)
    qt_api.QtWidgets.QApplication.instance().postEvent(slider, wheel_event)

    # Wait for event to be handled by slider before asserting
    QTest.qWait(250)

    assert slider.getValue() == 10


def test_wheel_event_scroll_down_default_single_step(qtbot):
    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)

    # Simulate mouse wheel event
    wheel_event = QWheelEvent(QPointF(0, 0), slider.mapToGlobal(QPointF(0, 0)),
                              QPoint(-10, -10), QPoint(-10, -10), Qt.MouseButton.NoButton,
                              Qt.KeyboardModifier.NoModifier, Qt.ScrollPhase.NoScrollPhase, False)
    qt_api.QtWidgets.QApplication.instance().postEvent(slider, wheel_event)

    # Wait for event to be handled by slider before asserting
    QTest.qWait(250)

    assert slider.getValue() == 4


def test_wheel_event_scroll_down_custom_single_step(qtbot):
    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)
    slider.setSingleStep(5)

    # Simulate mouse wheel event
    wheel_event = QWheelEvent(QPointF(0, 0), slider.mapToGlobal(QPointF(0, 0)),
                              QPoint(-10, -10), QPoint(-10, -10), Qt.MouseButton.NoButton,
                              Qt.KeyboardModifier.NoModifier, Qt.ScrollPhase.NoScrollPhase, False)
    qt_api.QtWidgets.QApplication.instance().postEvent(slider, wheel_event)

    # Wait for event to be handled by slider before asserting
    QTest.qWait(250)

    assert slider.getValue() == 0


def test_wheel_event_disabled_wheel_input(qtbot):
    slider = Slider()
    qtbot.addWidget(slider)

    slider.setRange(-50, 50)
    slider.setValue(5)
    slider.setMouseWheelInputEnabled(False)

    # Simulate mouse wheel event
    wheel_event = QWheelEvent(QPointF(0, 0), slider.mapToGlobal(QPointF(0, 0)),
                              QPoint(10, 10), QPoint(10, 10), Qt.MouseButton.NoButton,
                              Qt.KeyboardModifier.NoModifier, Qt.ScrollPhase.NoScrollPhase, False)
    qt_api.QtWidgets.QApplication.instance().postEvent(slider, wheel_event)

    # Wait for event to be handled by slider before asserting
    QTest.qWait(250)

    assert slider.getValue() == 5
