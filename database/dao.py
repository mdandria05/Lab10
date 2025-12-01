from database.DB_connect import DBConnect
from model.compagnia import Compagnia
from model.hub import Hub
from model.myspedizione import MySpedizione
class DAO:
    """
    Implementare tutte le funzioni necessarie a interrogare il database.
    """
    # TODO
    @staticmethod
    def readCompagnia():
        cnx = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM compagnia"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            result.append(Compagnia(row["id"], row["codice"], row["nome"]))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def readHub():
        cnx = DBConnect.get_connection()
        result = []
        query = "SELECT * FROM hub"
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            result.append(Hub(row["id"], row["codice"], row["nome"], row["citta"], row["stato"], row["latitudine"], row["longitudine"]))
        cursor.close()
        cnx.close()
        return result

    @staticmethod
    def readMySpedizione():
        cnx = DBConnect.get_connection()
        result = []
        query = """SELECT
                        id_hub_origine,
                        id_hub_destinazione,
                        COUNT(DISTINCT id) conteggio,
                        SUM(valore_merce) somma
                    FROM
                        spedizione
                    GROUP BY
                        id_hub_origine,
                        id_hub_destinazione
                    ORDER BY
                        id ASC;"""
        cursor = cnx.cursor(dictionary=True)
        cursor.execute(query)
        for row in cursor:
            result.append(MySpedizione(row["id_hub_origine"], row["id_hub_destinazione"], row["conteggio"], row["somma"]))
        cursor.close()
        cnx.close()
        return result
