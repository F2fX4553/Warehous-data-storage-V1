import sqlite3
class Database:
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS  story(
        id Integer Primary Key,
        designation text,
        quantite Integer,
        marque_et_type text,
        ref_fournisseur Integer,
        casse text,
        codee Integer
        )
        """

        self.cur.execute(sql)
        self.con.commit()

    def insert(self,designation,quantite,marque_et_type,ref_fournisseur,casse,codee):
        self.cur.execute("insert into story values (NULL,?,?,?,?,?,?)",
                         (designation,quantite,marque_et_type,ref_fournisseur,casse,codee))


        self.con.commit()
    def fetch(self):

        self.cur.execute("SELECT * FROM story")
        rows = self.cur.fetchall()
        return rows
    def remove(self,id):
        self.cur.execute("delete from story where id=?",(id,))
        self.con.commit()
    def update(self,id,designation,quantite,marque_et_type,ref_fournisseur,casse,codee):
        self.cur.execute("update story set designation=?,"
                         "quantite=?,"
                         "marque_et_type=?,"
                         "ref_fournisseur=?,"
                         "casse=?,"
                         "codee=? where id=? ",
                         (designation,quantite,marque_et_type,ref_fournisseur,casse,codee , id))
        self.con.commit()
    '''def search(self,id,designation,quantite,marque_et_type,ref_fournisseur,casse,codee):
        self.cur.execute("SELECT * FROM story WHERE id=? LIKE ?,"
                         "quantite=?,"
                         "marque_et_type=?,"
                         "ref_fournisseur=?,"
                         "casse=?,"
                         "codee=? where id=? ",
                         (designation, quantite, marque_et_type, ref_fournisseur, casse, codee, id))
        self.con.commit()'''



