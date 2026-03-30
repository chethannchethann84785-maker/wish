from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# ─────────────────────────────────────────
#  C U S T O M I Z E   H E R E
# ─────────────────────────────────────────
BIRTHDAY_PERSON = "YASHU"           # Her name
BIRTHDAY_MESSAGE = (
    "Every moment spent with you is a gift I'll always treasure. "
    "On your special day, I want you to know that you light up every time"
    "you walk into and make every day brighter just by being you. "
    "Happy Birthday, my Yashu! 🎂"
)
SENDER_NAME = "Forever Yours ❤️"   # Who is sending
ACCENT_COLOR = "#FF6B9D"           # Main theme color (pink)
# ─────────────────────────────────────────


@app.route("/")
def index():
    return render_template(
        "index.html",
        name=BIRTHDAY_PERSON,
        message=BIRTHDAY_MESSAGE,
        sender=SENDER_NAME,
        accent=ACCENT_COLOR,
    )


@app.route("/api/photos")
def get_photos():
    """Return list of photo filenames from the static/photos folder."""
    photos_dir = os.path.join(app.static_folder, "photos")
    supported = {".jpg", ".jpeg", ".png", ".gif", ".webp"}
    photos = []
    if os.path.isdir(photos_dir):
        for f in sorted(os.listdir(photos_dir)):
            if os.path.splitext(f)[1].lower() in supported:
                photos.append(f"/static/photos/{f}")
    return jsonify(photos)


if __name__ == "__main__":
    print("\n🎂  Birthday App is running!")
    print("   Open  →  http://localhost:5000\n")
    app.run(debug=True, port=5000)
