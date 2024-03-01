from PyQt5.QtCore import pyqtSignal, Qt, QRect
from PyQt5.QtGui import QColor, QFont, QPixmap, QBrush, QPen, QPainter, QFontMetrics
from PyQt5.QtWidgets import QWidget, QLabel


class Slider(QWidget):

    # Signal (object, so it can send both int and float)
    valueChanged = pyqtSignal(object)

    def __init__(self, parent=None):
        """Create a new Slider instance

        :param parent: the parent widget
        """

        super(Slider, self).__init__(parent)

        # Init settings
        self.minimum = 0
        self.maximum = 10
        self.is_float = False
        self.decimals = 1
        self.single_step = 0
        self.page_step = 0
        self.thousands_separator = ''
        self.decimal_separator = '.'
        self.prefix = ''
        self.suffix = ''
        self.showing_value = True
        self.text_color = QColor('#000000')
        self.background_color = QColor('#D6D6D6')
        self.accent_color = QColor('#0078D7')
        self.border_color = QColor('#D1CFD3')
        self.border_radius = 0
        self.keyboard_input_enabled = True
        self.mouse_wheel_input_enabled = True

        self.font = QFont()
        self.font.setFamily('Arial')
        self.font.setPointSize(9)
        self.font.setBold(True)

        # Slider value
        self.value = 0.0

        # Slider drag handling
        self.left_mouse_pressed = False

        # Widget that will be turned into a slider
        self.slider = QLabel(self)

        # Position of the slider value on the x-axis (in px)
        self.position_x = None

        # Pixmap for drawing the slider stuff
        self.canvas = QPixmap(self.width(), self.height())
        self.canvas.fill(QColor(self.background_color))
        self.slider.setPixmap(self.canvas)

        # Make focusable
        self.setFocusPolicy(Qt.ClickFocus)

        # Update stylesheet
        self.__update_stylesheet()

        # Call paint event
        self.update()

    def mousePressEvent(self, event):
        """Event that happens every time a mouse button gets pressed on this widget.
        If the left mouse button is being pressed, calculate and set new value

        :param event: the event sent by PyQt
        """

        if event.button() == Qt.LeftButton:
            self.left_mouse_pressed = True
            # Set value and position
            self.value = self.__get_value_from_position_x(event.pos().x())
            self.position_x = self.__clamp_position_x(event.pos().x())
            # Call paint event
            self.update()
            # Emit value changed signal
            self.__emit_value_changed()

    def mouseReleaseEvent(self, event):
        """Event that happens every time a mouse button gets released on this widget.
        If the left mouse button is being released, calculate and set new value

        :param event: the event sent by PyQt
        """

        if event.button() == Qt.LeftButton:
            self.left_mouse_pressed = False
            # Set value and position
            self.value = self.__get_value_from_position_x(event.pos().x())
            self.position_x = self.__clamp_position_x(event.pos().x())
            # Call paint event
            self.update()
            # Emit value changed signal
            self.__emit_value_changed()

    def mouseMoveEvent(self, event):
        """Event that happens every time the mouse gets moved on this widget.
        If the left mouse is being dragged, calculate and set new value

        :param event: the event sent by PyQt
        """

        if self.left_mouse_pressed:
            # Set value and position
            self.value = self.__get_value_from_position_x(event.pos().x())
            self.position_x = self.__clamp_position_x(event.pos().x())
            # Call paint event
            self.update()
            # Emit value changed signal
            self.__emit_value_changed()

    def wheelEvent(self, event):
        """Event that happens every time the mouse wheel is scrolled on this widget.
        Scrolling up increments the slider value by the single step * the amount scrolled.
        Scrolling down decrements the slider value by the single step * the amount scrolled.

        :param event: the event sent by PyQt
        """

        # Check if mouse wheel input is enabled
        if not self.mouse_wheel_input_enabled:
            return

        # Scrolled up
        if event.angleDelta().y() > 0:
            if self.single_step > 0:
                self.setValue(self.__clamp_value(self.value + self.single_step))
            else:
                single_step = self.__get_value_range() * 0.01
                self.setValue(self.__clamp_value(self.value + single_step))

        # Scrolled down
        else:
            if self.single_step > 0:
                self.setValue(self.__clamp_value(self.value - self.single_step))
            else:
                single_step = self.__get_value_range() * 0.01
                self.setValue(self.__clamp_value(self.value - single_step))

    def keyPressEvent(self, event):
        """Event that happens every time a key is pressed on this widget.
        The Home key sets the slider value to the minimum.
        The End key sets the slider value to the maximum.
        The Right and Up arrow keys increment the slider value by the single step.
        The Left and Down arrow keys decrement the slider value by the single step.
        The PageUp key increments the slider value by the page step.
        The PageDown key decrements the slider value by the page step.

        :param event: the event sent by PyQt
        """

        # Check if keyboard input is enabled
        if not self.keyboard_input_enabled:
            return

        # Home key
        if event.key() == Qt.Key_Home:
            self.setValue(self.minimum)

        # End key
        elif event.key() == Qt.Key_End:
            self.setValue(self.maximum)

        # Arrow key (up or right)
        elif event.key() == Qt.Key_Right or event.key() == Qt.Key_Up:
            if self.single_step > 0:
                self.setValue(self.__clamp_value(self.value + self.single_step))
            else:
                single_step = self.__get_value_range() * 0.01
                self.setValue(self.__clamp_value(self.value + single_step))

        # Arrow key (down or left)
        elif event.key() == Qt.Key_Left or event.key() == Qt.Key_Down:
            if self.single_step > 0:
                self.setValue(self.__clamp_value(self.value - self.single_step))
            else:
                single_step = self.__get_value_range() * 0.01
                self.setValue(self.__clamp_value(self.value - single_step))

        # PageUp key
        elif event.key() == Qt.Key_PageUp:
            if self.page_step > 0:
                self.setValue(self.__clamp_value(self.value + self.page_step))
            else:
                page_step = self.__get_value_range() * 0.05
                self.setValue(self.__clamp_value(self.value + page_step))

        # PageDown key
        elif event.key() == Qt.Key_PageDown:
            if self.page_step > 0:
                self.setValue(self.__clamp_value(self.value - self.page_step))
            else:
                page_step = self.__get_value_range() * 0.05
                self.setValue(self.__clamp_value(self.value - page_step))

    def paintEvent(self, event):
        """Event that happens every time a widget needs to update itself.
        All the drawing of the slider happens in here

        :param event: the event sent by PyQt
        """

        # Check if range is valid
        if self.minimum >= self.maximum:
            raise RuntimeError('Slider minimum must be less than maximum')

        # Unset position_x if size changed
        if self.slider.size() != self.size():
            self.position_x = None

        # Calculate position based on value if position_x not set
        if self.position_x is None:
            self.position_x = self.__get_position_x_from_value(self.value)

        # Redraw canvas
        self.slider.setFixedSize(self.width(), self.height())
        self.canvas = QPixmap(self.width(), self.height())
        self.canvas.fill(QColor(self.background_color))
        self.slider.setPixmap(self.canvas)

        # Init painter
        painter = QPainter(self.slider.pixmap())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(self.font)

        # Init pen
        pen = QPen()
        pen.setWidth(1)
        pen.setColor(QColor(self.accent_color))
        painter.setPen(pen)

        # Init brush
        brush = QBrush()
        brush.setColor(QColor(self.accent_color))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        # Draw slider value rect
        if self.position_x > 0:
            # Stuff needed for drawing the rect
            width = self.position_x - 2 if self.position_x + 2 >= self.width() else self.position_x
            height = self.height() - 2
            rect = QRect(0, 1, width, height)
            # Draw rect
            painter.drawRoundedRect(rect, self.border_radius, self.border_radius)

        # Draw slider value
        if self.showing_value:
            # Set pen color to text color
            pen.setColor(self.text_color)
            painter.setPen(pen)

            # Create formatted string from value
            value_string = self.__format_value(self.value, self.is_float, self.decimals,
                                               self.thousands_separator, self.decimal_separator)
            value_string_full = self.prefix + value_string + self.suffix

            # Get string width and height for current font
            metrics = QFontMetrics(self.font)
            text_width = metrics.width(value_string_full)
            text_height = metrics.tightBoundingRect(value_string_full).height()

            # Calculate text position x
            text_margin = 5

            text_pos_x = self.position_x + text_margin
            if text_pos_x + text_width >= self.width() - text_margin:
                text_pos_x = self.width() - text_width - text_margin

            text_pos_x = 1 if text_pos_x == 0 else int(text_pos_x)

            # Calculate text position y
            text_pos_y = int(self.height() - ((self.height() - text_height) / 2))

            # Draw value
            painter.drawText(text_pos_x, text_pos_y, value_string_full)

        # End painter
        painter.end()

    def getValue(self) -> int | float:
        """Get the current value of the slider

        :return: the current value
        """

        # Float
        if self.is_float:
            return round(self.value, self.decimals)
        # Int
        else:
            return int(self.value)

    def getValueFormatted(self) -> str:
        """Get the current formatted value shown on the slider

        :return: the formatted value string
        """

        formatted_value = self.__format_value(self.value, self.is_float, self.decimals,
                                              self.thousands_separator, self.decimal_separator)
        return self.prefix + formatted_value + self.suffix

    def setValue(self, value: int | float):
        """Set the value of the slider

        :param value: the new value
        """

        self.value = self.__clamp_value(value)
        self.position_x = None
        self.update()
        # Emit value changed signal
        self.__emit_value_changed()

    def getMinimum(self) -> int | float:
        """Get the minimum value of the slider

        :return: the minimum value
        """

        return self.minimum

    def setMinimum(self, minimum: int | float):
        """Set the minimum value of the slider

        :param minimum: the new minimum value
        """

        self.minimum = minimum
        self.update()

    def getMaximum(self) -> int | float:
        """Get the maximum value of the slider

        :return: the maximum value
        """

        return self.maximum

    def setMaximum(self, maximum: int | float):
        """Set the maximum value of the slider

        :param maximum: the new maximum value
        """

        self.maximum = maximum
        self.update()

    def getRange(self) -> tuple[int | float, int | float]:
        """Get slider value range (minimum and maximum)

        :return: the minimum and maximum value the slider can have
        """

        return self.minimum, self.maximum

    def setRange(self, minimum: int | float, maximum: int | float):
        """Set slider value range (minimum and maximum)

        :param minimum: the minimum value of the slider
        :param maximum: the maximum value of the slider
        """

        self.minimum = minimum
        self.maximum = maximum

    def isFloat(self) -> bool:
        """Get whether the slider is a float slider

        :return: whether the slider is a float slider
        """

        return self.is_float

    def setFloat(self, use_float: bool):
        """Set whether the slider should be a float slider

        :param use_float: whether the slider should be a float slider
        """

        self.is_float = use_float
        self.update()

    def getDecimals(self) -> int:
        """Get the amount of decimal places of the slider value

        :return: the current amount of decimal places
        """

        return self.decimals

    def setDecimals(self, decimals: int):
        """Set the amount of decimal places of the slider value

        :param decimals: the new amount of decimal places
        """

        self.decimals = decimals
        self.update()

    def getSingleStep(self) -> int | float:
        """Get slider single step

        :return: the current single step
        """

        return self.single_step

    def setSingleStep(self, single_step: int | float):
        """Set slider single step

        :param single_step: the new single step
        """

        self.single_step = single_step

    def getPageStep(self) -> int | float:
        """Get slider page step

        :return: the current page step
        """

        return self.page_step

    def setPageStep(self, page_step: int | float):
        """Set slider page step

        :param page_step: the new page step
        """

        self.page_step = page_step

    def getThousandsSeparator(self) -> str:
        """Get thousands separator of the slider

        :return: the current thousands separator
        """

        return self.thousands_separator

    def setThousandsSeparator(self, thousands_separator: str):
        """Set thousands separator of the slider

        :param thousands_separator: the new thousands separator
        """

        self.thousands_separator = thousands_separator
        self.update()

    def getDecimalSeparator(self) -> str:
        """Get decimal separator of the slider

        :return: the current decimal separator
        """

        return self.decimal_separator

    def setDecimalSeparator(self, decimal_separator: str):
        """Set decimal separator of the slider

        :param decimal_separator: the new decimal separator
        """

        self.decimal_separator = decimal_separator
        self.update()

    def getPrefix(self) -> str:
        """Get slider prefix

        :return: the current prefix
        """

        return self.prefix

    def setPrefix(self, prefix: str):
        """Set slider prefix

        :param prefix: the new prefix
        """

        self.prefix = prefix
        self.update()

    def getSuffix(self) -> str:
        """Get slider suffix

        :return: the current suffix
        """

        return self.suffix

    def setSuffix(self, suffix: str):
        """Set slider suffix

        :param suffix: the new suffix
        """

        self.suffix = suffix
        self.update()

    def isShowingValue(self) -> bool:
        """Get whether the value is shown

        :return: whether the value is being shown
        """

        return self.showing_value

    def showValue(self, on: bool):
        """Set whether the value should be shown

        :param on: whether the value should be shown
        """

        self.showing_value = on

    def getTextColor(self) -> QColor:
        """Get the text color of the slider

        :return: the current text color
        """

        return self.text_color

    def setTextColor(self, color: QColor):
        """Set the text color of the slider

        :param color: the new color
        """

        self.text_color = color
        self.update()

    def getBackgroundColor(self) -> QColor:
        """Get the background color of the slider

        :return: the current background color
        """

        return self.background_color

    def setBackgroundColor(self, color: QColor):
        """Set the background color of the slider

        :param color: the new color
        """

        self.background_color = color
        self.update()

    def getAccentColor(self) -> QColor:
        """Get the accent color of the slider

        :return: the current accent color
        """

        return self.accent_color

    def setAccentColor(self, color: QColor):
        """Set the accent color of the slider

        :param color: the new color
        """

        self.accent_color = color
        self.update()

    def getBorderColor(self) -> QColor:
        """Get the border color of the slider

        :return: the current border color
        """

        return self.border_color

    def setBorderColor(self, color: QColor):
        """Set the border color of the slider

        :param color: the new color
        """

        self.border_color = color
        self.__update_stylesheet()
        self.update()

    def getBorderRadius(self) -> int:
        """Get border radius of the slider

        :return: the current border radius
        """

        return self.border_radius

    def setBorderRadius(self, border_radius: int):
        """Set border radius of the slider

        :param border_radius: the new border radius
        """

        self.border_radius = border_radius
        self.__update_stylesheet()
        self.update()

    def getFont(self) -> QFont:
        """Get font of the slider

        :return: the current font
        """

        return self.font

    def setFont(self, font: QFont):
        """Set font of the slider

        :param font: the new font
        """

        self.font = font

    def isKeyboardInputEnabled(self) -> bool:
        """Get whether keyboard input is enabled

        :return: whether keyboard input is enabled
        """

        return self.keyboard_input_enabled

    def setKeyboardInputEnabled(self, enabled: bool):
        """Set whether keyboard input should be enabled

        :param enabled: whether keyboard input should be enabled
        """

        self.keyboard_input_enabled = enabled

    def isMouseWheelInputEnabled(self) -> bool:
        """Get whether mouse wheel input is enabled

        :return: whether mouse wheel input is enabled
        """

        return self.mouse_wheel_input_enabled

    def setMouseWheelInputEnabled(self, enabled: bool):
        """Set whether mouse wheel input should be enabled

        :param enabled: whether mouse wheel input should be enabled
        """

        self.mouse_wheel_input_enabled = enabled

    def __update_stylesheet(self):
        """Update the stylesheet with the current values"""

        border_color_hex = self.border_color.name()
        self.slider.setStyleSheet('border: 1px solid {}; border-radius: {}px;'
                                  .format(border_color_hex, self.border_radius))

    def __get_value_from_position_x(self, position_x: int) -> int | float:
        """Get slider value from position_x value

        :param position_x: the position_x value
        :return: the slider value
        """

        # Get slider range
        value_range = self.__get_value_range()

        # Calculate value
        value = position_x / self.width() * value_range

        if self.minimum < 0 or self.minimum > 0:
            value = value + self.minimum

        return self.__clamp_value(value)

    def __get_position_x_from_value(self, value: int | float) -> int:
        """Get position_x value from slider value

        :param value: the slider value
        :return: the position_x value
        """

        # Get slider range
        value_range = self.__get_value_range()

        # Calculate x position
        if self.minimum < 0:
            position_x = (value + abs(self.minimum)) * (self.width() / value_range)
        elif self.minimum > 0:
            position_x = (value - self.minimum) * (self.width() / value_range)
        else:
            position_x = value * (self.width() / value_range)

        return int(position_x)

    def __get_value_range(self) -> int | float:
        """Get the range from minimum to maximum of the slider

        :return: the value range
        """

        if self.minimum < 0:
            return self.maximum + abs(self.minimum)
        else:
            return self.maximum - self.minimum

    def __clamp_position_x(self, position_x: int) -> int:
        """Make sure that position_x stays between 0 and slider width

        :param position_x: the position_x value that will get clamped
        :return: the clamped position_x value
        """

        if position_x > self.width():
            position_x = self.width()
        if position_x < 0:
            position_x = 0
        return position_x

    def __clamp_value(self, value: int | float) -> int | float:
        """Make sure that value stays in slider range

        :param value: the value that will get clamped
        :return: the clamped value
        """

        if value > self.maximum:
            value = self.maximum
        if value < self.minimum:
            value = self.minimum
        return value

    def __format_value(self, value: int | float, is_float: bool, decimals: int,
                       thousands_separator: str, decimal_separator: str) -> str:
        """Format value into a string with given settings

        :param value: the value that will get formatted
        :param is_float: if the value should be a float
        :param decimals: the number of decimal places
        :param thousands_separator: the thousands separator
        :param decimal_separator: the decimal separator
        :return: the formatted value as a string
        """

        # Float slider
        if is_float:
            string_format = '{:,.' + str(decimals) + 'f}'
            temp_thousands_separator = '0888019ca0faa9774a728c864e248749'
            temp_decimal_separator = 'f6e9eccf7256112eccd52f41f1fded3f'
            return (string_format.format(value)
                    .replace(',', temp_thousands_separator)
                    .replace('.', temp_decimal_separator)
                    .replace(temp_thousands_separator, thousands_separator)
                    .replace(temp_decimal_separator, decimal_separator))

        # Int slider
        string_format = '{:,.0f}'
        return string_format.format(int(value)).replace(',', thousands_separator)

    def __emit_value_changed(self):
        """Emit signal that the value of the slider has changed"""

        # Float slider
        if self.is_float:
            self.valueChanged.emit(round(self.value, self.decimals))
        # Int slider
        else:
            self.valueChanged.emit(int(self.value))
