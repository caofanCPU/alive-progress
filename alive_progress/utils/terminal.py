import sys
from functools import partial
from os import get_terminal_size as _terminal_size

if sys.stdout.isatty():
    def _send_ansi_escape(sequence, param=''):  # pragma: no cover
        return partial(sys.__stdout__.write, f'\x1b[{param}{sequence}')


    def terminal_cols():
        return _terminal_size()[0]
else:
    def _send_ansi_escape(_sequence, _param=''):  # pragma: no cover
        pass


    def terminal_cols():
        return 10000  # do not truncate if there's no tty.

clear_traces = _send_ansi_escape('2K\r')  # clears the entire line: CSI n K -> with n=2.
hide_cursor = _send_ansi_escape('?25l')  # hides the cursor: CSI ? 25 l.
show_cursor = _send_ansi_escape('?25h')  # shows the cursor: CSI ? 25 h.
factory_cursor_up = partial(_send_ansi_escape, 'A')  # sends cursor up: CSI {x}A.
