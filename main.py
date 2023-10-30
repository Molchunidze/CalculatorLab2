from fastapi import FastAPI
app = FastAPI()

@app.post("/calculator/{Chislo1}/{Chislo2}/{Znak}")
def result(Chislo1: str, Chislo2: str,Znak: str):
    return reshenie(Chislo1,Chislo2,Znak)

def reshenie(Chislo1,Chislo2,Znak):
    if Znak=="+":
        return int(Chislo1) + int(Chislo2)
    if Znak=="-":
        return int(Chislo1) - int(Chislo2)
    if Znak=="*":
        return int(Chislo1) * int(Chislo2)
    if Znak=="/" and Chislo2!=0:
        return int(Chislo1)/int(Chislo2)



