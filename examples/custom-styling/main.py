import sys
from PyQt5.QtWidgets import QApplication
from window import Window


# Run example
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Set stylesheet
    with open("css/stylesheet.css", "r") as stylesheet:
        app.setStyleSheet(stylesheet.read())

    window = Window()
    window.show()
    sys.exit(app.exec_())
