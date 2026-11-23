# Eitr Store

Eitr Store is the index for the Eitr desktop's themes, plugins and wallpaper
packs. The app combines official and community discoveries in one window.
Lockscreens use Eitr's signed package repository and are not listed here.

## What can be listed

Every item lives in its author's own repository; this index only points to it. Fan
content is welcome: themes and wallpapers with art from games, films, anime and other
work you love, shared free for personal desktops.

- You host it and answer for it. Use an SPDX license ID, or `LicenseRef-` and a short
  name (for example `LicenseRef-Fan-Content`) for art that belongs to someone else, and
  say in your README who owns it.
- Nothing that pretends to be official, no paid or ripped assets, nothing illegal or
  adult.

## Removal requests

If you hold rights to something listed here and want it removed, open an issue in this
repository naming the entry. We remove it from the index; the files stay in their
author's repository, so contact the author too.

## Submit an item

Fork this repository and add an entry to the matching list in `index.json`.
Read [CONTRIBUTING.md](CONTRIBUTING.md), run `python3 validate.py`, and open a
pull request. Submissions are reviewed before publication. An `official: true`
flag is reserved for items maintained by Eitr; it never grants plugin permissions.

Each entry supplies `id`, `repository` (HTTPS or SSH Git URL), `folder`,
`maintainer`, `license` (SPDX identifier or `LicenseRef-` name) and `description` (up to 72 characters).
Plugins also require `commit`, the full reviewed commit SHA.

Schema 2 contains `themes`, `plugins`, `wallpapers`, and `removed` lists.
`removed` entries contain `kind`, `id`, and `reason` and cannot also be listed.
The desktop also reads schema 1 during migration.

The validator vendors the desktop's validation modules without modifications.
The desktop's Store tests compare these files byte for byte. Run it offline;
CI validates metadata and does not execute submitted content.

The vendored desktop modules keep their own license in `vendor/LICENSE`.
