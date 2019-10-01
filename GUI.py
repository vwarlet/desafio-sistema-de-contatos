from tkinter import *
import DataBase as db

class Gui():
    
    x_pad = 5
    y_pad = 3
    width_entry = 30

    # Cria a janela
    window = Tk()
    window.wm_title("Sistema de Contatos")

    # Cria variáveis que armazenarão o texto inserido pelo usuário
    txtNome = StringVar()
    txtCargo = StringVar()
    txtEmpresa = StringVar()
    txtTipoEmpresa = StringVar()
    txtTelefone = StringVar()
    txtEmail = StringVar()
    txtAssunto = StringVar()

    # Cria os objetos que estarão na janela
    lblnome = Label(window, text="Nome")
    lblcargo = Label(window, text="Cargo")
    lblempresa = Label(window, text="Empresa")
    lbltipoEmpresa = Label(window, text="Tipo Empresa")
    lbltelefone = Label(window, text="Telefone")
    lblemail = Label(window, text="E-mail")
    lblassunto = Label(window, text="Assunto")
    entNome = Entry(window, textvariable=txtNome, width=width_entry)
    entCargo = Entry(window, textvariable=txtCargo, width=width_entry)
    entEmpresa = Entry(window, textvariable=txtEmpresa, width=width_entry)
    entTipoEmpresa = Entry(window, textvariable=txtTipoEmpresa, width=width_entry)
    entTelefone = Entry(window, textvariable=txtTelefone, width=width_entry)
    entEmail = Entry(window, textvariable=txtEmail, width=width_entry)
    entAssunto = Entry(window, textvariable=txtAssunto, width=width_entry)
    listClientes = Listbox(window, width=100)
    scrollClientes = Scrollbar(window)
    btnListar = Button(window, text="Carregar")
    btnInserir = Button(window, text="Incluir")
    btnAtualizar = Button(window, text="Atualizar Selecionado")
    btnExcluir = Button(window, text="Excluir Selecionado")

    # Associa os objetos a grid da janela
    lblnome.grid(row=0, column=0)
    lblcargo.grid(row=1, column=0)
    lblempresa.grid(row=2, column=0)
    lbltipoEmpresa.grid(row=3, column=0)
    lbltelefone.grid(row=4, column=0)
    lblemail.grid(row=5, column=0)
    lblassunto.grid(row=6, column=0)
    entNome.grid(row=0, column=1, padx=50, pady=50)
    entCargo.grid(row=1, column=1)
    entEmpresa.grid(row=2, column=1)
    entTipoEmpresa.grid(row=3, column=1)
    entTelefone.grid(row=4, column=1)
    entEmail.grid(row=5, column=1)
    entAssunto.grid(row=6, column=1)
    listClientes.grid(row=0, column=2, rowspan=10)
    scrollClientes.grid(row=0, column=6, rowspan=10)
    btnListar.grid(row=7, column=0, columnspan=2)
    btnInserir.grid(row=9, column=0, columnspan=2)
    btnAtualizar.grid(row=10, column=0, columnspan=2)
    btnExcluir.grid(row=11, column=0, columnspan=2)

    # Associa a Scrollbar com a Listbox
    listClientes.configure(yscrollcommand=scrollClientes.set)
    scrollClientes.configure(command=listClientes.yview)

    # Ajusta a janela
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')
    

    def run(self):
        Gui.window.mainloop()

def incluirGui():
    new_window = Toplevel()
    new_window.wm_title("Cadastro de Contato")

    x_pad = 5
    y_pad = 3
    width_entry = 30

    # Cria variáveis que armazenarão o texto inserido pelo usuário
    txtNome = StringVar()
    txtCargo = StringVar()
    txtEmpresa = StringVar()
    txtTipoEmpresa = StringVar()
    txtTelefone = StringVar()
    txtEmail = StringVar()
    txtAssunto = StringVar()

    # Cria os objetos que estarão na janela
    lblnome = Label(new_window, text="Nome")
    lblcargo = Label(new_window, text="Cargo")
    lblempresa = Label(new_window, text="Empresa")
    lbltipoEmpresa = Label(new_window, text="Tipo Empresa")
    lbltelefone = Label(new_window, text="Telefone")
    lblemail = Label(new_window, text="E-mail")
    lblassunto = Label(new_window, text="Assunto")
    entNome = Entry(new_window, textvariable=txtNome, width=width_entry)
    entCargo = Entry(new_window, textvariable=txtCargo, width=width_entry)
    entEmpresa = Entry(new_window, textvariable=txtEmpresa, width=width_entry)
    entTipoEmpresa = Entry(new_window, textvariable=txtTipoEmpresa, width=width_entry)
    entTelefone = Entry(new_window, textvariable=txtTelefone, width=width_entry)
    entEmail = Entry(new_window, textvariable=txtEmail, width=width_entry)
    entAssunto = Entry(new_window, textvariable=txtAssunto, width=width_entry)
    btnSalvar = Button(new_window, text="Salvar")
    btnCancelar = Button(new_window, text="Cancelar")

    # Associa os objetos a grid da janela
    lblnome.grid(row=0, column=0)
    lblcargo.grid(row=1, column=0)
    lblempresa.grid(row=2, column=0)
    lbltipoEmpresa.grid(row=3, column=0)
    lbltelefone.grid(row=4, column=0)
    lblemail.grid(row=5, column=0)
    lblassunto.grid(row=6, column=0)
    entNome.grid(row=0, column=1, padx=10, pady=5)
    entCargo.grid(row=1, column=1, pady=5)
    entEmpresa.grid(row=2, column=1, pady=5)
    entTipoEmpresa.grid(row=3, column=1, pady=5)
    entTelefone.grid(row=4, column=1, pady=5)
    entEmail.grid(row=5, column=1, pady=5)
    entAssunto.grid(row=6, column=1, pady=5)
    btnSalvar.grid(row=7, column=0, columnspan=2)
    btnCancelar.grid(row=8, column=0, columnspan=2)

    # Ajusta a janela
    for child in new_window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')

    app = Gui()
    # Exibir a lista de contatos atualizada
    def view_command():
        rows = db.view() 
        app.listClientes.delete(0, END)
        for r in rows:
            app.listClientes.insert(END, r)              

    # Funções dos botões da janela de inclusão
    def insert_command():
        db.insert(txtNome.get(), txtCargo.get(), txtEmpresa.get(), txtTipoEmpresa.get(), txtTelefone.get(), txtEmail.get(), txtAssunto.get())
        new_window.destroy()
        view_command()
    
    btnCancelar.configure(command=new_window.destroy)
    btnSalvar.configure(command=insert_command)
   
    new_window.mainloop()
