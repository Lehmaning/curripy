# Conventions

## Dependency chain

The convention of package importing is as follows：

``_overlays`` -> ``_bootstrap`` -> ``utils`` -> ``<name_of_other_modules>``

Packages at right should not be imported by left ones, otherwise it may cause circular importing errors.
