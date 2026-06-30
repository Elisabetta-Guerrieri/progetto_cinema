from fastapi import APIRouter, HTTPException

import sqlite3

# Creo il mini-gestore delle rotte
router = APIRouter()

@router.get("/film/cerca")
def cerca_film(keyword: str):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM film WHERE titolo LIKE ?", (f"%{keyword}%",))
    risultati= cursor.fetchall()
    conn.close()
    return risultati

@router.get("/film")
def lista_film():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM film")
    risultati= cursor.fetchall()
    conn.close()
    return risultati