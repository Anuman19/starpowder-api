# Starpowder Knights

## Abstract
In unserem Projekt haben wir eine Webseite erstellt auf der Umgebungsdaten, wie Temperatur, angezeigt werden.
Diese Daten werden durch einen Sensor gemessen und über eine API an die Webseite weitergeleitet.

## FrontEnd

Das Frontend umfasst eine simple Next Anwendung.
Diese lädt bei Aufrufen der Seiten die drei Umgebungsdaten Temperatur, Luftfeuchtigkeit und Luftdruck.
Diese werden auf der Seite angezeigt und können per Knopfdruck einzeln aktualisiert werden.

Die Webseite ruft die API in der api.js Klasse ab. 
Dort werden einfache GET Requests auf die einzelnen Daten gesetzt und diese somit erneuert.
Per Knopfdruck kann ein weiterer Request gesetzt werden um die Daten manuell zu erneuern.

## BackEnd

Das Backend baut sich aus drei Teilen zusammen.
Wir haben einerseits den [M5Stack](/send-temp.m5f), welche über den Sensor die Daten misst und diese an den MQTT Broker weitersendet.
Der M5Stack sendet alle 5 Sekunden die aktuellen Daten.

Der [MQTT Broker](/mqtt.py) sendet die Daten, welche er vom M5Stack erhält weiter an die API.

Die [API](/main.py) läuft auf einem Server (http://78.46.95.141:8000) und erhält vom MQTT Broker die Daten. 
Diese werden in der API Applikation in einem Python dict abgespeichert. 
Die API bietet die simple Funktionalität, dass man die Umgebungsdaten abfragen kann und neue Daten posten kann.

## Testing

| Abschnitt           | Inhalt                                                                                               |
|---------------------|:-----------------------------------------------------------------------------------------------------|
| ID                  | T-01                                                                                                 |
| Vorbedingung        | M5 gestartet, MQTT Broker läuft, Seite gestartet                                                     |
| Ablauf              | Auf die Webseite navigieren und diese mit (F5) neu laden                                             |
| Erwartetes Resultat | Es werden alle drei Umgebungsdaten (Temperature, Humidity, Pressure) angezeigt.                      |

| Abschnitt           | Inhalt                                                                                               |
|---------------------|:-----------------------------------------------------------------------------------------------------|
| ID                  | T-02                                                                                                 |
| Vorbedingung        | T-01 hat geklappt                                                                                    |
| Ablauf              | Auf der Webseite einmal auf alle drei Knöpfe mit "Reload!" drücken.                                  |
| Erwartetes Resultat | Die Werte werden neu geladen und angezeigt.                                                          |


## Fazit

Unser Projekt begann bereits mit dem Wissen, dass wir nichts grosses oder komplexes umsetzen werden. 
Daher lag für uns der Fokus von Anfang an auf einer simplen funktionierenden Funktion.

Zunächst haben wir also unsere API, den MQTT Broker und den M5Stack lokal über den Raspberry Pi laufen lassen und die Website auch auf diesem geöffnet.
Allerdings konnte man dadurch die Webseite nur innerhalb des IoT Netzes aufrufen. 
Daher haben wir uns entschieden die API auf einem Server laufen zu lassen, um den Zugriff aus verschiedensten Netzen zu ermöglichen.
Auch wenn das Projekt keine grosse oder komplexe Funktionalität bietet, sind wir damit zufrieden, dass wir eine kleine funktionale "Wetterstation" erstellt haben.