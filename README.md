# Configuración de IAAS y CDN con Vultr y BackBlaze

Este repositorio contiene los pasos para configurar una infraestructura de IA y CDN utilizando Vultr y BackBlaze. El proyecto presenta una máquina virtual configurada con NGINX como proxy inverso y un entorno Python para ejecutar una aplicación Flask.

## Pasos para la configuración

### 1. Crear una cuenta en Vultr y BackBlaze
1.1 En **Vultr**, es necesario registrar una tarjeta de crédito para un consumo mínimo de $2.5. Al ser un nuevo usuario, recibirás automáticamente $300 gratuitos para usar durante el primer mes.  
1.2 En **BackBlaze**, solo necesitas crear la cuenta sin necesidad de registrar tarjeta, y podrás empezar a usar el servicio de inmediato.

### 2. Crear la máquina virtual (MV)
2.1 Crea la máquina virtual según las necesidades del proyecto. Si deseas usar IA, se recomienda seleccionar un servicio con GPU e Inferencia en Vultr. Si el proyecto es pequeño, puedes elegir el plan gratuito con 0.5 RM, que es suficiente para este caso.  
2.2 Una vez creada la MV, espera unos minutos hasta que se complete la instalación del sistema operativo. (Nota: los sistemas operativos son minimalistas, por lo que es necesario conocer cómo navegar y configurarlos).

### 3. Gestionar la máquina virtual
3.1 Para acceder a la MV, puedes hacerlo a través de la página de Vultr, que ofrece una terminal propia, o mediante una herramienta como PuTTY. La MV obtiene automáticamente una dirección IPv4 gratuita al ser creada.  
3.2 Instala **NGINX** como proxy inverso para gestionar las solicitudes del puerto 80 hacia la aplicación en Flask. Para ello, realiza la configuración de la siguiente manera:
```bash
sudo nano /etc/nginx/sites-available/flask_app

Agrega lo siguiente:
server {
    listen 80;
    server_name <IP_DEL_SERVIDOR>;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
