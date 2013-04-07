# -*- coding: iso-8859-1 -*-
import datetime
import unittest
import os

import PyLiterDB
print(PyLiterDB.__file__)

vals1 = [('simon', datetime.date(1984, 8, 17), 26)]
vals2 = [('camille', datetime.date(1986, 12, 12), 24),
         ('jean', datetime.date(1989, 6, 12), 21),
         ('florence', datetime.date(1994, 1, 14), 17),
         ('marie-anne', datetime.date(1999, 1, 28), 12)]
vals3 = [('éçùï', datetime.date(2000, 10, 10), 55)]
vals = vals1 + vals2 + vals3
filename = "test.pdl"


class TestPyLiterDB(unittest.TestCase):
    def setUp(self, empty=False):
        self.db = PyLiterDB.DB(filename)
        self.db.create("name", "birth", "age", mode="override")
        if not empty:
            for val in vals:
                self.db.insert(*val)

    def tearDown(self):
        self.db.commit()
        os.remove(filename)
        del self.db

    def test_db_insert(self):
        self.tearDown()
        self.setUp(empty=True)  # For this test we want an empty database
        for i, val in enumerate(vals):
            self.assertEqual(self.db.insert(*val), i)  # Ensure we get the ID.
        self.assertEqual(len(self.db), len(vals))  # Ensure
        # Everything was inserted.

    def test_db_select1(self):
        for i, v in enumerate(vals1):
            rec = self.db[i]  # Record should be Ith item in DB
            for j, field in enumerate(self.db.fields):  # j = counter
                self.assertEqual(rec[field], v[j])  # Ensure rec's field is
                # the same as origional lists j (?)

    def test_db_select2(self):
        self.assertEqual(self.db(name='foo'), [])  # Ensure get an empty list
        # when searching for non-existing item
        self.assertEqual(self.db(name='éçùï')[0]['birth'],
                         datetime.date(2000, 10, 10))  # Data integrity check

    def test_db_iter(self):
        self.assertEqual(len([x for x in self.db]),
                         len(self.db))  # Ensure length returns right number.

        for val in vals:  # Ensure we get data back in the right order.
            self.assertEqual([x for x in self.db if x['name'] == val],
                             self.db(name=val))
            self.assertEqual([x for x in self.db if x['birth'] == val],
                             self.db(birth=val))
            self.assertEqual([x for x in self.db if x['age'] == val],
                             self.db(age=val))

    def test_db_update(self):
        for record in self.db:
            self.db.update(record, name=record['name'].capitalize())
            # Capitalize all the names.
        self.assertEqual(self.db[0]['name'], "Simon")  # Ensure it was actually
        # Capitalized.

    def test_db_delete(self):
        self.db.delete(self.db(name="simon"))  # Delete simon from db
        self.assertEqual(self.db(name='simon'), [])  # Ensure he's no longer.
        self.assertEqual(len(self.db), len(vals) - 1)  # Ensure list is 1 short


if __name__ == "__main__":
    unittest.main()
