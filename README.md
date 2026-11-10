# FocusTimer

Plan a complete pomodoro focus schedule on paper: focus blocks, short breaks and long breaks, with exact start and end times.

**Honest note:** FocusTimer prints a plan. It does NOT wait in real time, count down, or beep when a block ends. Use the printed schedule with whatever clock or timer you already like.

## Requirements

- Python 3
- Standard library only — nothing to install

## Usage

A default day: four 25-minute focus sessions starting at 09:00, with a
5-minute break between sessions.

```bash
python3 focustimer.py --sessions 4 --start 09:00
```

Five sessions, where the break after the fourth session is the long one:

```bash
python3 focustimer.py --sessions 5 --start 09:00
```

### Options

| Option | Default | Meaning |
|---|---|---|
| `--sessions` | 4 | Number of focus blocks |
| `--focus` | 25 | Focus block length in minutes |
| `--break` | 5 | Short break length in minutes |
| `--long-break` | 15 | Long break length in minutes |
| `--every` | 4 | Every Nth break is the long break |
| `--start` | 09:00 | Start time, HH:MM |

Rules: a break follows every focus block except the last one. The break
after session N is the long break when N is a multiple of `--every`.
Times wrap past midnight naturally. See `examples.md` for real output.

## License

MIT — see `LICENSE`.
