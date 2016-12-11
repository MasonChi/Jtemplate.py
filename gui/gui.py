#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as tk
from tkinter.filedialog import askdirectory

from generator import generate


class Application:
    def __init__(self, window):
        """
        call function generate user interface
        :param window:
        """
        self.file_path_var = tk.StringVar()

        self.window = window
        self.buildContext()

        params = generate.Generate.get_from_store()
        if params:
            self.entry_host_var.set(params["host"])
            self.entry_port_var.set(params["port"])
            self.entry_username_var.set(params["username"])
            self.entry_password_var.set(params["password"])
            self.entry_database_var.set(params["database"])
            self.entry_table_var.set(params["table"])
            self.entry_entity_var.set(params["entity"])
            self.entry_author_var.set(params["author"])
            self.entry_project_var.set(params["project"])
            self.file_path_var.set(params["file_path"])

    def start(self):
        """
        start generate template files
        :return:
        """
        self.host = self.entry_host_var.get()
        self.port = int(self.entry_port_var.get())
        self.username = self.entry_username_var.get()
        self.password = self.entry_password_var.get()
        self.database = self.entry_database_var.get()
        self.table = self.entry_table_var.get()
        self.entity = self.entry_entity_var.get()
        self.author = self.entry_author_var.get()

        self.project = self.entry_project_var.get()
        self.file_path = self.file_path_var.get()

        start = generate.Generate(self.host, self.port, self.username, self.password, self.database,
                                  self.table, self.entity, self.author, self.project, self.file_path)
        start.gen()
        start.put_to_store

    def select_path(self):
        file_path = askdirectory()
        self.file_path_var.set(file_path)

    def buildContext(self):
        """
        build user interface
        :return:
        """
        self.context = tk.LabelFrame(self.window, text='Params Config', height=500, width=700)
        self.context.grid(row=1, column=0, ipadx=20, padx=45, pady=2)

        # column 0,1
        self.context_host = tk.Label(self.context, text='MySQL Host:')
        self.context_host.grid(row=0, column=0, padx=15, pady=5, sticky='w')

        self.entry_host_var = tk.StringVar()
        self.entry_host = tk.Entry(self.context, textvariable=self.entry_host_var)
        self.entry_host.grid(row=0, column=1, padx=15, pady=5, sticky='e')

        self.context_port = tk.Label(self.context, text='MySQL Port:')
        self.context_port.grid(row=1, column=0, padx=15, pady=5, sticky='w')

        self.entry_port_var = tk.StringVar()
        self.entry_port = tk.Entry(self.context, textvariable=self.entry_port_var)
        self.entry_port.grid(row=1, column=1, padx=15, pady=5)

        self.context_username = tk.Label(self.context, text='MySQL UserName:')
        self.context_username.grid(row=2, column=0, padx=15, pady=5, sticky='w')

        self.entry_username_var = tk.StringVar()
        self.entry_username = tk.Entry(self.context, textvariable=self.entry_username_var)
        self.entry_username.grid(row=2, column=1, padx=15, pady=5)

        self.context_password = tk.Label(self.context, text='MySQL Password:')
        self.context_password.grid(row=3, column=0, padx=15, pady=5, sticky='w')

        self.entry_password_var = tk.StringVar()
        self.entry_password = tk.Entry(self.context, textvariable=self.entry_password_var)
        self.entry_password.grid(row=3, column=1, padx=15, pady=5)

        self.context_project = tk.Label(self.context, text='ProjectName:')
        self.context_project.grid(row=4, column=0, padx=15, pady=5, sticky='w')

        self.entry_project_var = tk.StringVar()
        self.entry_project = tk.Entry(self.context, textvariable=self.entry_project_var)
        self.entry_project.grid(row=4, column=1, padx=15, pady=5)

        self.context_author = tk.Label(self.context, text='Author:')
        self.context_author.grid(row=5, column=0, padx=15, pady=5, sticky='w')

        self.entry_author_var = tk.StringVar()
        self.entry_author = tk.Entry(self.context, textvariable=self.entry_author_var)
        self.entry_author.grid(row=5, column=1, padx=15, pady=5)

        self.context_database = tk.Label(self.context, text='Database:')
        self.context_database.grid(row=6, column=0, padx=15, pady=5, sticky='w')

        self.entry_database_var = tk.StringVar()
        self.entry_database = tk.Entry(self.context, textvariable=self.entry_database_var)
        self.entry_database.grid(row=6, column=1, padx=15, pady=5)

        self.context_table = tk.Label(self.context, text='Table:')
        self.context_table.grid(row=7, column=0, padx=15, pady=5, sticky='w')

        self.entry_table_var = tk.StringVar()
        self.entry_table = tk.Entry(self.context, textvariable=self.entry_table_var)
        self.entry_table.grid(row=7, column=1, padx=15, pady=5)

        self.context_entity = tk.Label(self.context, text='Entity:')
        self.context_entity.grid(row=8, column=0, padx=15, pady=5, sticky='w')

        self.entry_entity_var = tk.StringVar()
        self.entry_entity = tk.Entry(self.context, textvariable=self.entry_entity_var)
        self.entry_entity.grid(row=8, column=1, padx=15, pady=5)

        # column 2,3
        self.context_file = tk.Label(self.context, text='FilePath:')
        self.context_file.grid(row=0, column=2, padx=15, pady=5, sticky='w')

        self.file_path = tk.Entry(self.context, textvariable=self.file_path_var)
        self.file_path.grid(row=0, column=3, padx=15, pady=5)

        self.target = tk.Button(self.context, command=self.select_path, text='Select Path')
        self.target.grid(row=0, column=4, padx=15, pady=5)

        # self.context_auto = tk.Label(self.context, text='AutoPath:')
        # self.context_auto.grid(row=1, column=2, padx=15, pady=5, sticky='w')

        # self.auto_var = tk.IntVar()
        # self.context_auto = tk.Checkbutton(self.context, text="Auto Path", variable=self.auto_var, onvalue=1,
        #                                    offvalue=0)
        # self.context_auto.grid(row=1, column=3, padx=10, pady=5, sticky='w')
        #
        # self.context_path = tk.Label(self.context, text='ProjectPath:')
        # self.context_path.grid(row=2, column=2, padx=15, pady=5, sticky='w')
        #
        # self.project_path_var = tk.StringVar()
        # self.project_path = tk.Entry(self.context, textvariable=self.project_path_var)
        # self.project_path.grid(row=2, column=3, padx=15, pady=5)

        # text and button
        self.text = tk.Text(window, width=75, height=6)
        self.text.grid(row=2, column=0, padx=45, pady=5, sticky='w')

        self.start = tk.Button(window, text='Start', width=17, command=self.start)
        self.start.grid(row=2, column=0, padx=45, sticky='e')


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Java SSM code template generator')
    window.geometry('800x600')

    canvas = tk.Canvas(window, height=150, width=700)
    image_file = tk.PhotoImage(file='welcome.gif')
    canvas.create_image(130, 10, anchor='nw', image=image_file)
    canvas.grid(row=0, column=0, padx=15, pady=2)

    Application(window)
    window.mainloop()
