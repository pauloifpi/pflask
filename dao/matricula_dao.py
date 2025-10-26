from dao.db_config import get_connection

class MatriculaDAO:

    sqlSelect = "SELECT id, aluno_id, curso_id, turma_id FROM matricula"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista