import sys
import requests

if len(sys.argv) == 1:
    print("You need to put only two or more indications (the file name and the urls)")
    sys.exit(1)

def output(message, file):
    print(message)
    file.write(message + "\n")
    
archivo = open("requests.txt", "a")

ERRORES_COMUNES = {
    200 : "Connected to the host",
    403 : "Dennied",
    404 : "Not Found"

}

urls = sys.argv[1:]       
        
        
for i in urls:    
    try:    
        r = requests.get(i, timeout=5)
        mensaje = ERRORES_COMUNES[r.status_code] #PROVIDED THAT r.status_code != the errors on ERRORES_COMUNES.
        output(f"{i} + {mensaje}", archivo)
    
    except requests.exceptions.Timeout:
        output(f"{i} Timeout", archivo)
    except requests.exceptions.ConnectionError:
        output(f"{i} ConnectionError", archivo)
    except requests.RequestException:
        output(f"{i} Request Exception", archivo)
    

archivo.close()
    
