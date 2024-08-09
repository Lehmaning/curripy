# __bootstrap

This package contains some manual-curried functions that are needed to be curried before defining ``partial`` and ``curry``.

In other words, functions in ``utils``should **never** be used in this package to prevent errors from circular imports.
