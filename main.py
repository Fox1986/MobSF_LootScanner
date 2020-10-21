#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-


#-----------------------------------------------------------------------------------------------#
# Title:            main.py                                                                     #
# Description:      Durchsucht Text-Dateien in einem Ordner nach bestimmten Keywords.           #
#                   Die Ergebnisse werden dann in einem Ordner Ergebnisse abgelegt              #
#                   Zu jeder analysierten Datei, wird eine separate Ergebnisdatei ausgegeben    #
# Author:           Hinrik Taeger                                                               #
# Version:          0.0.2                                                                       #
# Category:         Tool                                                                        #
# Tested System:    Ubuntu                                                                      #
# Date:             20.10.2020                                                                  #
#-----------------------------------------------------------------------------------------------#
import os

listeTestDateien = []
listeKeywords = []

pfadTest = "./Testdateien/"
pfadErgebnis = "./Ergebnisse/"


def keywordlist():
    file = open("Keywords", "r")
    line = file.readlines()
    for l in line:
        word = l.strip("\n")
        word2 = word.strip()
        if word2 == "":
            continue
        elif word2[0] == "#":
            continue
        if word2 == "//end":
            break
        else:
            if word2:
                listeKeywords.append(word2)
    file.close()


def findeTestdateien():
    for file in os.listdir(pfadTest):
        testDateien = file
        listeTestDateien.append(testDateien)


def erstelleErgebnisDatei(file):
    newFile = open(pfadErgebnis + file, "w+")
    newFile.close()


def schreibeErgebnis(fund, datei):
    file = open(datei, "a")
    file.write(fund)


def ergebnisse():
    for file in listeTestDateien:
        ergebnisFile = "Ergebnis__" + file
        erstelleErgebnisDatei(ergebnisFile)
        leseFile = open(pfadTest + file, "r")
        lines = leseFile.readlines()
        for w in listeKeywords:
            schreibeErgebnis("\n" + "____________________" + w + "____________________" + "\n", pfadErgebnis + ergebnisFile)
            for l in lines:
                if w in l:
                    schreibeErgebnis(l, pfadErgebnis + ergebnisFile)
        leseFile.close()





if __name__ == '__main__':
    findeTestdateien()
    keywordlist()
    ergebnisse()