#!/usr/bin/env python3

"""Run the GUI."""

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog

import src.pylib.db as db
from src.gui.main_window import Ui_MainWindow
from src.gui.dataframe_model import DataframeModel
from src.pylib.pdf import pdfs_to_text
from src.pylib.util import OK


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main page of the app."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        with db.connect() as cxn:
            df = db.select_guides(cxn)

        self.guides_model = DataframeModel(df)
        self.guides_table.setModel(self.guides_model)

        self.build_db_btn.clicked.connect(
            lambda: self.event_status(db.create))

        self.backup_db_btn.clicked.connect(
            lambda: self.event_status(db.backup_database))

        self.pdf_to_text_btn.clicked.connect(self.pdf_to_text)

    def pdf_to_text(self):
        """Attach open PDFs dialog."""
        files, _ = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Load PDFs into Database',
            filter='All Files (*);;PDF Files (*.pdf)')
        if files:
            pdfs_to_text(files)
            with db.connect() as cxn:
                self.guides_model.dataframe = db.select_guides(cxn)
            self.set_status('PDFs loaded.')

    def event_status(self, func):
        """Wrap action so that we can display results."""
        status, msg = func()
        self.set_status(msg, status)

    def set_status(self, msg, status=OK):
        """Display the status."""
        color = 'rgb(0,0,0)' if status == OK else 'rgb(255,0,0)'
        self.statusBar().setStyleSheet(f'color: {color};')
        self.statusBar().showMessage(msg)


def main():
    """Do it."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
