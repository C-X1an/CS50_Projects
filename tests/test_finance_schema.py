import importlib.util
import sqlite3
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

root = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("finance_initializer",root / "cs50x/Week9/finance/init_db.py")
initializer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(initializer)

class FinanceSchemaTest(unittest.TestCase):
    def test_database_has_only_empty_application_tables(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "finance.db"
            initializer.initialize_database(path)
            with closing(sqlite3.connect(path)) as database:
                for table in ["users","buy_history","sell_history","transaction_history"]:
                    self.assertEqual(database.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0],0)
                self.assertEqual(database.execute("PRAGMA integrity_check").fetchone()[0],"ok")
            original = path.read_bytes()
            with self.assertRaises(FileExistsError):
                initializer.initialize_database(path)
            self.assertEqual(path.read_bytes(),original)
