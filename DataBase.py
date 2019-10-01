import sqlite3 as sql

class DataBase():
    database    = "clientes.db"
    conn        = None
    cur         = None
    connected   = False

    def connect(self):
        DataBase.conn      = sql.connect(DataBase.database)
        DataBase.cur       = DataBase.conn.cursor()
        DataBase.connected = True

    def disconnect(self):
        DataBase.conn.close()
        DataBase.connected = False

    def execute(self, sql, parms = None):
        if DataBase.connected:
            if parms == None:
                DataBase.cur.execute(sql)
            else:
                DataBase.cur.execute(sql, parms)
            return True
        else:
            return False

    def fetchall(self):
        return DataBase.cur.fetchall()

    def persist(self):
        if DataBase.connected:
            DataBase.conn.commit()
            return True
        else:
            return False


def initDB():
    db = DataBase()
    db.connect()
    db.execute("CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY , nome TEXT, cargo TEXT, empresa TEXT, tipoEmpresa TEXT, telefone TEXT, email TEXT, assunto TEXT)")
    db.persist()
    db.disconnect()

def insert(nome, cargo, empresa, tipoEmpresa, telefone, email, assunto):
    db = DataBase()
    db.connect()
    db.execute("INSERT INTO clientes VALUES(NULL, ?,?,?,?,?,?,?)", (nome, cargo, empresa, tipoEmpresa, telefone, email, assunto))
    db.persist()
    db.disconnect()

def view():
    db = DataBase()
    db.connect()
    db.execute("SELECT * FROM clientes")
    rows = db.fetchall()
    db.disconnect()
    return rows

def search(nome="", cargo="", empresa="", tipoEmpresa="", telefone="", email="", assunto=""):
    db = DataBase()
    db.connect()
    db.execute("SELECT * FROM clientes WHERE nome=? or cargo=? or empresa=? or tipoEmpresa=? or telefone=? or email=? or assunto=?  ORDER BY empresa", (nome, cargo, empresa, tipoEmpresa, telefone, email, assunto))
    rows = db.fetchall()
    db.disconnect()
    return rows

def delete(id):
    db = DataBase()
    db.connect()
    db.execute("DELETE FROM clientes WHERE id = ?", (id,))
    db.persist()
    db.disconnect()

def update(id, nome, cargo, empresa, tipoEmpresa, telefone, email, assunto):
    db = DataBase()
    db.connect()
    db.execute("UPDATE clientes SET nome=?, cargo=?, empresa=?, tipoEmpresa=?, telefone=?, email=?, assunto=? WHERE id = ?", (nome, cargo, empresa, tipoEmpresa, telefone, email, assunto, id))
    db.persist()
    db.disconnect()

initDB()


