import pyqrcode

homepage = "http://koienergy.cl/dos/"

url = pyqrcode.create(homepage)
url.svg("koienergy.svg", scale =10)
