import datetime
import tkinter as tk
import ttkbootstrap as ttk

BARANG: list[str] = ['Laptop','Proyektor','Kamera','Tripod','Mic Wireless','Kabel HDMI','Speaker','Lainnya']
STATUS: list[str] = ['Dipinjam','Dikembalikan']
KOLOM: list[str] = ['id','nama','barang','tgl_pinjam','tgl_kembali','status']

# Data contoh supaya warna status langsung kelihatan. Hapus kalau tidak diperlukan.
CONTOH_DATA: list[tuple] = [
]

class RentalBarangApp:
    def __init__(self,root:ttk.Window)->None:
        self.root = root
        self.root.title('Rental & Peminjaman Barang')
        self.root.geometry('900x600')
        self.root.minsize(780,500)

        self.style = ttk.Style()
        self.dark_mode = True

        self._build_header()
        self._build_form_section()
        self._build_button_bar()
        self._build_table_section()
        self._apply_row_colors()

    def _build_header(self)->None:
        header = ttk.Frame(self.root,padding=(15,15,15,0))
        header.pack(fill='x')
        ttk.Label(header,text='Rental & Peminjaman Barang',font=('Helvetica',20,'bold'),bootstyle='info').pack(side='left')
        ttk.Button(header,text='Ganti Tema',command=self.toggle_theme,bootstyle='secondary-outline').pack(side='right')

    def _build_form_section(self)->None:
        form_frame = ttk.Labelframe(self.root,text='Data Peminjaman',padding=12,bootstyle='info')
        form_frame.pack(fill='x',padx=15,pady=(10,5))
        form_frame.columnconfigure(1,weight=1)
        form_frame.columnconfigure(3,weight=1)

        ttk.Label(form_frame,text='Nama Peminjam:').grid(row=0,column=0,sticky='w',padx=(0,8),pady=5)
        self.nama_var = tk.StringVar()
        self.nama_entry = ttk.Entry(form_frame,textvariable=self.nama_var)
        self.nama_entry.grid(row=0,column=1,sticky='ew',padx=(0,15),pady=5)

        ttk.Label(form_frame,text='Barang:').grid(row=0,column=2,sticky='w',padx=(0,8),pady=5)
        self.barang_var = tk.StringVar(value=BARANG[0])
        self.barang_cmb = ttk.Combobox(form_frame,textvariable=self.barang_var,values=BARANG,state='readonly')
        self.barang_cmb.grid(row=0,column=3,sticky='ew',pady=5)

        ttk.Label(form_frame,text='Tgl Pinjam (YYYY-MM-DD):').grid(row=1,column=0,sticky='w',padx=(0,8),pady=5)
        self.pinjam_var = tk.StringVar(value=datetime.date.today().isoformat())
        self.pinjam_entry = ttk.Entry(form_frame,textvariable=self.pinjam_var)
        self.pinjam_entry.grid(row=1,column=1,sticky='ew',padx=(0,15),pady=5)

        ttk.Label(form_frame,text='Tgl Kembali (YYYY-MM-DD):').grid(row=1,column=2,sticky='w',padx=(0,8),pady=5)
        self.kembali_var = tk.StringVar(value=self._default_kembali())
        self.kembali_entry = ttk.Entry(form_frame,textvariable=self.kembali_var)
        self.kembali_entry.grid(row=1,column=3,sticky='ew',pady=5)

        ttk.Label(form_frame,text='Status:').grid(row=2,column=0,sticky='w',padx=(0,8),pady=5)
        self.status_var = tk.StringVar(value=STATUS[0])
        self.status_cmb = ttk.Combobox(form_frame,textvariable=self.status_var,values=STATUS,state='readonly')
        self.status_cmb.grid(row=2,column=1,sticky='ew',padx=(0,15),pady=5)

    def _build_button_bar(self)->None:
        btn_frame = ttk.Frame(self.root,padding=(15,8))
        btn_frame.pack(fill='x')
        ttk.Button(btn_frame,text='Tambah',command=self.handle_add,bootstyle='success').pack(side='left',padx=(0,8))
        ttk.Button(btn_frame,text='Ubah',command=self.handle_update,bootstyle='info').pack(side='left',padx=(0,8))
        ttk.Button(btn_frame,text='Hapus',command=self.handle_delete,bootstyle='danger').pack(side='left',padx=(0,8))
        ttk.Button(btn_frame,text='Bersihkan Form',command=self.clear_form,bootstyle='secondary-outline').pack(side='right')

    def _build_table_section(self)->None:
        table_frame = ttk.Frame(self.root,padding=(15,5,15,15))
        table_frame.pack(fill='both',expand=True)

        self.tree = ttk.Treeview(table_frame,columns=KOLOM,show='headings',selectmode='browse',bootstyle='info')
        headers = {
            'id' : ('ID',60,'center'),
            'nama' : ('Nama Peminjam',170,'w'),
            'barang' : ('Barang',150,'w'),
            'tgl_pinjam' : ('Tgl Pinjam',110,'center'),
            'tgl_kembali' : ('Tgl Kembali',110,'center'),
            'status' : ('Status',110,'center'),
        }

        for col_id, (title,width,anchor) in headers.items():
            self.tree.heading(col_id,text=title)
            self.tree.column(col_id,width=width,anchor=anchor)

        scrollbar = ttk.Scrollbar(table_frame,orient='vertical',command=self.tree.yview,bootstyle='info-round')
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side='left',fill='both',expand=True)
        scrollbar.pack(side='right',fill='y')

        for row in CONTOH_DATA:
            self.tree.insert('','end',values=row,tags=(row[5],))

    def _apply_row_colors(self)->None:
        self.tree.tag_configure('Dipinjam',foreground=self.style.colors.warning)
        self.tree.tag_configure('Dikembalikan',foreground=self.style.colors.success)

    def _default_kembali(self)->str:
        return (datetime.date.today() + datetime.timedelta(days=7)).isoformat()

    def toggle_theme(self)->None:
        self.dark_mode = not self.dark_mode
        self.style.theme_use('darkly' if self.dark_mode else 'flatly')
        self._apply_row_colors()

    def handle_add(self)->None:
        print('Tambah Clicked')
    def handle_update(self)->None:
        print('Ubah Clicked')
    def handle_delete(self)->None:
        print('Hapus Clicked')
    def clear_form(self)->None:
        self.nama_var.set('')
        self.barang_var.set(BARANG[0])
        self.pinjam_var.set(datetime.date.today().isoformat())
        self.kembali_var.set(self._default_kembali())
        self.status_var.set(STATUS[0])

if __name__ == '__main__':
    root = ttk.Window(themename='darkly')
    app = RentalBarangApp(root)
    root.mainloop()