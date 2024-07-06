from flask import Flask, send_file, request, render_template
import io
import gtts
import os
from pydub import AudioSegment
app = Flask(__name__)
sep = os.path.sep

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/sound')
def background_process():
    original = request.args.get("text")
    print(original)
    sound1 = gtts.gTTS(text=original, lang='zh-CN', slow=False)
    sound = io.BytesIO()
    sound1.write_to_fp(sound)
    sound.seek(0)
    original_audio = AudioSegment.from_file(sound, "wav")
    backward = original_audio.reverse()
    real = io.BytesIO()
    backward.export(real, format="wav")
    return send_file(real, mimetype="audio/wav")


if __name__ == '__main__':
    app.run("127.0.0.1", 2333)
