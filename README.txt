CLOUD UPLOAD BUNDLE
===================
1600 styles: every style that used to be inside the mod (1186) plus 414 new ones from packs_1.zip.

  packs/       one zip per style, named <id>.zip   (all under the 95 MB limit)
  previews/    one 256x256 picture per style, named <id>.png (names under each texture)
  styles-to-add.json   the index.json entries (id, category, name, sha256, size, added, preview)
  merge_into_index.py  puts those entries into your repo's index.json

How to upload
  1. Extract all the cloud-upload zip parts into the same folder (merge when asked).
  2. In your cloud repo folder, copy in the packs/ and previews/ folders.
  3. python merge_into_index.py <your repo>/index.json     (keeps your existing styles)
  4. Commit and push. Players see the styles the next time they open the menu
     (GitHub can take up to 5 minutes to hand out the new list).

GitHub tip: 1600 files and about 680 MB is a lot for one push. If it fails, push packs/ in a few
batches (for example one category prefix at a time) and push index.json last.
