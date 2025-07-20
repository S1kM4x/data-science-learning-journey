
from datetime import datetime

message = "Error en servidor"
date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open("logs.txt", "a") as log: # a es igual append
    log.write(f"[{date}] {message}\n") # \n es para que haga un salto 