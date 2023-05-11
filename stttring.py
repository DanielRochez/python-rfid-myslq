nombre = "Hugo Vargas"
texto = "Texto del RFID"
rfid = 8462519551

# "INSERT INTO rfid (nombre,texto,rfid) VALUES ('Daniel Alejandro','Test Python 4',88843565);"
query = "INSERT INTO rfid (nombre,texto,ifid_id) VALUES ('" + nombre + "','" + texto + "'," + str(rfid) + ")"

print (query)