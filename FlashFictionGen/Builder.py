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
import re, random

class Builder:

    def expand_phrase_until_complete(self, grammar, sentence):

        while "#" in sentence:
            to_replace = re.findall(r'[#]\S*[#]', sentence)
            tag = (random.choice(to_replace))
            replacement = grammar.get_random_expansion(tag)
            sentence = sentence.replace(tag, replacement, 1)
        return sentence