from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"ism": "Muhammadaziz",
            "familiya": "O`lmasov",
            "yosh": "16"

            }

