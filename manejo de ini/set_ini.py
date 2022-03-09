import configparser
configuracion = configparser.ConfigParser()

configuracion['General'] = {'chrome' : 'C:\dchrome\chromedriver.exe'}
configuracion['Paginas'] = {'page' : 'https://www.outlock.com'}

with open('configuracion.ini', 'w') as archivoconfig:
	configuracion.write(archivoconfig)