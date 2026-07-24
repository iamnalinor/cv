from datetime import datetime
from pathlib import Path
import tempfile
from typing import Literal

from minify_html import minify
from content import analyst, developer
from jinja2 import Environment, FileSystemLoader
from pylatex import Document

import os
import re
import shutil
import subprocess
import sys

import pytinytex

BASE_PATH = Path(__file__).parent.parent

DIST_PATH = BASE_PATH / "dist"
CSS_PATH = BASE_PATH / "css"
FONTS_PATH = BASE_PATH / "fonts"
CMU_FONTS_PATH = BASE_PATH / "fonts" / "cm-unicode"
JS_PATH = BASE_PATH / "js"
FAVICON_PATH = BASE_PATH / "favicon.ico"
ROBOTS_TXT_PATH = BASE_PATH / "robots.txt"

PROFILES = {
    "default": {
        "header": developer.HEADER,
        "blocks": developer.BLOCKS,
        "base_path": "",
        "pdf_en": "Albert_Zuev_CV.pdf",
        "pdf_ru": "Albert_Zuev_CV_Russian.pdf",
    },
    "analyst": {
        "header": analyst.HEADER,
        "blocks": analyst.BLOCKS,
        "base_path": "/analyst",
        "pdf_en": "Albert_Zuev_Analyst_CV.pdf",
        "pdf_ru": "Albert_Zuev_Analyst_CV_Russian.pdf",
    },
}


def html_to_latex(content: str) -> str:
    # Convert <b>...</b> to \textbf{...}
    content = re.sub(r"<b>(.*?)</b>", r"\\textbf{\1}", content, flags=re.DOTALL)

    # Convert <i>...</i> to \textit{...}
    content = re.sub(r"<i>(.*?)</i>", r"\\textit{\1}", content, flags=re.DOTALL)

    # Convert <a href="url">text</a> to \href{url}{text}
    content = re.sub(
        r'<a\s+href=[\'"]([^\'"]+)[\'"]>(.*?)</a>',
        r"\\href{\1}{\2}",
        content,
        flags=re.DOTALL,
    )

    return content.replace("&", r"\&").replace("#", r"\#").replace("%", r"\%")


def prepare_content[T: list[T] | dict[str, T] | str](
    content: T,
    output_type: Literal["html", "latex"],
    selected_variant: str | None = None,
) -> T:
    """
    Prepare content for display.

    Variant can be specified to choose specific variant (e.g. language) of mapping values.
    For example: given a dict
    {
        "name": "variant 0",
        "name__1": "variant 1",
    },
    with variant="1" the result will be {"name": "variant 1"}.
    If selected variant does not exist, rollback to default variant.
    """

    if isinstance(content, bool):
        return content

    if isinstance(content, str):
        if output_type == "html":
            return content.replace("--", "—")

        return html_to_latex(content)

    if isinstance(content, list):
        return [prepare_content(x, output_type, selected_variant) for x in content]

    if not isinstance(content, dict):
        raise ValueError(
            "prepare_content accepts only values of dict, list, and str types"
        )

    result = {}

    for key, value in content.items():
        key_name, _, key_variant = key.partition("__")

        has_selected = (
            selected_variant is not None
            and f"{key_name}__{selected_variant}" in content
        )

        if has_selected and key_variant != selected_variant:
            continue

        if not has_selected and key_variant != "":
            continue

        result[key_name] = prepare_content(value, output_type, selected_variant)

    return result


def format_html(variant: str | None = None, profile: str = "default") -> str:
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("cv.html")

    language = "ru" if "ru" in variant else "en"
    date = datetime.now().strftime("%d.%m.%Y" if language == "ru" else "%Y-%m-%d")
    pdf_filename = PROFILES[profile]["pdf_ru" if language == "ru" else "pdf_en"]

    rendered = template.render(
        header=prepare_content(PROFILES[profile]["header"], "html", variant),
        blocks=prepare_content(PROFILES[profile]["blocks"], "html", variant),
        date=date,
        language=language,
        pdf_filename=pdf_filename,
        base_path=PROFILES[profile]["base_path"],
    )
    return minify(rendered)


def format_index_html(profile: str = "default") -> str:
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("index.html")

    rendered = template.render(base_path=PROFILES[profile]["base_path"])
    return minify(rendered)


def format_latex(variant: str, profile: str = "default") -> str:
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("cv.tex")

    return template.render(
        header=prepare_content(PROFILES[profile]["header"], "latex", variant),
        blocks=prepare_content(PROFILES[profile]["blocks"], "latex", variant),
        language="ru" if "ru" in variant else "en",
    )


def build_latex_pdf(output_path: Path, variant: str, profile: str = "default") -> bytes:
    rendered = format_latex(variant, profile)

    output_path.with_suffix(".tex").write_text(rendered, encoding="utf-8")

    doc = Document(default_filepath=output_path.with_suffix(""))
    doc.generate_tex = lambda _: None  # skip tex generation

    if "ru" in variant:
        exe = "xelatex.exe" if sys.platform == "win32" else "xelatex"
        compiler = os.path.join(pytinytex.get_tinytex_path(), exe)
    else:
        compiler = pytinytex.get_pdflatex_engine()

    try:
        doc.generate_pdf(compiler=compiler)
    except UnicodeDecodeError:
        log_file = output_path.with_suffix(".log")
        print(log_file.read_text(encoding="utf-8", errors="ignore"))
        raise


def ensure_cmu_fonts() -> None:
    bin_path = Path(pytinytex.get_tinytex_path())
    font_dir = bin_path.parent.parent / "texmf-dist/fonts/opentype/public/cm-unicode"
    font_dir.mkdir(parents=True, exist_ok=True)

    missing = [
        f for f in CMU_FONTS_PATH.glob("*.otf") if not (font_dir / f.name).is_file()
    ]
    if not missing:
        return

    for font_file in missing:
        shutil.copy2(font_file, font_dir / font_file.name)

    exe = "mktexlsr.exe" if sys.platform == "win32" else "mktexlsr"
    subprocess.run([bin_path / exe], check=True, capture_output=True)


def main() -> None:
    DIST_PATH.mkdir(exist_ok=True)

    try:
        pytinytex.get_tinytex_path()
    except RuntimeError:
        with tempfile.TemporaryDirectory() as tempdir:
            pytinytex.download_tinytex(variation=2, download_folder=tempdir)

        for pkg in ["collection-langcyrillic", "babel-russian"]:
            pytinytex.install(pkg)

    ensure_cmu_fonts()

    for profile, settings in PROFILES.items():
        profile_dist = DIST_PATH / settings["base_path"].lstrip("/")
        profile_dist.mkdir(exist_ok=True)

        for language in ["en", "ru"]:
            (profile_dist / f"{language}.html").write_text(
                format_html(language, profile),
                encoding="utf-8",
            )

        (profile_dist / "index.html").write_text(
            format_index_html(profile),
            encoding="utf-8",
        )

        build_latex_pdf(DIST_PATH / settings["pdf_en"], "en", profile)
        build_latex_pdf(DIST_PATH / settings["pdf_ru"], "ru", profile)

    shutil.copytree(CSS_PATH, DIST_PATH / "css", dirs_exist_ok=True)
    shutil.copytree(FONTS_PATH, DIST_PATH / "fonts", dirs_exist_ok=True)
    shutil.copytree(JS_PATH, DIST_PATH / "js", dirs_exist_ok=True)
    shutil.copy2(FAVICON_PATH, DIST_PATH)
    shutil.copy2(ROBOTS_TXT_PATH, DIST_PATH)


if __name__ == "__main__":
    main()
