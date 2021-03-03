#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# lyrics_processor_test.py

# University of Zurich
# Department of Computational Linguistics

# Authors: # TODO
# Matriculation Numbers: #TODO


# Test Units for Lyrics Analyzer Engine
# Module for functional and non functional testing of lyrics_processor module

# Import Statements
from unittest import TestCase, main
import lyrics_processor as lp
from os import path


class LpTest(TestCase):
    """
    lyrics_processor non functional tests
    """

    def test_output_split_up_lines_function(self):
        lyrics = 'It was you,. That showed me who I am..'
        result = lp.split_up_lines(lyrics)
        self.assertIsInstance(result, list, "Required type of output is list")

    def test_output_tokenize_lines_function(self):
        split_lyrics = ['It was you,', 'That showed me who I am.']
        result = lp.tokenize_lines(split_lyrics)
        self.assertIsInstance(result, list, "Required type of output is list")
        self.assertIsInstance(result[0], list, "Required inner type is list")
        
    def test_output_filter_profanity_function(self):
        tokenized_lyrics = [['Huh', ',', 'it\'s', 'pissing', 'me', 'off', '.'], ['Rock', 'me', 'baby']]
        result = lp.filter_profanity(tokenized_lyrics, 'profane_words.txt')
        self.assertIsInstance(result, tuple, "Required type of output is tuple")
        self.assertIsInstance(result[0], list, "Required inner type is list")
        self.assertIsInstance(result[1], int, "Required inner type is int")

    def test_output_print_lyrics_function(self):
        lyrics = [['It', 'was', 'you', ','], ['That', 'showed', 'me', 'who', 'I', 'am', '.']]
        self.assertIsNone(lp.print_lyrics(lyrics), "Required type of output is None")

    def test_existence_answer_file(self):
    	self.assertTrue(path.exists("task_5.txt"), "Add a text file named task_5.txt with answers for task 5")

    """
    lyrics_processor functional tests: to be extended according to description
    """

    def test_split_up_lines_function(self):
        lyrics = 'It was you,. That showed me who I am..'
        result = lp.split_up_lines(lyrics)
        self.assertEqual(['It was you,', 'That showed me who I am.'], result, "Lines are not split up correctly at last dot after every line")
        # TODO: extend with two assertions

    def test_tokenize_lines_function(self):
        split_lyrics = ['It was you,', 'That showed me who I am.']
        result = lp.tokenize_lines(split_lyrics)
        self.assertEqual([['It', 'was', 'you', ','], ['That', 'showed', 'me', 'who', 'I', 'am', '.']], result, "Line tokenization incorrect")
        # TODO: extend with two assertions

    def test_filter_profanity_function(self):
        tokenized_lyrics = [['Huh', ',', 'it\'s', 'pissing', 'me', 'off', '.'], ['Rock', 'me', 'baby']]
        result = lp.filter_profanity(tokenized_lyrics, 'profane_words.txt')
        self.assertEqual(([['Huh', ',', 'it\'s', '#######', 'me', 'off', '.'], ['Rock', 'me', 'baby']], 1), result, "Profane words are not censored correctly or are counted incorrectly")
        # TODO: extend with two assertions


if __name__ == '__main__':
    main()
