import unittest

from chatgtp.core import MessageRequest, build_response


class BuildResponseTests(unittest.TestCase):
    def test_build_response_with_values(self) -> None:
        result = build_response(MessageRequest(user_name="Ava", topic="testing"))
        self.assertEqual(
            result,
            "Hi Ava! Stage 2 is active and ready to discuss testing.",
        )

    def test_build_response_uses_defaults_for_blank_fields(self) -> None:
        result = build_response(MessageRequest(user_name="   ", topic=""))
        self.assertEqual(
            result,
            "Hi friend! Stage 2 is active and ready to discuss the project.",
        )


if __name__ == "__main__":
    unittest.main()
