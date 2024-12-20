import json
import os

def load_notes(notes_file):
    """Load notes from a file."""
    if not os.path.exists(notes_file):
        return []
    with open(notes_file, "r") as file:
        return json.load(file)

def save_notes(notes_file, notes):
    """Save notes to a file."""
    with open(notes_file, "w") as file:
        json.dump(notes, file)

def add_note_to_file(notes_file, title, content):
    """Add a new note to the file."""
    notes = load_notes(notes_file)
    notes.append({"title": title, "content": content})
    save_notes(notes_file, notes)

def delete_note_from_file(notes_file, note_id):
    """Delete a note by index."""
    notes = load_notes(notes_file)
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
        save_notes(notes_file, notes)
