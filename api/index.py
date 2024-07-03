from flask import Flask, send_file, request, render_template
import io
import gtts
import pypinyin
import os
app = Flask(__name__)
sep = os.path.sep

@app.route('/')
def home():
    return render_template('main.html')


@app.route('/sound')
def background_process():
    original = request.args.get("text")
    new = original[::-1]
    pyin = pypinyin.core.lazy_pinyin(new)
    for i in pyin:
        pyin[pyin.index(i)] = i[::-1]
    print(pyin)
    txt = "".join(pyin)
    sound1 = gtts.gTTS(text=txt, lang='en', slow=False)
    sound = io.BytesIO()
    sound1.write_to_fp(sound)
    sound.seek(0)
    return send_file(sound, mimetype="audio/wav")


if __name__ == '__main__':
    app.run("127.0.0.1", 2333)
