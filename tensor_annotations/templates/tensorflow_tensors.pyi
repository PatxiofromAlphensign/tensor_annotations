# LINT.IfChange
"""Type stubs for custom TensorFlow tensor classes.

NOTE: This file is generated from templates/tensorflow_tensors.pyi.

To regenerate, run the following from the tensor_annotations directory:
   tools/render_tensor_template.py \
     --template templates/tensorflow_tensors.pyi \
     --out tensorflow.pyi
"""

from typing import Any, TypeVar, Tuple, Sequence, Generic, overload, Union

from tensor_annotations.axes import Axis


Shape = Sequence[int]
Shape1 = Tuple[int]
Shape2 = Tuple[int, int]
Shape3 = Tuple[int, int, int]
Shape4 = Tuple[int, int, int, int]

A1 = TypeVar('A1', bound=Axis)
A2 = TypeVar('A2', bound=Axis)
A3 = TypeVar('A3', bound=Axis)
A4 = TypeVar('A4', bound=Axis)

Number = Union[int, float]

{% set unary_funcs = ['__abs__', '__neg__', '__pos__'] %}
{# Yes, __mul__ _is_ elementwise! __matmul__ is matrix multiply. #}
{% set binary_elementwise_funcs = ['__add__', '__sub__', '__floordiv__',
                                   '__truediv__', '__pow__', '__lt__', '__le__',
                                   '__ge__', '__gt__', '__mul__', '__rmul__'] %}


# A quick refresher on broadcasting rules:
# 1. Tensor[A, B] + scalar = Tensor[A, B]
# 2. Otherwise, start with trailing dimension of each tensor and work
#    forwards. Broadcasting is possible if, for each axis, the dimensions
#    of that axis in each tensor are either a) equal or b) one of them is 1.
# We deliberately ignore case b) for the time being since we don't support
# literal shapes yet.

class Tensor0:
  def __getitem__(self, index) -> Any: ...
  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators
  {% for func in unary_funcs %}
  def {{ func }}(self) -> Tensor0: ...
  {% endfor %}
  # END: Unary operators

  # BEGIN: Binary element-wise operators
  {% for func in binary_elementwise_funcs %}
  @overload
  def {{ func }}(self, other: Tensor0) -> Tensor0: ...
  @overload
  def {{ func }}(self, other: Tensor1) -> Tensor1: ...
  @overload
  def {{ func }}(self, other: Tensor2) -> Tensor2: ...
  @overload
  def {{ func }}(self, other: Tensor3) -> Tensor3: ...
  @overload
  def {{ func }}(self, other: Tensor4) -> Tensor4: ...
  {% endfor %}
  # END: Binary element-wise operators


class Tensor1(Generic[A1]):
  def __getitem__(self, index) -> Any: ...
  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators
  {% for func in unary_funcs %}
  def {{ func }}(self) -> Tensor1[A1]: ...
  {% endfor %}
  # END: Unary operators

  # BEGIN: Binary element-wise operators

  {% for func in binary_elementwise_funcs %}

  {# Broadcasting case 1: Broadcasting with scalars #}
  @overload
  def {{ func }}(self, other: Number) -> Tensor1[A1]: ...
  @overload
  def {{ func }}(self, other: Tensor0) -> Tensor1[A1]: ...

  {# No broadcast #}
  @overload
  def {{ func }}(self, other: Tensor1[A1]) -> Tensor1[A1]: ...

  {% endfor %}

  # END: Binary element-wise operators


class Tensor2(Generic[A1, A2]):
  def __getitem__(self, index) -> Any: ...
  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators
  {% for func in unary_funcs %}
  def {{ func }}(self) -> Tensor2[A1, A2]: ...
  {% endfor %}
  # END: Unary operators

  # BEGIN: Binary element-wise operators

  {% for func in binary_elementwise_funcs %}

  {# Broadcasting case 1: Broadcasting with scalars #}
  @overload
  def {{ func }}(self, other: Number) -> Tensor2[A1, A2]: ...
  @overload
  def {{ func }}(self, other: Tensor0) -> Tensor2[A1, A2]: ...

  {# Broadcasting case 2: Broadcasting with a lesser rank #}
  @overload
  def {{ func }}(self, other: Tensor1[A2]) -> Tensor2[A1, A2]: ...

  {# No broadcast #}
  @overload
  def {{ func }}(self, other: Tensor2[A1, A2]) -> Tensor2[A1, A2]: ...

  {% endfor %}

  # END: Binary element-wise operators


class Tensor3(Generic[A1, A2, A3]):
  def __getitem__(self, index) -> Any: ...
  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators
  {% for func in unary_funcs %}
  def {{ func }}(self) -> Tensor3[A1, A2, A3]: ...
  {% endfor %}
  # END: Unary operators

  # BEGIN: Binary element-wise operators

  {% for func in binary_elementwise_funcs %}

  {# Broadcasting case 1: Broadcasting with scalars #}
  @overload
  def {{ func }}(self, other: Number) -> Tensor3[A1, A2, A3]: ...
  @overload
  def {{ func }}(self, other: Tensor0) -> Tensor3[A1, A2, A3]: ...

  {# Broadcasting case 2: Broadcasting with a lesser rank #}
  @overload
  def {{ func }}(self, other: Tensor1[A3]) -> Tensor3[A1, A2, A3]: ...
  @overload
  def {{ func }}(self, other: Tensor2[A2, A3]) -> Tensor3[A1, A2, A3]: ...

  {# No broadcast #}
  @overload
  def {{ func }}(self, other: Tensor3[A1, A2, A3]) -> Tensor3[A1, A2, A3]: ...

  {% endfor %}

  # END: Binary element-wise operators


class Tensor4(Generic[A1, A2, A3, A4]):
  def __getitem__(self, index) -> Any: ...
  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators
  {% for func in unary_funcs %}
  def {{ func }}(self) -> Tensor4[A1, A2, A3, A4]: ...
  {% endfor %}
  # END: Unary operators

  # BEGIN: Binary element-wise operators

  {% for func in binary_elementwise_funcs %}

  {# Broadcasting case 1: Broadcasting with scalars #}
  @overload
  def {{ func }}(self, other: Number) -> Tensor4[A1, A2, A3, A4]: ...
  @overload
  def {{ func }}(self, other: Tensor0) -> Tensor4[A1, A2, A3, A4]: ...

  {# Broadcasting case 2: Broadcasting with a lesser rank #}
  @overload
  def {{ func }}(self, other: Tensor1[A4]) -> Tensor4[A1, A2, A3, A4]: ...
  @overload
  def {{ func }}(self, other: Tensor2[A3, A4]) -> Tensor4[A1, A2, A3, A4]: ...
  @overload
  def {{ func }}(self, other: Tensor3[A2, A3, A4]) -> Tensor4[A1, A2, A3, A4]: ...

  {# No broadcast #}
  @overload
  def {{ func }}(self, other: Tensor4[A1, A2, A3, A4]) -> Tensor4[A1, A2, A3, A4]: ...

  {% endfor %}

  # END: Binary element-wise operators

# LINT.ThenChange(../tensorflow.pyi)
