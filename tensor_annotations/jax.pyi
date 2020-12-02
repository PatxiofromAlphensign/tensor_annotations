"""Type stubs for custom JAX tensor classes.

NOTE: This file is generated from templates/jax_tensors.pyi.

To regenerate, run the following from the tensor_annotations directory:
   tools/render_tensor_template.py \
     --template templates/jax_tensors.pyi \
     --out jax.pyi
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


# A quick refresher on broadcasting rules:
# 1. Array[A, B] + scalar = Array[A, B].
# 2. Otherwise, start with trailing dimension of each tensor and work
#    forwards. Broadcasting is possible if, for each axis, the dimensions
#    of that axis in each tensor are either a) equal or b) one of them is 1.
# We deliberately ignore case b) for the time being since we don't support
# literal shapes yet.

class Array0:
  def __getitem__(self, index) -> Any: ...

  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators

  def __abs__(self) -> Array0: ...

  def __neg__(self) -> Array0: ...

  def __pos__(self) -> Array0: ...

  # END: Unary operators

  # BEGIN: Binary element-wise operators

  @overload
  def __add__(self, other: Array0) -> Array0: ...

  @overload
  def __add__(self, other: Array1) -> Array1: ...

  @overload
  def __add__(self, other: Array2) -> Array2: ...

  @overload
  def __add__(self, other: Array3) -> Array3: ...

  @overload
  def __add__(self, other: Array4) -> Array4: ...

  @overload
  def __sub__(self, other: Array0) -> Array0: ...

  @overload
  def __sub__(self, other: Array1) -> Array1: ...

  @overload
  def __sub__(self, other: Array2) -> Array2: ...

  @overload
  def __sub__(self, other: Array3) -> Array3: ...

  @overload
  def __sub__(self, other: Array4) -> Array4: ...

  @overload
  def __floordiv__(self, other: Array0) -> Array0: ...

  @overload
  def __floordiv__(self, other: Array1) -> Array1: ...

  @overload
  def __floordiv__(self, other: Array2) -> Array2: ...

  @overload
  def __floordiv__(self, other: Array3) -> Array3: ...

  @overload
  def __floordiv__(self, other: Array4) -> Array4: ...

  @overload
  def __truediv__(self, other: Array0) -> Array0: ...

  @overload
  def __truediv__(self, other: Array1) -> Array1: ...

  @overload
  def __truediv__(self, other: Array2) -> Array2: ...

  @overload
  def __truediv__(self, other: Array3) -> Array3: ...

  @overload
  def __truediv__(self, other: Array4) -> Array4: ...

  @overload
  def __pow__(self, other: Array0) -> Array0: ...

  @overload
  def __pow__(self, other: Array1) -> Array1: ...

  @overload
  def __pow__(self, other: Array2) -> Array2: ...

  @overload
  def __pow__(self, other: Array3) -> Array3: ...

  @overload
  def __pow__(self, other: Array4) -> Array4: ...

  @overload
  def __lt__(self, other: Array0) -> Array0: ...

  @overload
  def __lt__(self, other: Array1) -> Array1: ...

  @overload
  def __lt__(self, other: Array2) -> Array2: ...

  @overload
  def __lt__(self, other: Array3) -> Array3: ...

  @overload
  def __lt__(self, other: Array4) -> Array4: ...

  @overload
  def __le__(self, other: Array0) -> Array0: ...

  @overload
  def __le__(self, other: Array1) -> Array1: ...

  @overload
  def __le__(self, other: Array2) -> Array2: ...

  @overload
  def __le__(self, other: Array3) -> Array3: ...

  @overload
  def __le__(self, other: Array4) -> Array4: ...

  @overload
  def __ge__(self, other: Array0) -> Array0: ...

  @overload
  def __ge__(self, other: Array1) -> Array1: ...

  @overload
  def __ge__(self, other: Array2) -> Array2: ...

  @overload
  def __ge__(self, other: Array3) -> Array3: ...

  @overload
  def __ge__(self, other: Array4) -> Array4: ...

  @overload
  def __gt__(self, other: Array0) -> Array0: ...

  @overload
  def __gt__(self, other: Array1) -> Array1: ...

  @overload
  def __gt__(self, other: Array2) -> Array2: ...

  @overload
  def __gt__(self, other: Array3) -> Array3: ...

  @overload
  def __gt__(self, other: Array4) -> Array4: ...

  @overload
  def __mul__(self, other: Array0) -> Array0: ...

  @overload
  def __mul__(self, other: Array1) -> Array1: ...

  @overload
  def __mul__(self, other: Array2) -> Array2: ...

  @overload
  def __mul__(self, other: Array3) -> Array3: ...

  @overload
  def __mul__(self, other: Array4) -> Array4: ...

  @overload
  def __rmul__(self, other: Array0) -> Array0: ...

  @overload
  def __rmul__(self, other: Array1) -> Array1: ...

  @overload
  def __rmul__(self, other: Array2) -> Array2: ...

  @overload
  def __rmul__(self, other: Array3) -> Array3: ...

  @overload
  def __rmul__(self, other: Array4) -> Array4: ...

  # END: Binary element-wise operators


class Array1(Generic[A1]):
  def __getitem__(self, index) -> Any: ...

  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators

  def __abs__(self) -> Array1[A1]: ...

  def __neg__(self) -> Array1[A1]: ...

  def __pos__(self) -> Array1[A1]: ...

  # END: Unary operators

  # BEGIN: Binary element-wise operators

  # Broadcasting case 1: Array[A, B] + scalar = Array[A, B].

  @overload
  def __add__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __add__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __sub__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __sub__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __floordiv__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __floordiv__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __truediv__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __truediv__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __pow__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __pow__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __lt__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __lt__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __le__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __le__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __ge__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __ge__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __gt__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __gt__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __mul__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __mul__(self, other: Array0) -> Array1[A1]: ...

  @overload
  def __rmul__(self, other: Number) -> Array1[A1]: ...

  @overload
  def __rmul__(self, other: Array0) -> Array1[A1]: ...

  # Broadcasting case 2: Array[A, B, C] + Array[B, C] = Array[A, B, C].

  @overload
  def __add__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __sub__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __floordiv__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __truediv__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __pow__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __lt__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __le__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __ge__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __gt__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __mul__(self, other: Array1[A1]) -> Array1[A1]: ...

  @overload
  def __rmul__(self, other: Array1[A1]) -> Array1[A1]: ...

  # END: Binary element-wise operators


class Array2(Generic[A1, A2]):
  def __getitem__(self, index) -> Any: ...

  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators

  def __abs__(self) -> Array2[A1, A2]: ...

  def __neg__(self) -> Array2[A1, A2]: ...

  def __pos__(self) -> Array2[A1, A2]: ...

  # END: Unary operators

  # BEGIN: Binary element-wise operators

  # Broadcasting case 1: Array[A, B] + scalar = Array[A, B].

  @overload
  def __add__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __add__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __sub__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __sub__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __floordiv__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __floordiv__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __truediv__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __truediv__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __pow__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __pow__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __lt__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __lt__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __le__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __le__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __ge__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __ge__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __gt__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __gt__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __mul__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __mul__(self, other: Array0) -> Array2[A1, A2]: ...

  @overload
  def __rmul__(self, other: Number) -> Array2[A1, A2]: ...

  @overload
  def __rmul__(self, other: Array0) -> Array2[A1, A2]: ...

  # Broadcasting case 2: Array[A, B, C] + Array[B, C] = Array[A, B, C].

  @overload
  def __add__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __add__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __sub__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __sub__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __floordiv__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __floordiv__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __truediv__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __truediv__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __pow__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __pow__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __lt__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __lt__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __le__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __le__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __ge__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __ge__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __gt__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __gt__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __mul__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __mul__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  @overload
  def __rmul__(self, other: Array1[A2]) -> Array2[A1, A2]: ...

  @overload
  def __rmul__(self, other: Array2[A1, A2]) -> Array2[A1, A2]: ...

  # END: Binary element-wise operators


class Array3(Generic[A1, A2, A3]):
  def __getitem__(self, index) -> Any: ...

  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators

  def __abs__(self) -> Array3[A1, A2, A3]: ...

  def __neg__(self) -> Array3[A1, A2, A3]: ...

  def __pos__(self) -> Array3[A1, A2, A3]: ...

  # END: Unary operators

  # BEGIN: Binary element-wise operators

  # Broadcasting case 1: Array[A, B] + scalar = Array[A, B].

  @overload
  def __add__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __add__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __sub__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __sub__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __floordiv__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __floordiv__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __truediv__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __truediv__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __pow__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __pow__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __lt__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __lt__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __le__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __le__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __ge__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __ge__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __gt__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __gt__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __mul__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __mul__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  @overload
  def __rmul__(self, other: Number) -> Array3[A1, A2, A3]: ...

  @overload
  def __rmul__(self, other: Array0) -> Array3[A1, A2, A3]: ...

  # Broadcasting case 2: Array[A, B, C] + Array[B, C] = Array[A, B, C].

  @overload
  def __add__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __add__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __add__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __sub__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __sub__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __sub__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __floordiv__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __floordiv__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __floordiv__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __truediv__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __truediv__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __truediv__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __pow__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __pow__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __pow__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __lt__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __lt__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __lt__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __le__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __le__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __le__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __ge__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __ge__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __ge__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __gt__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __gt__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __gt__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __mul__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __mul__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __mul__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __rmul__(self, other: Array1[A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __rmul__(self, other: Array2[A2, A3]) -> Array3[A1, A2, A3]: ...

  @overload
  def __rmul__(self, other: Array3[A1, A2, A3]) -> Array3[A1, A2, A3]: ...

  # END: Binary element-wise operators


class Array4(Generic[A1, A2, A3, A4]):
  def __getitem__(self, index) -> Any: ...

  def __setitem__(self, index, value) -> Any: ...

  # BEGIN: Unary operators

  def __abs__(self) -> Array4[A1, A2, A3, A4]: ...

  def __neg__(self) -> Array4[A1, A2, A3, A4]: ...

  def __pos__(self) -> Array4[A1, A2, A3, A4]: ...

  # END: Unary operators

  # BEGIN: Binary element-wise operators

  # Broadcasting case 1: Array[A, B] + scalar = Array[A, B].

  @overload
  def __add__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __add__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __sub__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __sub__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __floordiv__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __floordiv__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __truediv__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __truediv__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __pow__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __pow__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __lt__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __lt__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __le__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __le__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __ge__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __ge__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __gt__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __gt__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __mul__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __mul__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __rmul__(self, other: Number) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __rmul__(self, other: Array0) -> Array4[A1, A2, A3, A4]: ...

  # Broadcasting case 2: Array[A, B, C] + Array[B, C] = Array[A, B, C].

  @overload
  def __add__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __add__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __add__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __add__(self, other: Array4[A1, A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  @overload
  def __sub__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __sub__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __sub__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __sub__(self, other: Array4[A1, A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  @overload
  def __floordiv__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __floordiv__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __floordiv__(self, other: Array3[A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  @overload
  def __floordiv__(self, other: Array4[A1, A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  @overload
  def __truediv__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __truediv__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __truediv__(self, other: Array3[A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  @overload
  def __truediv__(self, other: Array4[A1, A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  @overload
  def __pow__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __pow__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __pow__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __pow__(self, other: Array4[A1, A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  @overload
  def __lt__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __lt__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __lt__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __lt__(self, other: Array4[A1, A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __le__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __le__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __le__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __le__(self, other: Array4[A1, A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __ge__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __ge__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __ge__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __ge__(self, other: Array4[A1, A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __gt__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __gt__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __gt__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __gt__(self, other: Array4[A1, A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __mul__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __mul__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __mul__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __mul__(self, other: Array4[A1, A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  @overload
  def __rmul__(self, other: Array1[A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __rmul__(self, other: Array2[A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __rmul__(self, other: Array3[A2, A3, A4]) -> Array4[A1, A2, A3, A4]: ...

  @overload
  def __rmul__(self, other: Array4[A1, A2, A3, A4]) -> Array4[
    A1, A2, A3, A4]: ...

  # END: Binary element-wise operators
