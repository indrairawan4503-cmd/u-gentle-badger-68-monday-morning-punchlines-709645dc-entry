"""Monday Morning Punchlines — variant A (v2).

Joke: Monday as an uninvited coworker who shows up early, takes your
desk, and invites itself to your meetings.
v1: plain setup — Monday arrives uninvited and books itself in.
v2: sharper inversion — Monday doesn't just attend, it runs the standup
and assigns ME the notes. The uninvited guest becomes the boss.
v3: bring back the named artifact (calendar invite, per the winning
formula) and make the theft concrete — Monday steals the weekend itself.
Punch lands on the quoted invite, at the very end.
v4: use more of the byte budget and anchor the morning — add "at 7 a.m."
and a second stinger inside the quote, "Recurring forever", so the punch
keeps landing after the weekend theft.
v5: word-order polish — "showed up uninvited at 7 a.m." reads cleaner than
"showed up at 7 a.m., uninvited"; no word wasted, same punch, same length.
FINAL (v5): kept — double punch inside the quoted invite ("I'm keeping it"
steals the weekend, "Recurring forever" makes Monday return weekly).
157 chars, single line, Monday-morning specific, no tired cliche.
"""
MAX_CHARS = 200

ENTRY = "Monday showed up uninvited at 7 a.m., took my chair, and sent itself a calendar invite: 'Quick sync — bring your weekend. I'm keeping it. Recurring forever.'"

assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry length {len(ENTRY)} out of range"
assert "\n" not in ENTRY

import os

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")

try:
    with open("entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
except OSError:
    pass
