from pathlib import Path
from flask import Flask, send_from_directory

from build_content import PROFILES, format_html, format_index_html


BASE_PATH = Path(__file__).parent.parent

app = Flask(__file__)


def register_profile(profile: str, base_path: str) -> None:
    def index():
        return format_index_html(profile)

    def index_en():
        return format_html("en", profile)

    def index_ru():
        return format_html("ru", profile)

    app.add_url_rule(f"{base_path}/", f"{profile}_index", index)
    app.add_url_rule(f"{base_path}/en", f"{profile}_en", index_en)
    app.add_url_rule(f"{base_path}/ru", f"{profile}_ru", index_ru)


for profile, settings in PROFILES.items():
    register_profile(profile, settings["base_path"])


SERVE_DIRECTORIES = ["css", "fonts", "js"]


@app.route("/<path:directory>/<path:filename>")
def serve_static(directory, filename):
    if directory not in SERVE_DIRECTORIES:
        return "This directory is not served.", 403

    return send_from_directory(BASE_PATH / directory, filename)


if __name__ == "__main__":
    app.run(debug=True)
