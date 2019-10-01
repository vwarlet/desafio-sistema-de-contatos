from GUI import *
import DataBase as db

app = None

def view_command():
    if app.txtNome.get()=="" and app.txtCargo.get()=="" and app.txtEmpresa.get()=="" and app.txtTipoEmpresa.get()=="" and app.txtTelefone.get()=="" and app.txtEmail.get()=="" and app.txtAssunto.get()=="":
        rows = db.view()
    else: 
        rows = db.search(app.txtNome.get(), app.txtCargo.get(), app.txtEmpresa.get(), app.txtTipoEmpresa.get(), app.txtTelefone.get(), app.txtEmail.get(), app.txtAssunto.get())
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)
    
def search_command():
    app.listClientes.delete(0, END)
    rows = db.search(app.txtNome.get(), app.txtCargo.get(), app.txtEmpresa.get(), app.txtTipoEmpresa.get(), app.txtTelefone.get(), app.txtEmail.get(), app.txtAssunto.get())
    for r in rows:
        app.listClientes.insert(END, r)

def update_command():
    db.update(selected[0], app.txtNome.get(), app.txtCargo.get(), app.txtEmpresa.get(), app.txtTipoEmpresa.get(), app.txtTelefone.get(), app.txtEmail.get(), app.txtAssunto.get())
    view_command()

def del_command():
    id = selected[0]
    db.delete(id)
    view_command()

def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()[0]
    selected = app.listClientes.get(index)
    app.entNome.delete(0, END)
    app.entNome.insert(END, selected[1])
    app.entCargo.delete(0, END)
    app.entCargo.insert(END, selected[2])
    app.entEmpresa.delete(0, END)
    app.entEmpresa.insert(END, selected[3])
    app.entTipoEmpresa.delete(0, END)
    app.entTipoEmpresa.insert(END, selected[4])
    app.entTelefone.delete(0, END)
    app.entTelefone.insert(END, selected[5])
    app.entEmail.delete(0, END)
    app.entEmail.insert(END, selected[6])
    app.entAssunto.delete(0, END)
    app.entAssunto.insert(END, selected[7])
    return selected


if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)
    app.btnListar.configure(command=view_command)
    app.btnInserir.configure(command=incluirGui)
    app.btnAtualizar.configure(command=update_command)
    app.btnExcluir.configure(command=del_command)
    
    
    app.run()
