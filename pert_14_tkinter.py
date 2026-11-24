import tkinter as tk
import os
import datetime
from tkinter import ttk
os.system('cls')

KATEGORI : list[str] = ['food','transport','utilities','entertainment','shopping','healthcare','other']
KOLOM: list[str] = ['id','date','category','description','amount']

class ExpenseTrackerAPP:
    def __init__(self,root:tk.Tk)->None:
        self.root =  root
        self.root.title('Personal Expense Tracker')
        self.root.geometry('760x500')
        self.root.minsize(680,440)

        style = ttk.Style(self.root)
        if 'clam' in style.theme_names():
            style.theme_use('clam')

        self._build_form_section()
        self._build_button_bar()
        self._build_table_section()

    def _build_form_section(self)->None:
        form_frame = ttk.LabelFrame(self.root, text='Expense Details',padding=12)
        form_frame.pack(fill='x',padx=15,pady=(15,5))
        form_frame.columnconfigure(1,weight=1)
        form_frame.columnconfigure(3,weight=2)
        
        ttk.Label(form_frame,text='Date (YYYY-MM-DD):').grid(row=0,column=0,sticky='w',padx=(0,8),pady=5)
        self.date_var = tk.StringVar(value=datetime.date.today().isoformat())
        self.date_entry = ttk.Entry(form_frame,textvariable=self.date_var,width=16)
        self.date_entry.grid(row=0,column=1,sticky='ew',padx=(0,15),pady=5)
        
        ttk.Label(form_frame,text='Kategori').grid(row=0,column=2,sticky='w',padx=(0,8),pady=5)
        self.category_var = tk.StringVar(value=KATEGORI[0])
        self.category_cmb = ttk.Combobox(form_frame, textvariable=self.category_var, values = KATEGORI, state='readonly', width=16)
        self.category_cmb.grid(row=0,column=3,sticky='ew',pady=5)

        ttk.Label(form_frame,text='Amount (IDR):').grid(row=1,column=0,sticky='w',padx=(0,8),pady=5)
        self.amount_var = tk.StringVar()
        self.amount_entry = ttk.Entry(form_frame, textvariable=self.amount_var, width=16)
        self.amount_entry.grid(row=1,column=1,sticky='ew',padx=(0,15),pady=5)

        ttk.Label(form_frame,text='Description:').grid(row=1,column=2,sticky='w',padx=(0,8),pady=5)
        self.desc_var = tk.StringVar()
        self.desc_entry = ttk.Entry(form_frame,textvariable=self.desc_var)
        self.desc_entry.grid(row=1,column=3,sticky='ew',pady=5)
    
    def _build_button_bar(self)->None:
        btn_frame = ttk.Frame(self.root,padding=(15,8))
        btn_frame.pack(fill='x')
        ttk.Button(btn_frame,text='Add Expense',command=self.handle_add).pack(side='left',padx=(0,8))
        ttk.Button(btn_frame,text='Update Selected',command=self.handle_update).pack(side='left',padx=(0,8))
        ttk.Button(btn_frame,text='Delete Selected',command=self.handle_delete).pack(side='left',padx=(0,8))
        ttk.Button(btn_frame,text='Clear Form',command=self.clear_form).pack(side='right')

    def _build_table_section(self)->None:
        table_frame = ttk.Frame(self.root,padding=(15,5,15,15))
        table_frame.pack(fill='both',expand=True)

        self.tree = ttk.Treeview(table_frame,columns=KOLOM,show='headings',selectmode='browse')
        headers = {'id' : ('Id',70,'center'),'date' : ('Date',110,'center'),'category' : ('Category',120,'w'),'description' : ('Description',300,'w'),'amount' : ('Amount(IDR)',100,'e')}

        for col_id, (title,width,anchor) in headers.items():
            self.tree.heading(col_id,text=title)
            self.tree.column(col_id,width=width,anchor=anchor)

        scrollbar= ttk.Scrollbar(table_frame, orient='vertical',command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side='left',fill='both',expand=True)
        scrollbar.pack(side='right',fill='y')

    def handle_add(self)->None:
        print('Add Expense Clicked')
    def handle_update(self)->None:
        print('Update Selected Clicked')
    def handle_delete(self)->None:
        print('Delete Selected Clicked')
    def clear_form(self)->None:
        self.date_var.set(datetime.date.today().isoformat())
        self.category_var.set(KATEGORI[0])
        self.amount_var.set('')
        self.desc_var.set('')

if __name__ == '__main__':
    root = tk.Tk()
    app = ExpenseTrackerAPP(root)
    root.mainloop()