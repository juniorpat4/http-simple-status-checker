import sys
import requests

if len(sys.argv) != 2:
    print("You need to put only two indications (the file name and the url")
    sys.exit(1)

def output(message, file):
    print(message)
    file.write(message + "\n")
    
archivo = open("request.txt", "a")

ERRORES_COMUNES = {
    200 : "Connected to the host",
    403 : "Dennied",
    404 : "Not Found"

}

url = sys.argv[1]

try: 
    r = requests.get(url, timeout=5)
    mensaje = ERRORES_COMUNES[r.status_code]
    output(f"{url} + { mensaje}", archivo)
    
except requests.exceptions.Timeout:
    output(f"{url} Timeout", archivo)
except requests.exceptions.ConnectionError:
    output(f"{url} ConnectionError", archivo)
except requests.RequestException:
    output(f"{url} Request Exception", archivo)
    

archivo.close()
    