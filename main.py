from fastapi import FastAPI

# Instantiate app
app = FastAPI()


#Handle get requests to root
@app.get("/")
def read_root():
    return {"message": "Hello World"} 

@app.get("/hello")
def hello(name: str = "Bipul Islam"):
    return {"message": f"Hello {name}"}

