# FocusTimer — Examples

Real output captured from actual runs.

## Four sessions (the default shape)

```bash
python3 focustimer.py --sessions 4 --start 09:00
```

```
09:00-09:25 Focus 1
09:25-09:30 Break
09:30-09:55 Focus 2
09:55-10:00 Break
10:00-10:25 Focus 3
10:25-10:30 Break
10:30-10:55 Focus 4
Total: 115 minutes, ends at 10:55
```

## Five sessions — the break after session 4 is the long break

With the default `--every 4`, the break after every fourth session is the
long break (15 minutes by default).

```bash
python3 focustimer.py --sessions 5 --start 09:00
```

```
09:00-09:25 Focus 1
09:25-09:30 Break
09:30-09:55 Focus 2
09:55-10:00 Break
10:00-10:25 Focus 3
10:25-10:30 Break
10:30-10:55 Focus 4
10:55-11:10 Long break
11:10-11:35 Focus 5
Total: 155 minutes, ends at 11:35
```
