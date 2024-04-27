from api.models import User, UserAnswer, AudioFile, Test
from react_flask_app.backend.api import create_app, db

app = create_app()
with app.app_context():
    current_user = User.query.order_by(User.id.asc()).first()
    print("current user:", current_user)
    answers = current_user.answers
    for answer in answers:
        audio_id = answer.audio_id
        audio = AudioFile.query.filter_by(id=audio_id).first()
        if (audio != None):
            print("genre:", audio.genre)
            print("mood:", audio.mood)
            print("vocal:" ,audio.vocal)