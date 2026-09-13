import io
from contextlib import redirect_stdout
from unittest.mock import patch

import queue


def test_queue_commands():
    input_text = "\n".join(
        [
            "15",
            "push 1",
            "push 2",
            "front",
            "back",
            "size",
            "empty",
            "pop",
            "pop",
            "pop",
            "size",
            "empty",
            "pop",
            "push 3",
            "empty",
            "front",
        ]
    )
    expected = "\n".join(["1", "2", "2", "0", "1", "2", "-1", "0", "1", "-1","0","3"])

    output = io.StringIO()
    with patch("builtins.input", side_effect=input_text.splitlines()), redirect_stdout(output):
        queue.queue.clear()
        queue.main()

    assert output.getvalue().strip() == expected
