# pyqt-vertical-selection-square-graphics-view
PyQt QGraphicsView with selection box. User can move horizontal border of the box vertically.

## Requirements
* PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-vertical-selection-square-graphics-view.git --upgrade```

## Feature
* Being able to drag and drop horizontal border vertically
* Pressing mouse cursor to place more adjacent border on the spot.
* Right click to release the focus of the box

## Example
Code Sample
```python
from PyQt5.QtWidgets import QWidget, QGridLayout, QApplication, QPushButton, QFileDialog

from pyqt_vertical_selection_square_graphics_view.verticalSelectionSquareGraphicsView import \
    VerticalSelectionSquareGraphicsView


class VerticalSelectionSquareGraphicsViewExample(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        addImageBtn = QPushButton('Add image')
        addImageBtn.clicked.connect(self.__addImage)
        self.__view = VerticalSelectionSquareGraphicsView()

        lay = QGridLayout()
        lay.addWidget(addImageBtn)
        lay.addWidget(self.__view)

        self.setLayout(lay)

    def __addImage(self):
        filename = QFileDialog.getOpenFileName(self, 'Open', '', 'Image Files (*.png *.jpg *.bmp)')
        if filename[0]:
            filename = filename[0]
            self.__view.setFile(filename)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ex = VerticalSelectionSquareGraphicsViewExample()
    ex.show()
    sys.exit(app.exec_())
```

Result

https://user-images.githubusercontent.com/55078043/157777737-a801f085-936e-4f08-95bc-9ae51313454a.mp4

## See Also

<a href="https://github.com/yjg30737/pyqt-horizontal-selection-square-graphics-view.git">pyqt-horizontal-selection-square-graphics-view</a>
