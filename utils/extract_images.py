import os
import re
import base64
from pathlib import Path

ROOT = Path("docs")
IMAGE_DIR = ROOT / "images"
IMAGE_DIR.mkdir(exist_ok=True)

# ------------------------------------------------------------
# 1. Inline Markdown images:
#    ![alt](data:image/png;base64,XXXX)
# ------------------------------------------------------------
MD_INLINE = re.compile(
    r"""
    !

\[
        (?P<alt>.*?)              # alt text
    \]


    \(
        \s*
        data:image/
        (?P<ext>[^;]+)            # extension (png, jpeg, svg, etc.)
        ;base64,
        (?P<data>[A-Za-z0-9+/=\n\r]+?)   # Base64 payload
        \s*
    \)
    """,
    re.VERBOSE | re.DOTALL
)

# ------------------------------------------------------------
# 2. Inline HTML images:
#    <img src="data:image/png;base64,XXXX">
# ------------------------------------------------------------
HTML_INLINE = re.compile(
    r"""
    <img
        [^>]*?
        src="
            data:image/
            (?P<ext>[^;]+)        # extension
            ;base64,
            (?P<data>[A-Za-z0-9+/=\n\r]+?)   # Base64 payload
        "
        [^>]*?>
    """,
    re.VERBOSE | re.DOTALL
)

# ------------------------------------------------------------
# 3. Reference-style Base64 images:
#    [image5]: <data:image/png;base64,XXXX>
# ------------------------------------------------------------
MD_REFERENCE = re.compile(
    r"""
    ^
    

\[
        (?P<ref>[^\]

]+)           # reference name
    \]

:
    \s*
    <
        data:image/
        (?P<ext>[^;]+)            # extension
        ;base64,
        (?P<data>[A-Za-z0-9+/=\n\r]+?)   # Base64 payload
    >
    """,
    re.VERBOSE | re.MULTILINE | re.DOTALL
)

# ------------------------------------------------------------
# Save Base64 image to docs/images/
# ------------------------------------------------------------
def save_image(data_b64, ext, md_stem, counter):
    filename = IMAGE_DIR / f"{md_stem}_image_{counter}.{ext}"
    with open(filename, "wb") as f:
        f.write(base64.b64decode(data_b64))
    return filename.name

# ------------------------------------------------------------
# Process a single Markdown file
# ------------------------------------------------------------
def process_markdown(md_path):
    text = md_path.read_text(encoding="utf-8")
    original = text
    md_stem = md_path.stem
    counter = 1

    # --- Inline Markdown ---
    def repl_md_inline(match):
        nonlocal counter
        alt = match.group("alt")
        ext = match.group("ext")
        data = match.group("data")
        filename = save_image(data, ext, md_stem, counter)
        counter += 1
        return f"![{alt}](../images/{filename})"

    text = MD_INLINE.sub(repl_md_inline, text)

    # --- Inline HTML ---
    def repl_html(match):
        nonlocal counter
        ext = match.group("ext")
        data = match.group("data")
        filename = save_image(data, ext, md_stem, counter)
        counter += 1
        return f"![image](../images/{filename})"

    text = HTML_INLINE.sub(repl_html, text)

    # --- Reference-style ---
    def repl_reference(match):
        nonlocal counter
        ref = match.group("ref")
        ext = match.group("ext")
        data = match.group("data")
        filename = save_image(data, ext, md_stem, counter)
        counter += 1
        return f"[{ref}]: ../images/{filename}"

    text = MD_REFERENCE.sub(repl_reference, text)

    # Write back if changed
    if text != original:
        md_path.write_text(text, encoding="utf-8")
        print(f"Updated: {md_path}")
    else:
        print(f"No embedded images in: {md_path}")

# ------------------------------------------------------------
# Walk docs/ recursively
# ------------------------------------------------------------
def walk_docs():
    for md_file in ROOT.rglob("*.md"):
        process_markdown(md_file)

if __name__ == "__main__":
    walk_docs()
