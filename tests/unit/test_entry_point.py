# -*- coding: utf-8 -*-

import unittest
import subprocess


class TestEntryPoint(unittest.TestCase):
    def test_execute_file(self):
        expected_output = u"""\xe0\xae\xb5\xe0\xae\xa3\xe0\xae\x95\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xae\xe0\xaf\x8d \xe0\xae\x89\xe0\xae\xb2\xe0\xae\x95\xe0\xae\xae\xe0\xaf\x8d!\n\xe0\xae\x87\xe0\xae\xa4\xe0\xaf\x81 \xe0\xae\x8e\xe0\xae\xa9\xe0\xaf\x8d \xe0\xae\xae\xe0\xaf\x81\xe0\xae\xa4\xe0\xae\xb2\xe0\xaf\x8d \xe0\xae\x8e\xe0\xae\xb4\xe0\xae\xbf\xe0\xae\xb2\xe0\xaf\x8d \xe0\xae\xa8\xe0\xae\xbf\xe0\xae\xb0\xe0\xae\xb2\xe0\xaf\x8d\n******* \xe0\xae\xb5\xe0\xae\xa3\xe0\xae\x95\xe0\xaf\x8d\xe0\xae\x95\xe0\xae\xae\xe0\xaf\x8d! \xe0\xae\xae\xe0\xaf\x80\xe0\xae\xa3\xe0\xaf\x8d\xe0\xae\x9f\xe0\xaf\x81\xe0\xae\xae\xe0\xaf\x8d \xe0\xae\x9a\xe0\xae\xa8\xe0\xaf\x8d\xe0\xae\xa4\xe0\xae\xbf\xe0\xae\xaa\xe0\xaf\x8d\xe0\xae\xaa\xe0\xaf\x8b\xe0\xae\xae\xe0\xaf\x8d *******\n"""  # noqa
        res = subprocess.Popen(['ezhili', '../hello.n'],
                               stdout=subprocess.PIPE)
        self.assertEqual(res.stdout.read(), expected_output)
