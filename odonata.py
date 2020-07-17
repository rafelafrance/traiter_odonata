#!/usr/bin/env python3

"""Run the GUI."""

import sys

import pandas as pd
from PyQt5 import Qt, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog

import src.pylib.db as db
from src.gui.data_frame_model import DataFrameModel
from src.gui.main_window import Ui_MainWindow
from src.pylib.pdf import pdfs_to_text

OK = 0
ERROR = 1


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """Main page of the app."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.doc_id = ''

        df = self.load_dataframe(db.select_docs)
        self.guides_model = DataFrameModel(df)
        self.guides_table.setModel(self.guides_model)

        self.doc_edit.setPlainText('')
        self.reset_edits_btn.clicked.connect(self.reset_edits)
        self.cancel_edits_btn.clicked.connect(self.cancel_edits)
        self.save_edits_btn.clicked.connect(self.save_edits)

        self.build_db_btn.clicked.connect(self.reset_db)

        self.backup_db_btn.clicked.connect(
            lambda: self.event_status(db.backup_database))

        self.pdf_to_text_btn.clicked.connect(self.pdf_to_text)

    def save_edits(self):
        """Accept changes to the doc."""
        edits = self.doc_edit.toPlainText()
        db.update_doc(self.doc_id, edits)
        self.doc_edit.setPlainText(edits)

    def cancel_edits(self):
        """Cancel changes to the doc."""
        edits = self.get_doc_edits(db.select_doc, self.doc_id)
        db.update_doc(self.doc_id, edits)
        self.doc_edit.setPlainText(edits)

    def reset_edits(self):
        """Rest the doc back to its original form."""
        db.reset_doc(self.doc_id)
        edits = self.get_doc_edits(db.select_doc, self.doc_id)
        self.doc_edit.setPlainText(edits)

    def doc_double_click(self, idx: Qt.QModelIndex):
        """Show the document for editing."""
        self.doc_id = self.guides_model.dataframe.loc[idx.row(), 'doc_id']
        edits = self.get_doc_edits(db.select_doc, self.doc_id)
        self.doc_edit.setPlainText(edits)

    def load_dataframe(self, func, *args, **kwargs):
        """LOad a dataframe from the database."""
        try:
            df = func(*args, **kwargs)
            return df
        except Exception as err:
            self.set_status(err, status=ERROR)
            return pd.DataFrame()

    def get_doc_edits(self, func, *args, **kwargs):
        """As per."""
        result = ''
        try:
            result = func(*args, **kwargs)
        except Exception as err:
            self.set_status(err, status=ERROR)
        return result

    def pdf_to_text(self):
        """Attach open PDFs dialog."""
        files, _ = QFileDialog.getOpenFileNames(
            parent=self,
            caption='Load PDFs into Database',
            filter='All Files (*);;PDF Files (*.pdf)')
        if files:
            pdfs_to_text(files)
            self.guides_model.dataframe = db.select_docs()
            self.set_status('PDFs loaded.')

    def reset_db(self):
        """Reset the database."""
        self.event_status(db.create)
        df = self.load_dataframe(db.select_docs)
        self.guides_model.dataframe = df

    def event_status(self, func, msg=''):
        """Wrap action so that we can display results."""
        result = None
        try:
            result = func()
            self.set_status(msg)
        except Exception as err:
            self.set_status(err, status=ERROR)
        return result

    def set_status(self, msg, status=OK):
        """Display the status."""
        msg = ' '.join(str(msg).split())
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
