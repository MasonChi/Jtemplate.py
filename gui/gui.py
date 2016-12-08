#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import tkinter as tk

from mysql import mysql_param


class Application:
    def __init__(self, window):
        self.window = window
        self.buildContext()

    def start(self):
        pass

    def buildContext(self):
        self.context = tk.LabelFrame(self.window, text='Params Config', height=500, width=700)
        self.context.grid(row=1, column=0, ipadx=65, padx=45, pady=2)

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

        self.file_path_var = tk.StringVar()
        self.file_path = tk.Entry(self.context, textvariable=self.file_path_var)
        self.file_path.grid(row=0, column=3, padx=15, pady=5)

        self.context_auto = tk.Label(self.context, text='AutoPath:')
        self.context_auto.grid(row=1, column=2, padx=15, pady=5, sticky='w')

        self.auto_var = tk.IntVar()
        self.context_auto = tk.Checkbutton(self.context, text="Auto Path", variable=self.auto_var, onvalue=1,
                                           offvalue=0)
        self.context_auto.grid(row=1, column=3, padx=10, pady=5, sticky='w')

        self.context_path = tk.Label(self.context, text='ProjectPath:')
        self.context_path.grid(row=2, column=2, padx=15, pady=5, sticky='w')

        self.path_var = tk.StringVar()
        self.path = tk.Entry(self.context, textvariable=self.path_var)
        self.path.grid(row=2, column=3, padx=15, pady=5)

        # text and button
        self.text = tk.Text(window, width=75, height=6)
        self.text.grid(row=2, column=0, padx=45, pady=5, sticky='w')

        self.start = tk.Button(window, text='Start', width=17,command=self.start)
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

# HOST = 'localhost'
# USERNAME = 'root'
# PASSWORD = '123456'
# PORT = 401
#
# PROJECT = 'project'
# PROJECT_PATH = r'C:\Apps\project'
# AUTHOR = 'child'
#
# DATABASE = 'project'
# TABLE = 'user'
# ENTITY = 'User'
#
# FILE_PATH = r'C:\test'
