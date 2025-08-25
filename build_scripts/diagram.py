#!/usr/bin/env python
"""Generate architecture diagram using matplotlib."""
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


def rbox(ax, xy, w, h, text, fontsize=9):
    x, y = xy
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03", linewidth=1.3)
    ax.add_patch(box)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize)


# figure
fig, ax = plt.subplots(figsize=(12, 8))
ax.axis("off")

# main boxes with detailed text
boxes = {
    "api": (
        (0.05, 0.78),
        0.28,
        0.18,
        "CDISC Library API\n"
        "\u2022 OAuth2 Bearer token\n"
        "\u2022 Accept: application/vnd.cdisc+json\n"
        "\u2022 Hypermedia links",
    ),
    "crawler": (
        (0.37, 0.78),
        0.28,
        0.22,
        "Crawler (build_canonical.py)\n"
        "\u2022 HATEOAS traversal\n"
        "\u2022 Pagination handling\n"
        "\u2022 CT caching & de-dup\n"
        "\u2022 JSON schema validate\n"
        "\u2022 Error retries/back-off",
    ),
    "canonical": (
        (0.69, 0.78),
        0.28,
        0.20,
        "Canonical store\ncrf.json (Git)\n"
        "\u2022 Versioning & tags\n"
        "\u2022 Schema-validated\n"
        "\u2022 Change diff reports",
    ),
    "build": (
        (0.37, 0.45),
        0.28,
        0.28,
        "Build script + Templates\n(build.py & Jinja/Pandoc)\n"
        "\u2022 Jinja \u2192 Markdown & LaTeX\n"
        "\u2022 Pandoc \u2192 DOCX/TeX\n"
        "\u2022 pandas/openpyxl \u2192 CSV/XLSX\n"
        "\u2022 odmlib \u2192 ODM-XML\n"
        "\u2022 FHIR export module",
    ),
    "outputs": (
        (0.69, 0.46),
        0.28,
        0.23,
        "Generated artefacts\n"
        "\u2022 form.md\n\u2022 form.docx\n\u2022 form.tex\n"
        "\u2022 form.csv / .xlsx\n\u2022 form.odm.xml\n\u2022 form.fhir.json",
    ),
    "ci": (
        (0.37, 0.12),
        0.28,
        0.18,
        "CI / GitHub Actions\n"
        "\u2022 On push trigger\n"
        "\u2022 Install deps\n"
        "\u2022 Run build.py\n"
        "\u2022 Upload artefacts",
    ),
}

# draw boxes
for key, (xy, w, h, text) in boxes.items():
    rbox(ax, xy, w, h, text)


def arrow(ax, start_key, end_key, vert_shift=0):
    sx, sy = boxes[start_key][0]
    sw, sh = boxes[start_key][1], boxes[start_key][2]
    ex, ey = boxes[end_key][0]
    _, eh = boxes[end_key][1], boxes[end_key][2]
    start = (sx + sw, sy + sh / 2 + vert_shift)
    end = (ex, ey + eh / 2 + vert_shift)
    ax.add_patch(
        FancyArrowPatch(start, end, arrowstyle="-|>", mutation_scale=18, linewidth=1.2)
    )


# top flow arrows
arrow(ax, "api", "crawler")
arrow(ax, "crawler", "canonical")
arrow(ax, "canonical", "outputs")

# canonical down to build
sx, sy = boxes["canonical"][0]
sw, sh = boxes["canonical"][1], boxes["canonical"][2]
bx, by = boxes["build"][0]
bw, bh = boxes["build"][1], boxes["build"][2]
ax.add_patch(
    FancyArrowPatch(
        (sx + sw / 2, sy),
        (bx + bw / 2, by + bh),
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=1.2,
    )
)

# build to outputs
arrow(ax, "build", "outputs")

# build down to CI
sx, sy = boxes["build"][0]
sw, sh = boxes["build"][1], boxes["build"][2]
cx, cy = boxes["ci"][0]
cw, ch = boxes["ci"][1], boxes["ci"][2]
ax.add_patch(
    FancyArrowPatch(
        (sx + sw / 2, sy),
        (cx + cw / 2, cy + ch),
        arrowstyle="-|>",
        mutation_scale=18,
        linewidth=1.2,
    )
)

plt.tight_layout()

if __name__ == "__main__":
    plt.show()
