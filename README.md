# IAAS y CDN
Uso de Vultr y BackBlaze
# Inicio
1. Crear una cuenta en VULTR y BACKBLAZE
1.1 En VULTR es necesario registrar una tarjeta de crédito con un consumo de $2.5 y por nuevo usuario se registra automáticamente $300 gratuitos para usar durante 1 mes
1.2 En BACKBLAZE solo se crea la cuenta sin necesidad de registro de tarjeta y se puede empezar a usar
2. Crear la máquina virtual
2.1 Crear la máquina virtual según se adapte a las necesidades y objetivo del proyecto, si se desea usar IA se recomiendo escoger algún servicio de GPU e Inferencia de VULTR. Si es un proyecto pequeño como el presentado podemos elegir el plan gratuito con 0.5 RM ya que será suficiente para el proyecto presentado.
2.2 Una vez ya creada la máquina virtual esperamos unos minutos hasta que se complete la instalación del Sistema Operativo. (NOTA: Los SO son minimal por lo que es necesario saber como navegar y configurarlos de ser el caso)
3. Gestionar la máquina virtual
3.1 Para acceder a la MV podemos hacerlo mediante la página de VULTR ya que nos ofrece si propia terminal o a travéz de putty ya que la MV ya concede una dirección IPv4 gratuita al general la MV.
4. Preparar el entorno de la MV
4.1 Instalar python3 en la máquina virtual
4.2 Instalar las librerias para manejo de entorno virtual
   sudo apt install python3-venv
4.3 Crear un entorno virtual en el que se instalarán todas las librerias requeridas para el proyecto
   python3 -m venv dispo
