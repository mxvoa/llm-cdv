import unittest

from chunker import chunk_text


class ChunkTextTests(unittest.TestCase):
    def test_chunks_into_limit_sized_parts(self):
        self.assertEqual(
            chunk_text("one two three four five", 2),
            ["one two", "three four", "five"],
        )

    def test_preserves_word_order_spelling_and_punctuation(self):
        self.assertEqual(
            chunk_text("Hello, WORLD! don't stop.", 2),
            ["Hello, WORLD!", "don't stop."],
        )

    def test_empty_text_returns_empty_list(self):
        self.assertEqual(chunk_text("", 3), [])

    def test_whitespace_only_text_returns_empty_list(self):
        self.assertEqual(chunk_text("  \t\n", 3), [])

    def test_nonpositive_limit_raises_value_error_even_for_empty_text(self):
        for limit in (0, -1):
            with self.subTest(limit=limit):
                with self.assertRaises(ValueError):
                    chunk_text("", limit)

    def test_single_word(self):
        self.assertEqual(chunk_text("word", 1), ["word"])


if __name__ == "__main__":
    unittest.main()
