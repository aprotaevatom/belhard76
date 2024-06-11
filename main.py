from fastapi import FastAPI
from psycopg2 import connect
from uvicorn import run


def is_palindrome(text: str) -> bool:
    return text.lower() == text.lower()[::-1]


app = FastAPI()
conn = connect("postgresql://admin:admin@0.0.0.0:5432/admin")
with conn.cursor() as cur:
    cur.execute(f"select * from category where category.id = {int(input())}")


if __name__ == '__main__':
    run(
        app=app,
        host="0.0.0.0",
        port=80
    )
