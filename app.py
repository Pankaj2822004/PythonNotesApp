from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Function to load notes from JSON file
def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save notes to JSON file
def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file)

@app.route('/')
def index():
    notes = load_notes()
    return render_template('index.html', notes=notes)

@app.route('/add_note', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_note = {'title': title, 'content': content}
        notes = load_notes()
        notes.append(new_note)
        save_notes(notes)
        return redirect(url_for('index'))
    return render_template('add_note.html')



@app.route('/edit_note', methods=['POST'])
def edit_note():
    data = request.form
    old_title = data['old_title']
    new_title = data['title']
    new_content = data['content']
    
    # Update the note in the JSON file
    with open('notes.json', 'r') as file:
        notes = json.load(file)

    for note in notes:
        if note['title'] == old_title:
            note['title'] = new_title
            note['content'] = new_content
            break

    with open('notes.json', 'w') as file:
        json.dump(notes, file)

    return redirect('/')

@app.route('/delete_note', methods=['POST'])
def delete_note():
    title = request.form['title']
    notes = load_notes()
    notes = [note for note in notes if note['title'] != title]
    save_notes(notes)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



