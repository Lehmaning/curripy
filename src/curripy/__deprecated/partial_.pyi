from functools import partial as partial_

partial = partial_
"""
Notice: this is not the true type of curripy.partial.
The reason for marking curripy.partial as a type alias to functools.partial is
it makes curripy.partial able to show real type of the function with support of mypy and lsp,
without any third-party mypy plugin.
"""
