from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSignal, Qt
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
        self.float = False
        self.decimals = 1
        self.single_step = 0
        self.page_step = 0
        self.thousands_seperator = ''
        self.decimal_seperator = '.'
        self.prefix = ''
        self.suffix = ''
        self.display_value = True
        self.text_color = QtGui.QColor('#000000')
        self.background_color = QtGui.QColor('#D6D6D6')
        self.accent_color = QtGui.QColor('#0078D7')
        self.border_color = QtGui.QColor('#D1CFD3')
        self.border_radius = 0

        self.font = QtGui.QFont()
        self.font.setFamily('Arial')
        self.font.setPointSize(9)
        self.font.setBold(True)

        # Slider value
        self.value = 0.0

        # Slider drag handling
        self.mouse_pressed = False

        # Widget that will be turned into a slider
        self.slider = QLabel(self)

        # Position of the slider value on the x-axis (in px)
        self.position_x = None

        # Pixmap for drawing the slider stuff
        self.canvas = QtGui.QPixmap(self.width(), self.height())
        self.canvas.fill(QtGui.QColor(self.background_color))
        self.slider.setPixmap(self.canvas)

        # Make focusable
        self.setFocusPolicy(Qt.ClickFocus)

        # Update stylesheet
        self.__update_stylesheet()

        # Call paint event
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = True
            # Set value and position
            self.value = self.__get_value_from_position_x(event.pos().x())
            self.position_x = self.__clamp_position_x(event.pos().x())
            # Call paint event
            self.update()
            # Emit value changed signal
            self.__emit_value_changed()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.mouse_pressed = False
            # Set value and position
            self.value = self.__get_value_from_position_x(event.pos().x())
            self.position_x = self.__clamp_position_x(event.pos().x())
            # Call paint event
            self.update()
            # Emit value changed signal
            self.__emit_value_changed()

    def mouseMoveEvent(self, event):
        if self.mouse_pressed:
            # Set value and position
            self.value = self.__get_value_from_position_x(event.pos().x())
            self.position_x = self.__clamp_position_x(event.pos().x())
            # Call paint event
            self.update()
            # Emit value changed signal
            self.__emit_value_changed()

    def wheelEvent(self, event):
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
        self.canvas = QtGui.QPixmap(self.width(), self.height())
        self.canvas.fill(QtGui.QColor(self.background_color))
        self.slider.setPixmap(self.canvas)

        # Init painter
        painter = QtGui.QPainter(self.slider.pixmap())
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setFont(self.font)

        # Init pen
        pen = QtGui.QPen()
        pen.setWidth(1)
        pen.setColor(QtGui.QColor(self.accent_color))
        painter.setPen(pen)

        # Init brush
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor(self.accent_color))
        brush.setStyle(Qt.SolidPattern)
        painter.setBrush(brush)

        # Draw slider value rect
        if self.position_x > 0:
            # Stuff needed for drawing the rect
            width = self.position_x - 2 if self.position_x + 2 >= self.width() else self.position_x
            height = self.height() - 2
            rect = QtCore.QRect(0, 1, width, height)
            # Draw rect
            painter.drawRoundedRect(rect, self.border_radius, self.border_radius)

        # Draw slider value
        if self.display_value:
            # Set pen color to text color
            pen.setColor(self.text_color)
            painter.setPen(pen)

            # Create formatted string from value
            value_string = self.__format_value(self.value, self.float, self.decimals,
                                               self.thousands_seperator, self.decimal_seperator)
            value_string_full = self.prefix + value_string + self.suffix

            # Get string width and height for current font
            metrics = QtGui.QFontMetrics(self.font)
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

    def getValue(self):
        # Float
        if self.float:
            return round(self.value, self.decimals)
        # Int
        else:
            return int(self.value)

    def setValue(self, value: float):
        self.value = self.__clamp_value(value)
        self.position_x = None
        self.update()
        # Emit value changed signal
        self.__emit_value_changed()

    def getMinimum(self):
        return self.minimum

    def setMinimum(self, minimum: float):
        self.minimum = minimum
        self.update()

    def getMaximum(self):
        return self.maximum

    def setMaximum(self, maximum: float):
        self.maximum = maximum
        self.update()

    def getRange(self):
        return self.minimum, self.maximum

    def setRange(self, minimum: float, maximum: float):
        self.minimum = minimum
        self.maximum = maximum

    def isFloat(self):
        return self.float

    def setFloat(self, use_float: bool):
        self.float = use_float
        self.update()

    def getDecimals(self):
        return self.decimals

    def setDecimals(self, decimals: int):
        self.decimals = decimals
        self.update()

    def getSingleStep(self):
        return self.single_step

    def setSingleStep(self, single_step: float):
        self.single_step = single_step

    def getPageStep(self):
        return self.page_step

    def setPageStep(self, page_step: float):
        self.page_step = page_step

    def getThousandsSeperator(self):
        return self.thousands_seperator

    def setThousandsSeperator(self, thousands_seperator: str):
        self.thousands_seperator = thousands_seperator
        self.update()

    def getDecimalSeperator(self):
        return self.decimal_seperator

    def setDecimalSeperator(self, decimal_seperator: str):
        self.decimal_seperator = decimal_seperator
        self.update()

    def getPrefix(self):
        return self.prefix

    def setPrefix(self, prefix: str):
        self.prefix = prefix
        self.update()

    def getSuffix(self):
        return self.suffix

    def setSuffix(self, suffix: str):
        self.suffix = suffix
        self.update()

    def getShowValue(self):
        return self.display_value

    def showValue(self, show_value: bool):
        self.display_value = show_value

    def getTextColor(self):
        return self.text_color

    def setTextColorHex(self, text_color_hex: str):
        self.text_color = QtGui.QColor(text_color_hex)
        self.update()

    def setTextColorRgba(self, r: int, g: int, b: int, a: int):
        self.text_color = QtGui.QColor.fromRgba(QtGui.qRgba(r, g, b, a))
        self.update()

    def getBackgroundColor(self):
        return self.background_color

    def setBackgroundColorHex(self, background_color_hex: str):
        self.background_color = QtGui.QColor(background_color_hex)
        self.update()

    def setBackgroundColorRgba(self, r: int, g: int, b: int, a: int):
        self.background_color = QtGui.QColor.fromRgba(QtGui.qRgba(r, g, b, a))
        self.update()

    def getAccentColor(self):
        return self.accent_color

    def setAccentColorHex(self, accent_color_hex: str):
        self.accent_color = QtGui.QColor(accent_color_hex)
        self.update()

    def setAccentColorRgba(self, r: int, g: int, b: int, a: int):
        self.accent_color = QtGui.QColor.fromRgba(QtGui.qRgba(r, g, b, a))
        self.update()

    def getBorderColor(self):
        return self.border_color

    def setBorderColorHex(self, border_color_hex: str):
        self.border_color = QtGui.QColor(border_color_hex)
        self.__update_stylesheet()
        self.update()

    def setBorderColorRgba(self, r: int, g: int, b: int, a: int):
        self.border_color = QtGui.QColor.fromRgba(QtGui.qRgba(r, g, b, a))
        self.__update_stylesheet()
        self.update()

    def getBorderRadius(self):
        return self.border_radius

    def setBorderRadius(self, border_radius: int):
        self.border_radius = border_radius
        self.__update_stylesheet()
        self.update()

    def getFont(self):
        return self.font

    def setFont(self, font: QtGui.QFont):
        self.font = font

    def __update_stylesheet(self):
        border_color_hex = self.border_color.name()
        self.slider.setStyleSheet('QLabel {border: 1px solid ' + border_color_hex +
                                  '; border-radius: ' + str(self.border_radius) + 'px;}')

    def __get_value_from_position_x(self, position_x: int):
        # Get slider range
        value_range = self.__get_value_range()

        # Calculate value
        value = position_x / self.width() * value_range

        if self.minimum < 0 or self.minimum > 0:
            value = value + self.minimum

        return self.__clamp_value(value)

    def __get_position_x_from_value(self, value: float):
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

    def __get_value_range(self):
        if self.minimum < 0:
            return self.maximum + abs(self.minimum)
        else:
            return self.maximum - self.minimum

    def __clamp_position_x(self, position_x: int):
        if position_x > self.width():
            position_x = self.width()
        if position_x < 0:
            position_x = 0
        return position_x

    def __clamp_value(self, value: float):
        if value > self.maximum:
            value = self.maximum
        if value < self.minimum:
            value = self.minimum
        return value

    def __format_value(self, value: float, is_float: bool, decimals: int,
                       thousands_seperator: str, decimal_seperator: str):
        # Float slider
        if is_float:
            string_format = '{:,.' + str(decimals) + 'f}'
            temp_thousands_seperator = '0888019ca0faa9774a728c864e248749'
            temp_decimal_seperator = 'f6e9eccf7256112eccd52f41f1fded3f'
            return string_format.format(value)\
                .replace(',', temp_thousands_seperator)\
                .replace('.', temp_decimal_seperator)\
                .replace(temp_thousands_seperator, thousands_seperator)\
                .replace(temp_decimal_seperator, decimal_seperator)

        # Int slider
        string_format = '{:,.0f}'
        return string_format.format(int(value)).replace(',', thousands_seperator)

    def __emit_value_changed(self):
        # Float slider
        if self.float:
            self.valueChanged.emit(round(self.value, self.decimals))
        # Int slider
        else:
            self.valueChanged.emit(int(self.value))
