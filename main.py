#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-


#-----------------------------------------------------------------------------------------------#
# Title:            main.py                                                                     #
# Description:      Durchsucht Text-Dateien in einem Ordner nach bestimmten Keywords.           #
#                   Die Ergebnisse werden dann in einem Ordner Ergebnisse abgelegt              #
#                   Zu jeder analysierten Datei, wird eine separate Ergebnisdatei ausgegeben    #
# Author:           Hinrik Taeger                                                               #
# Version:          0.0.1                                                                       #
# Category:         Tool                                                                        #
# Tested System:    Ubuntu                                                                      #
# Date:             20.10.2020                                                                  #
#-----------------------------------------------------------------------------------------------#
import os

listePfadeTestDateien = []
listeErgebnisDateien = []
listeKeywords = []


def keywordlist():
    file = open("Keywords", "r")
    line = file.readlines()
    for l in line:
        word = l.strip("\n")
        listeKeywords.append(word)
    file.close()

def findeTestdateien():
    for file in os.listdir("./Testdateien"):
        pfadName = "./Testdateien/" + file
        listePfadeTestDateien.append(pfadName)


def erstelleErgebnisDatei():
    for file in os.listdir("./Testdateien"):
        newName = "Ergebnis__" + file
        listeErgebnisDateien.append(newName)
        newFile = open("./Ergebnisse/" + newName, "w+")
        newFile.close()


def suche():
    for file in listePfadeTestDateien:
        file = open(file, "r")
        lines = file.readlines()
        for l in lines:
            if "password" in l:
                print(l)
        file.close()


if __name__ == '__main__':
    erstelleErgebnisDatei()
    findeTestdateien()
    keywordlist()
    suche()