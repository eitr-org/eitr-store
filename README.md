# Eitr Store

Eitr Store is the index for the Eitr desktop's themes, plugins and wallpaper
packs. The app combines official and community discoveries in one window.
Lockscreens use Eitr's signed package repository and are not listed here.

## Submit an item

Fork this repository and add an entry to the matching list in `index.json`.
Read [CONTRIBUTING.md](CONTRIBUTING.md), run `python3 validate.py`, and open a
pull request. Submissions are reviewed before publication. An `official: true`
flag is reserved for items maintained by Eitr; it never grants plugin permissions.

Each entry supplies `id`, `repository` (HTTPS or SSH Git URL), `folder`,
`maintainer`, `license` (SPDX identifier) and `description` (up to 72 characters).
Plugins also require `commit`, the full reviewed commit SHA.

Schema 2 contains `themes`, `plugins`, `wallpapers`, and `removed` lists.
`removed` entries contain `kind`, `id`, and `reason` and cannot also be listed.
The desktop also reads schema 1 during migration.

The validator vendors the desktop's validation modules without modifications.
The desktop's Store tests compare these files byte for byte. Run it offline;
CI validates metadata and does not execute submitted content.

The vendored desktop modules keep their own license in `vendor/LICENSE`.
