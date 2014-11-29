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
import random,math

class GrammarLoader:

    def __init__(self, filename):
        self._filename = "./Grammar_Files/" + filename
        self._grammar = {}

    def load_grammar(self):

        grammar_file = open(self._filename, 'r')
        grammar = {}
        for line in grammar_file.readlines():

            if not line.startswith("#") and not line.strip()=="":
                line = line.strip()
                symbol = "#" + line.split(":")[0] + "#"
                tokens = line.split(":")[1].split(";")
                random.shuffle(tokens)
                grammar[symbol] = tokens

        self._grammar = grammar

    def get_random_expansion(self, tag):
        midway = math.floor(len(self._grammar[tag])/2)
        choice = random.randint(midway, len(self._grammar[tag]) - 1)
        value = self._grammar[tag].pop(choice)
        self._grammar[tag].insert(0, value)
        return self._grammar[tag][0]