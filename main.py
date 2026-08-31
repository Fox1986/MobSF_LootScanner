#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-


#-----------------------------------------------------------------------------------------------#
# Title:            main.py                                                                     #
# Description:      Durchsucht Text-Dateien in einem Ordner nach bestimmten Keywords.           #
#                   Die Ergebnisse werden dann in einem Ordner Ergebnisse abgelegt              #
#                   Zu jeder analysierten Datei, wird eine separate Ergebnisdatei ausgegeben    #
# Author:           Hinrik Taeger                                                               #
# Version:          0.1.0                                                                       #
# Category:         Tool                                                                        #
#-----------------------------------------------------------------------------------------------#
import argparse
import os

PFAD_TEST = "./Testdateien/"
PFAD_ERGEBNIS = "./Ergebnisse/"
PFAD_KEYWORDS = "./Keywords"


def keywordlist(pfad_keywords):
    liste_keywords = []
    with open(pfad_keywords, "r", encoding="utf-8", errors="replace") as file:
        for line in file:
            word = line.strip("\n").strip()
            if word == "":
                continue
            elif word[0] == "#":
                continue
            if word == "//end":
                break
            else:
                liste_keywords.append(word)
    return liste_keywords


def findeTestdateien(pfad_test):
    return [f for f in os.listdir(pfad_test) if os.path.isfile(os.path.join(pfad_test, f))]


def ergebnisse(pfad_test, pfad_ergebnis, liste_test_dateien, liste_keywords):
    os.makedirs(pfad_ergebnis, exist_ok=True)
    for datei in liste_test_dateien:
        ergebnis_datei = os.path.join(pfad_ergebnis, "Ergebnis__" + datei)
        with open(os.path.join(pfad_test, datei), "r", encoding="utf-8", errors="replace") as lese_file:
            lines = lese_file.readlines()
        with open(ergebnis_datei, "w", encoding="utf-8") as schreib_file:
            for w in liste_keywords:
                schreib_file.write("\n" + "____________________" + w + "____________________" + "\n")
                w_lower = w.lower()
                for l in lines:
                    if w_lower in l.lower():
                        schreib_file.write(l)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Durchsucht Text-Dateien nach Keywords (z.B. MobSF-Dynamic-Analysis-Output)."
    )
    parser.add_argument('--input', default=PFAD_TEST, help=f"Ordner mit den zu durchsuchenden Dateien (Standard: {PFAD_TEST})")
    parser.add_argument('--output', default=PFAD_ERGEBNIS, help=f"Ordner für die Ergebnisdateien (Standard: {PFAD_ERGEBNIS})")
    parser.add_argument('--keywords', default=PFAD_KEYWORDS, help=f"Pfad zur Keywords-Datei (Standard: {PFAD_KEYWORDS})")
    args = parser.parse_args()

    test_dateien = findeTestdateien(args.input)
    keywords = keywordlist(args.keywords)
    ergebnisse(args.input, args.output, test_dateien, keywords)
    print(f"{len(test_dateien)} Datei(en) durchsucht, Ergebnisse liegen in {args.output}")
