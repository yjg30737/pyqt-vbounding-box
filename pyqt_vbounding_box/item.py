from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsRectItem, QGraphicsItem
from PyQt5.QtCore import Qt


class Item(QGraphicsRectItem):
    def __init__(self, view, parent=None):
        super().__init__(parent)
        self.__initUi(view)

    def __initUi(self, view=None):
        self.__view = view
        self.setAcceptHoverEvents(True)
        self.setFlags(QGraphicsItem.ItemIsSelectable)
        self.__setStyleOfSelectionSquare()

    def __setStyleOfSelectionSquare(self):
        sq_pen = QPen()
        sq_pen.setStyle(Qt.DashLine)
        sq_pen.setWidth(4)
        self.setPen(sq_pen)

    def mouseMoveEvent(self, e):
        scene_rect = self.__view.scene().sceneRect()
        y = e.pos().y()

        border_rect = self.sceneBoundingRect()

        border_rect_top = border_rect.top()
        border_rect_bottom = border_rect.bottom()

        scene_rect_bottom = scene_rect.bottom()-5

        if abs(y-border_rect_top) > abs(y-border_rect_bottom):
            if e.buttons() & Qt.LeftButton:
                bottom = scene_rect_bottom if y > scene_rect_bottom else y
                rect = self.rect()
                rect.setBottom(bottom)
                self.setRect(rect)
        else:
            if e.buttons() & Qt.LeftButton:
                if y < 0:
                    y = 0
                top = y
                rect = self.rect()
                rect.setTop(top)
                self.setRect(rect)
        return super().mouseMoveEvent(e)

    def hoverEnterEvent(self, e):
        return super().hoverEnterEvent(e)

    def hoverMoveEvent(self, e):
        y = int(e.pos().y())
        selection_rect = self.sceneBoundingRect()
        if y in range(int(selection_rect.top()), int(selection_rect.top())+5):
            self.setCursor(Qt.SizeVerCursor)
        elif y in range(int(selection_rect.bottom())-10, int(selection_rect.bottom())):
            self.setCursor(Qt.SizeVerCursor)
        else:
            self.unsetCursor()
        return super().hoverMoveEvent(e)

    def hoverLeaveEvent(self, e):
        return super().hoverLeaveEvent(e)