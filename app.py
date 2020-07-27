#!/usr/bin/env python3

"""Run the GUI."""

import tkinter as tk
import tkinter.ttk as ttk
from os.path import basename, dirname, splitext
from shutil import copy
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

import src.pylib.db as db
import src.pylib.doc as doc

OK = 0
ERROR = 1
MEMORY = ':memory:'


class App(tk.Tk):
    """Build the app."""

    def __init__(self):
        tk.Tk.__init__(self)
        self.dirty = False
        self.path = MEMORY
        self.cxn = db.connect(self.path)
        self.db_dir = '.'
        self.doc_dir = '.'

        db.create(self.cxn, self.path)

        self.title(self.get_title())
        self.geometry('1024x760')

        menu = tk.Menu(self)

        file_menu = tk.Menu(menu, tearoff=False)
        file_menu.add_command(label='Open', underline=0, command=self.open_db)
        file_menu.add_command(label='New', underline=0, command=self.new_db)
        file_menu.add_command(
            label='Save...', underline=0,
            command=self.save_as_db,
            state=tk.DISABLED)
        file_menu.add_command(
            label='Save as...', underline=5, command=self.save_as_db)
        file_menu.add_separator()
        file_menu.add_command(
            label='Quit', underline=0, command=self.safe_quit)

        menu.add_cascade(label='File', underline=0, menu=file_menu)
        self.config(menu=menu)

        notebook = ttk.Notebook(self)
        tab1 = tk.Frame(notebook)
        tab2 = tk.Frame(notebook)
        notebook.add(tab1, text='Import')
        notebook.add(tab2, text='Transform')
        notebook.pack(expand=True, fill="both")

        tab1_frame = tk.Frame(tab1)
        tab1_frame.pack(expand=True, fill='both')

        tab1_top_frame = tk.Frame(tab1_frame)
        tab1_top_frame.pack(expand=False, fill='x', pady=(32, 32))
        tab1_bottom_frame = tk.Frame(tab1_frame)
        tab1_bottom_frame.pack(expand=True, fill='both')

        pdf_to_text_btn = tk.Button(
            tab1_top_frame, text='PDF to Text...', command=self.pdf_to_text)
        pdf_to_text_btn.pack(side=tk.LEFT, padx=(16, 16))

        import_text_btn = tk.Button(
            tab1_top_frame, text='Import Text...', command=self.import_text)
        import_text_btn.pack(side=tk.LEFT, padx=(16, 16))

        ocr_text_btn = tk.Button(
            tab1_top_frame, text='OCR PDF...', state=tk.DISABLED,
            command=self.ocr_pdf)
        ocr_text_btn.pack(side=tk.LEFT, padx=(16, 16))

        self.docs = doc.select_docs(self.cxn)
        self.docs.set_index('doc_id', inplace=True)
        self.docs_tree = ttk.Treeview(tab1_bottom_frame)
        self.docs_tree['columns'] = list(self.docs.columns)
        for col in self.docs.columns:
            self.docs_tree.column(col, stretch=True)
            self.docs_tree.heading(col, text=col)
        self.docs_tree.pack(expand=True, fill='both')

        tab2_frame = tk.Frame(tab2)
        tab2_frame.pack(expand=True, fill='both')

        tab2_top_frame = tk.Frame(tab2_frame)
        tab2_top_frame.pack(expand=False, fill='x', pady=(32, 32))
        tab2_middle_frame = tk.Frame(tab2_frame)
        tab2_middle_frame.pack(expand=True, fill='both')
        tab2_bottom_frame = tk.Frame(tab2_frame)
        tab2_bottom_frame.pack(expand=False, fill='x')

        self.doc_sel = ttk.Combobox(tab2_top_frame)
        self.doc_sel.pack(side=tk.LEFT, padx=(16, 16))

        self.edits = ScrolledText(tab2_middle_frame)
        self.edits.pack(fill="both", expand=True)
        self.edits.insert(tk.INSERT, '')

    def open_db(self):
        """Open a database and fill the fields with its data."""
        path = filedialog.askopenfile(
            initialdir=self.db_dir, title='Open a Traiter Database',
            filetypes=(('db files', '*.db'), ('all files', '*.*')))
        if not path:
            return
        self.db_dir = dirname(path.name)
        self.path = path.name
        self.cxn = db.connect(self.path)
        self.repopulate()

    def new_db(self):
        """Open a database and fill the fields with its data."""
        path = filedialog.asksaveasfilename(
            initialdir=self.db_dir, title='Create a New Database',
            filetypes=(('db files', '*.db'), ('all files', '*.*')))
        if not path:
            return
        self.db_dir = dirname(path)
        self.path = path
        self.cxn = db.connect(path)
        db.create(self.cxn, path)
        self.repopulate()

    def save_as_db(self):
        """Open a database and fill the fields with its data."""
        path = filedialog.asksaveasfilename(
            initialdir=self.db_dir, title='Save the Database',
            filetypes=(('db files', '*.db'), ('all files', '*.*')))
        if not path:
            return
        copy(self.path, path)
        self.db_dir = dirname(path)
        self.path = path
        self.cxn = db.connect(path)
        self.repopulate()

    def safe_quit(self):
        """Prompt to save changes before quitting."""
        if self.path == MEMORY and self.dirty:
            yes = messagebox.askyesno(
                self.get_title(),
                'Are you sure you want to exit before saving?')
            if not yes:
                return
        self.quit()

    def pdf_to_text(self):
        """Import PDFs into the database."""
        paths = filedialog.askopenfilenames(
            initialdir=self.doc_dir, title='Import PDF Files', multiple=True,
            filetypes=(('pdf files', '*.pdf'), ('all files', '*.*')))
        if paths:
            self.dirty = True
            self.doc_dir = dirname(paths[0])
            doc.import_files(self.cxn, paths, type_='pdf')
            self.repopulate()

    def import_text(self):
        """Import PDFs into the database."""
        self.dirty = True
        print('import_text')

    def ocr_pdf(self):
        """Import PDFs into the database."""
        self.dirty = True
        print('ocr_pdf')

    def repopulate(self):
        """Repopulate the controls from new data."""
        self.title(self.get_title())
        self.docs = doc.select_docs(self.cxn)
        doc_ids = self.docs['doc_id'].tolist()
        self.doc_sel['values'] = doc_ids
        self.doc_sel['width'] = max(len(i) for i in doc_ids)
        self.doc_sel.current(0)
        self.docs.set_index('doc_id', inplace=True)
        self.docs_tree.delete(*self.docs_tree.get_children())
        for doc_id, row in self.docs.iterrows():
            self.docs_tree.insert('', tk.END, text=doc_id, values=list(row))

    def get_title(self):
        """Build the window title."""
        title = splitext(basename(self.path))[0]
        return f'Traiter ({title})'


if __name__ == '__main__':
    APP = App()
    APP.mainloop()
