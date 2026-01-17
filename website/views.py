# We will crete teh first routs, like login page, home-page, 

# First we start with flask:
from flask import Blueprint, render_template
# This has so much routs here, has URL, 
from flask_login import login_required, current_user

views = Blueprint('views', __name__) # Recc: call the same name

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    data = request.get_json()
    note_id = data.get('noteId')

    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()

    return jsonify({})

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

