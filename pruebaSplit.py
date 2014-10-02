str = 'http://sg.nl.gob.mx/OrdenCompra_2009/BsqAnioProvMes.aspx?Anio=2012&MesId=3&ProveedorId=9687&EntidadId=1004&ConceptoId=308'

str = str.split('&')[2]

str = str.split('=')[1]

print str