#!/usr/bin/python
# coding: utf-8
#
# Something, Somewhere, copyright (c) 2014 Ben Kybartas <b.a.kybartas@tudelft.nl>
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
# SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR
# IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
#
# 29 November 2014

__author__ = 'Ben'

from GrammarLoader import GrammarLoader
from Builder import Builder

def get_word_count(novel):
    return len(novel.split())

filename = "SomethingSomewhere.tex"
title = "Somewhere, Something"
author = "Ben Kybartas"
latex_header = "\\documentclass{report}\n\\title{" + title + "}\n\\author{" + author + "}\n\\date{}\n\\begin{document}\n\\maketitle"
latex_footer = "\\end{document}"

#This will eventually be a 50k word novel
novel = ""

#Load our grammar
loader = GrammarLoader("NaNoGenMo2014_Grammar.txt")
loader.load_grammar()

#Set up the builder
builder = Builder()

#Our current story
story_number = 0

while(get_word_count(novel) < 50000):

    #increment story number
    story_number += 1

    #Generate a line
    new_line = builder.expand_phrase_until_complete(loader, "#main#")

    #Fix some stuff
    new_line = new_line[0].upper() + new_line[1:]
    new_line = new_line.replace("  ", " ")

    #Yeah its a hack
    new_line = new_line.replace(" a a", " an a")
    new_line = new_line.replace(" a e", " an e")
    new_line = new_line.replace(" a i", " an i")
    new_line = new_line.replace(" a o", " an o")
    new_line = new_line.replace(" a u", " an u")
    new_line = new_line.replace(" A a", " An a")
    new_line = new_line.replace(" A e", " An e")
    new_line = new_line.replace(" A i", " An i")
    new_line = new_line.replace(" A o", " An o")
    new_line = new_line.replace(" A u", " An u")

    #Split up our lines
    new_line = new_line.replace(". ", ".\n\n")

    #Add the header
    new_line = "~\n\n" + new_line

    #Add it to our novel
    novel += "\\chapter*{" + str(story_number) + "}\n" + new_line + "\n"

#Write the novel
file = open("Result\\" + filename, "w")
file.write(latex_header)
file.write(novel)
file.write(latex_footer)
file.close()