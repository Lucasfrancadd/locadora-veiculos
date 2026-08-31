import sqlite3


def conectar():
    return sqlite3.connect("locadora_novo.db")


def criar_tabela():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS veiculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT,
            modelo TEXT,
            ano INTEGER,
            placa TEXT,
            diaria REAL,
            status TEXT
        )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_veiculo(marca, modelo, ano, placa,diaria, status):

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("""
        INSERT INTO veiculos (marca, modelo, ano, placa, diaria, status)
        VALUES (?, ?, ?, ?, ? ,?)
    """, (marca, modelo, ano, placa, diaria, status))

    conexao.commit()
    conexao.close()


def consultar_veiculos():

    conexao = conectar()

    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM veiculos")

    veiculos = cursor.fetchall()

    conexao.close()

    return veiculos
