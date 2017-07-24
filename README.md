Attendee Notes
==============

This project keeps track of event attendees. However, just like our real
attendees, they sometimes misbehave. The people running our events would
like to keep track of these misbehaviors and tell each other about them.
To do this, we're going to add the ability to create notes about
attendees.

The models and CRUD endpoints for Attendees already exist, but the
models and CRUD endpoints for these attendee notes do not. The task here
is to create the model(s), endpoints, and views to add notes to
attendees.

Here's a quick rundown of our requirements:

1. Must have the ability to create notes, and associate those with an
   attendee.
2. Must have the ability to retrieve all notes.
3. Must have the ability to retrieve all notes for a given attendee.
4. Must NOT be able to delete or edit a specific note.


If there's time, we should also implement the following:

1. Add notes to the serialization of an attendee, but make it optional
2. Update our API to optionally include notes when retrieving attendees
3. Clean up the repoistory a bit (separate concerns, use more Flask features, etc)


Here are a few assumptions we can make about this task:

1. This is just an API, so we don't need to worry about templates. Our
   view functions can just return JSON directly.
2. We can ignore authentication for the sake of this task.


Installation
------------

1. Clone this repository
2. Create a virtual environment

        # In Python 2:
        $> pip install virtualenv
        $> virtualenv venv

        # In Python3, up to 3.6:
        $> pyvenv venv

        # In Python 3.6 and above:
        $> python3 -m venv venv

3. Activate the virtual environment

        $> source venv/bin/activate

4. Install requirements

        $> pip install -r requirements.txt

5. Run the dev server

        $> python app.py

6. Confirm that everything is working

        $> curl http://localhost:5000/attendees

8. Create a few test attendees

        $> curl \
            -X POST \
            "http://localhost:5000/attendees?first_name=Doc&last_name=McStuffins"
        $> curl \
            -X POST \
            "http://localhost:5000/attendees?first_name=Chilly&last_name=McStuffins"

9. Create a new git branch (use your name as the branch name), and let's get started!

