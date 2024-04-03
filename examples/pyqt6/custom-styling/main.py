import sys
from PyQt6.QtWidgets import QApplication
from window import Window


# Run example
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Set stylesheet
    with open("css/stylesheet.css", "r") as stylesheet:
        app.setStyleSheet(stylesheet.read())

    window = Window()
    window.show()
    app.exec()
