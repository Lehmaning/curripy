# curripy

Curried and point-free versions of the Python standard libraries functions and methods.

## Features

* A set of efficient functions corresponing to the built-in and standard Python functions
* Point-free style of functions and methods for better composition
* All implementations are encapsulations of upstream library

<!-- 
## Installation

 ```shell
pip install curripy
``` -->

## Build

```shell
git clone https://github.com/Lehmaning/curripy.git
cd curripy
rye sync
rye build
```

Then check the build results in directory ```dist```, then install ```curripy``` from them.

## Dependencies

* [dry-python/returns](https://github.com/dry-python/returns): Provides support for currying, pipes (composing) and Functors
* [dry-python/classes](https://github.com/dry-python/classes): Brings support for typeclasses
* [dgilland/pydash](https://github.com/dgilland/pydash): Adds support for currying, composing, arity and curry_right
