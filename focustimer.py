#!/usr/bin/env python3
"""FocusTimer - plan a complete pomodoro focus schedule on paper.

Prints a full focus/break schedule with start and end times. It does NOT
wait in real time and does not beep; it just plans the day.

Standard library only.
"""

import argparse
import sys


def parse_start(value):
    """Parse an HH:MM string into minutes since midnight."""
    parts = value.split(":")
    if len(parts) != 2:
        raise ValueError("expected HH:MM")
    try:
        hours = int(parts[0])
        minutes = int(parts[1])
    except ValueError:
        raise ValueError("expected HH:MM with numbers")
    if not (0 <= hours <= 23 and 0 <= minutes <= 59):
        raise ValueError("hour must be 00-23 and minute 00-59")
    return hours * 60 + minutes


def fmt(minutes):
    """Format minutes since midnight as HH:MM, wrapping past 24h."""
    minutes %= 24 * 60
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def build_schedule(sessions, focus, break_minutes, long_break, every, start):
    lines = []
    now = start
    for k in range(1, sessions + 1):
        end = now + focus
        lines.append(f"{fmt(now)}-{fmt(end)} Focus {k}")
        now = end
        if k < sessions:
            if k % every == 0:
                length = long_break
                label = "Long break"
            else:
                length = break_minutes
                label = "Break"
            end = now + length
            lines.append(f"{fmt(now)}-{fmt(end)} {label}")
            now = end
    total = now - start
    lines.append(f"Total: {total} minutes, ends at {fmt(now)}")
    return lines


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Plan a complete pomodoro focus schedule on paper."
    )
    parser.add_argument("--sessions", type=int, default=4,
                        help="number of focus sessions (default: 4)")
    parser.add_argument("--focus", type=int, default=25,
                        help="focus block length in minutes (default: 25)")
    parser.add_argument("--break", dest="break_minutes", type=int, default=5,
                        help="short break length in minutes (default: 5)")
    parser.add_argument("--long-break", type=int, default=15,
                        help="long break length in minutes (default: 15)")
    parser.add_argument("--every", type=int, default=4,
                        help="every Nth break is the long break (default: 4)")
    parser.add_argument("--start", default="09:00",
                        help="start time as HH:MM (default: 09:00)")
    args = parser.parse_args(argv)

    if args.sessions < 1:
        parser.error("--sessions must be at least 1")
    if args.focus < 1:
        parser.error("--focus must be at least 1")
    try:
        start = parse_start(args.start)
    except ValueError:
        parser.error(f"invalid --start {args.start!r}: expected HH:MM (00:00-23:59)")

    for line in build_schedule(args.sessions, args.focus, args.break_minutes,
                               args.long_break, args.every, start):
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
