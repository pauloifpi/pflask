from dao.db_config import get_connection

class CursoDAO:

    sqlSelect = "SELECT id, nome_curso, duracao FROM curso"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, nome_curso, duracao):
        conn = get_connection()
        cursor = conn.cursor()

        if id:  # atualizar
            sql = """UPDATE curso 
                     SET nome_curso = %s, duracao = %s 
                     WHERE id = %s"""
            cursor.execute(sql, (nome_curso, duracao, id))
        else:  # inserir
            sql = """INSERT INTO curso (nome_curso, duracao)
                     VALUES (%s, %s)"""
            cursor.execute(sql, (nome_curso, duracao))

        conn.commit()
        conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nome_curso, duracao FROM curso WHERE id = %s",
            (id,)
        )
        curso = cursor.fetchone()
        conn.close()
        return curso
    
    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nome_curso, duracao FROM curso WHERE id = %s", (id,))
        registro = cursor.fetchone()
        conn.close()
        return registro
    
    def remover(self, id):   
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM curso WHERE id = %s", (id,))
        conn.commit()
        conn.close()
        return {"status": "ok"}        

