# -*- coding: utf-8 -*-
import subprocess

if __name__ == '__main__':
    cmd = "pdflatex C:/Users/吴青峰/PycharmProjects/math_to_csv/test.tex"
    s = subprocess.Popen(cmd, shell=True)
    while True:
        if s.poll() is not None:
            break
