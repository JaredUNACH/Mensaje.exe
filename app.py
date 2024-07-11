import webview

def load_html():
	# Asegúrate de que la ruta al archivo HTML es correcta.
	# Puede ser una ruta absoluta o relativa a la ubicación de este script.
	webview.create_window('Mi Aplicación Web', url='web\index.html')

if __name__ == '__main__':
	load_html()
	webview.start()