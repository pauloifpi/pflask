from dao.db_config import get_connection

class TurmaDAO:

    sqlSelect = "SELECT id, semestre, curso_id, professor_id FROM turma"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT turma.id,
                   turma.semestre,
                   curso.nome_curso,
                   professor.nome,
                   professor.disciplina
            FROM turma
            JOIN curso ON turma.curso_id = curso.id
            JOIN professor ON turma.professor_id = professor.id
            ORDER BY turma.id DESC
        """)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, semestre, curso, professor):
        conn = get_connection()
        cursor = conn.cursor()

        if id:  # atualizar
            sql = """UPDATE turma 
                     SET semestre = %s, curso_id = %s, professor_id = %s 
                     WHERE id = %s"""
            cursor.execute(sql, (semestre, curso, professor, id))
        else:  # inserir
            sql = """INSERT INTO turma (semestre, curso_id, professor_id)
                     VALUES (%s, %s, %s)"""
            cursor.execute(sql, (semestre, curso, professor))

        conn.commit()
        conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, semestre, curso_id, professor_id
            FROM turma
            WHERE id = %s
        """, (id,))
        registro = cursor.fetchone()
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM turma WHERE id = %s", (id,))
        conn.commit()
        conn.close()
        return {"status": "ok"}
