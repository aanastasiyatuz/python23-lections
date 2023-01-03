from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"message":"hello world"}

@app.post("/create")
def create():
    return {"message":"created"}

@app.delete("/delete")
def delete():
    return {"message":"deleted"}

