from dao.db_config import get_connection

class ProfessorDAO:

    sqlSelect = "SELECT id, nome, disciplina FROM professor"

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, nome, disciplina):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id is None or id == "":
                
                cursor.execute(
                    "INSERT INTO professor (nome, disciplina) VALUES (%s, %s)",
                    (nome, disciplina)
                )
            else:
                
                cursor.execute(
                    "UPDATE professor SET nome=%s, disciplina=%s WHERE id=%s",
                    (nome, disciplina, id)
                )

            conn.commit()
            return {"status": "ok"}

        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}

        finally:
            conn.close()
