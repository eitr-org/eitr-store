# Contributing

Host your item in your own repository and follow the content rules in the README:
fan content is welcome when its owner is credited and its license is `LicenseRef-` plus
a short name; your own work uses a valid SPDX license identifier. Identify the
maintainer and explain changes in your pull request.
Keep descriptions factual, short, and free of instructions to reviewers.

Themes and wallpaper packs are data only: no scripts, executable files,
symlinks, submodules, install hooks or external dependencies. Eitr validates
all regular blobs, file counts, aggregate bytes and decoded images before
installation. Themes follow the Eitr theme package schema. Wallpaper packs
contain `eitr-wallpapers.json` with `id`, `name`, `description`, and an `images`
list of unique flat JPEG, PNG or WebP filenames, plus only those images.
Limits are the desktop's theme MAX_FILES and MAX_BYTES and image decoder limits.

Plugins run as the user. Pin the complete reviewed commit SHA, disclose system
packages and capabilities, and include reproducible source. A new commit needs
a new review; the desktop also requires permission review before installation
or update. The official badge never replaces this review.

Reviewers check provenance, licensing, metadata, content safety and ownership.
CI checks metadata only; inspect data and plugin sources separately without
running untrusted commands. Do not use pull_request_target for submitted code.

To remove an item, delete its listing and add its kind, ID and a public reason
to `removed`. Do not publish private reports or personal data. Removal from the
index prevents new discovery; it does not delete files on installed desktops.
