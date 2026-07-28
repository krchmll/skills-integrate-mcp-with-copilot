import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from app import activities


class AppTests(unittest.TestCase):
    def test_github_skills_activity_is_available(self):
        self.assertIn("GitHub Skills", activities)
        self.assertEqual(
            activities["GitHub Skills"]["description"],
            "Learn practical coding and collaboration skills through GitHub-focused workshops"
        )


if __name__ == "__main__":
    unittest.main()
