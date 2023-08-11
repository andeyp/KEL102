# Beschreibung
Bibliothek zum schnellen Ansteuern von RND320 Steuerbare, elektronische Lasten auf Python-Basis
zu verwenden in Python-Programmen von Fritsch Elektronik GmbH und ASSA ABLOY Albstadt.

#### Befehle:

```LoadInit(Type, Port):```
Type wird in der Config.ini festgelegt. Default ist "KEL".
Port wird in der Config.ini festgelegt. Port im Gerätemanager sichtbar, z.b. 
```[LOAD]```
```type = KEL```
```com = COM257```

```LoadExit:```
Schaltet das Gerät aus, z.b. nach dem Beenden des Programmes oder nach einem Fehler um Ablauf und schließt den seriellen Port.

```LoadOn:```
Schaltet das Gerät bzw. den Ausgang mit den eingestellten Werten ein. Diese Funktion wird nach jeder Werteänderung automatisch aufgerufen. Soll nicht im eigenen Code verwendet werden.

```LoadOff:```
Schaltet das Gerät bzw. den Ausgang aus.

```LoadSetCV(dValue)```
dValue ist ein float. Einstellen der Spannung. Nach der Funktion wechselt die Last auf "ON".

```LoadSetCC(dValue)```
dValue ist ein float. EInstellen des Stromes. Nach der Funktion wechselt die Last auf "ON".

```LoadSetPower(dValue)```
dValue ist ein float. Einstellen der maximalen Leistung (in Watt).

```LoadGetVoltage```
Liest den aktuellen Spannungswert aus. Rückgabe muss mit     
    ```result, rawValue = kel102.LoadGetVoltage()```
    ```rawValue = rawValue[:-1]```
    ```fltValue = float(rawValue[:-1])```
im eigentlichen Code umgewandelt werden. 

```LoadGetCurrent```
Liest den aktuellen Stromwert aus. Rückgabe muss mit     
    ```result, rawValue = kel102.LoadGetCurrent()```
    ```rawValue = rawValue[:-1]```
    ```fltValue = float(rawValue[:-1])```
im eigentlichen Code umgewandelt werden. 

```LoadGetPower```
Liest die aktuelle Leistung aus. Rückgabe muss mit     
    ```result, rawValue = kel102.LoadGetPower()```
    ```rawValue = rawValue[:-1]```
    ```fltValue = float(rawValue[:-1])```
im eigentlichen Code umgewandelt werden. 
