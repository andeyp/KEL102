# Beschreibung
Bibliothek zum schnellen Ansteuern von RND320 Steuerbare, elektronische Lasten auf Python-Basis
zu verwenden in Python-Programmen von Fritsch und AAST.

# Befehle:
    LoadInit(Type, Port):
        Type wird in der Config.ini festgelegt. Default ist "KEL"
        Port wird in der Config.ini festgelegt. Port im Ger�temanager sichtbar

    LoadExit:
        Schaltet das Ger�t aus, z.b. nach dem Beenden des Programmes oder nach einem Fehler um Ablauf und schlie�t den seriellen Port.

    LoadOn:
        Schaltet das Ger�t bzw. den Ausgang mit den eingestellten Werten ein. Diese Funktion wird nach jeder Werte�nderung automatisch aufgerufen. Soll nicht im eigenen Code verwendet werden.

    LoadSetCV(dValue)
        dValue ist ein float. Einstellen der Spannung. Nach der Funktion wechselt die Last auf "ON"

    LoadSetCC(dValue)
        dValue ist ein float. EInstellen des Stromes. Nach der Funktion wechselt die Last auf "ON"

    LoadSetPower(dValue)
        dValue ist ein float. Einstellen der maximalen Leistung (in Watt).

    LoadGetVoltage
        Liest den aktuellen Spannungswert aus. R�ckgabe in Datenformat float in der Variable fltValue
    
    LoadGetCurrent
        Liest den aktuellen Stromwert aus. R�ckgabe in Datenformat float in der Variable fltValue

    LoadGetPower
        Liest die aktuelle Leistung aus. R�ckgabe in Datenformat float in der Variable fltValue
