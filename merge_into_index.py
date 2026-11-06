"""
Adds the styles in styles-to-add.json to your cloud repo's index.json (existing styles stay, a style
with the same id is replaced). Run it once, then copy packs/ and previews/ into the repo and push.

    python merge_into_index.py <path to the repo's index.json>
    python merge_into_index.py            (looks for ../index.json next to this folder)
"""
import json, os, sys

here = os.path.dirname(os.path.abspath(__file__))
target = sys.argv[1] if len(sys.argv) > 1 else os.path.join(here, "index.json")
if not os.path.isfile(target):
    # a fresh repo: start a new index
    index = {"version": 1, "styles": []}
else:
    with open(target, encoding="utf-8") as f:
        index = json.load(f)
index.setdefault("styles", [])
new = json.load(open(os.path.join(here, "styles-to-add.json"), encoding="utf-8"))["styles"]
ids = {s["id"] for s in new}
kept = [s for s in index["styles"] if s.get("id") not in ids]
index["styles"] = kept + new
with open(target, "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)
    f.write("\n")
print(f"{len(new)} styles added or replaced, {len(kept)} others kept -> {target}")
