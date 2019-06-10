import builtins as _mod_builtins
import numpy as _mod_numpy
import scipy.sparse.csc as _mod_scipy_sparse_csc
import scipy.sparse.csr as _mod_scipy_sparse_csr

class dtype(_mod_builtins.object):
    'dtype(obj, align=False, copy=False)\n\n    Create a data type object.\n\n    A numpy array is homogeneous, and contains elements described by a\n    dtype object. A dtype object can be constructed from different\n    combinations of fundamental numeric types.\n\n    Parameters\n    ----------\n    obj\n        Object to be converted to a data type object.\n    align : bool, optional\n        Add padding to the fields to match what a C compiler would output\n        for a similar C-struct. Can be ``True`` only if `obj` is a dictionary\n        or a comma-separated string. If a struct dtype is being created,\n        this also sets a sticky alignment flag ``isalignedstruct``.\n    copy : bool, optional\n        Make a new copy of the data-type object. If ``False``, the result\n        may just be a reference to a built-in data-type object.\n\n    See also\n    --------\n    result_type\n\n    Examples\n    --------\n    Using array-scalar type:\n\n    >>> np.dtype(np.int16)\n    dtype(\'int16\')\n\n    Structured type, one field name \'f1\', containing int16:\n\n    >>> np.dtype([(\'f1\', np.int16)])\n    dtype([(\'f1\', \'<i2\')])\n\n    Structured type, one field named \'f1\', in itself containing a structured\n    type with one field:\n\n    >>> np.dtype([(\'f1\', [(\'f1\', np.int16)])])\n    dtype([(\'f1\', [(\'f1\', \'<i2\')])])\n\n    Structured type, two fields: the first field contains an unsigned int, the\n    second an int32:\n\n    >>> np.dtype([(\'f1\', np.uint), (\'f2\', np.int32)])\n    dtype([(\'f1\', \'<u4\'), (\'f2\', \'<i4\')])\n\n    Using array-protocol type strings:\n\n    >>> np.dtype([(\'a\',\'f8\'),(\'b\',\'S10\')])\n    dtype([(\'a\', \'<f8\'), (\'b\', \'|S10\')])\n\n    Using comma-separated field formats.  The shape is (2,3):\n\n    >>> np.dtype("i4, (2,3)f8")\n    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\', (2, 3))])\n\n    Using tuples.  ``int`` is a fixed type, 3 the field\'s shape.  ``void``\n    is a flexible type, here of size 10:\n\n    >>> np.dtype([(\'hello\',(int,3)),(\'world\',np.void,10)])\n    dtype([(\'hello\', \'<i4\', 3), (\'world\', \'|V10\')])\n\n    Subdivide ``int16`` into 2 ``int8``\'s, called x and y.  0 and 1 are\n    the offsets in bytes:\n\n    >>> np.dtype((np.int16, {\'x\':(np.int8,0), \'y\':(np.int8,1)}))\n    dtype((\'<i2\', [(\'x\', \'|i1\'), (\'y\', \'|i1\')]))\n\n    Using dictionaries.  Two fields named \'gender\' and \'age\':\n\n    >>> np.dtype({\'names\':[\'gender\',\'age\'], \'formats\':[\'S1\',np.uint8]})\n    dtype([(\'gender\', \'|S1\'), (\'age\', \'|u1\')])\n\n    Offsets in bytes, here 0 and 25:\n\n    >>> np.dtype({\'surname\':(\'S25\',0),\'age\':(np.uint8,25)})\n    dtype([(\'surname\', \'|S25\'), (\'age\', \'|u1\')])'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = dtype
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, obj, align=False, copy=False):
        'dtype(obj, align=False, copy=False)\n\n    Create a data type object.\n\n    A numpy array is homogeneous, and contains elements described by a\n    dtype object. A dtype object can be constructed from different\n    combinations of fundamental numeric types.\n\n    Parameters\n    ----------\n    obj\n        Object to be converted to a data type object.\n    align : bool, optional\n        Add padding to the fields to match what a C compiler would output\n        for a similar C-struct. Can be ``True`` only if `obj` is a dictionary\n        or a comma-separated string. If a struct dtype is being created,\n        this also sets a sticky alignment flag ``isalignedstruct``.\n    copy : bool, optional\n        Make a new copy of the data-type object. If ``False``, the result\n        may just be a reference to a built-in data-type object.\n\n    See also\n    --------\n    result_type\n\n    Examples\n    --------\n    Using array-scalar type:\n\n    >>> np.dtype(np.int16)\n    dtype(\'int16\')\n\n    Structured type, one field name \'f1\', containing int16:\n\n    >>> np.dtype([(\'f1\', np.int16)])\n    dtype([(\'f1\', \'<i2\')])\n\n    Structured type, one field named \'f1\', in itself containing a structured\n    type with one field:\n\n    >>> np.dtype([(\'f1\', [(\'f1\', np.int16)])])\n    dtype([(\'f1\', [(\'f1\', \'<i2\')])])\n\n    Structured type, two fields: the first field contains an unsigned int, the\n    second an int32:\n\n    >>> np.dtype([(\'f1\', np.uint), (\'f2\', np.int32)])\n    dtype([(\'f1\', \'<u4\'), (\'f2\', \'<i4\')])\n\n    Using array-protocol type strings:\n\n    >>> np.dtype([(\'a\',\'f8\'),(\'b\',\'S10\')])\n    dtype([(\'a\', \'<f8\'), (\'b\', \'|S10\')])\n\n    Using comma-separated field formats.  The shape is (2,3):\n\n    >>> np.dtype("i4, (2,3)f8")\n    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\', (2, 3))])\n\n    Using tuples.  ``int`` is a fixed type, 3 the field\'s shape.  ``void``\n    is a flexible type, here of size 10:\n\n    >>> np.dtype([(\'hello\',(int,3)),(\'world\',np.void,10)])\n    dtype([(\'hello\', \'<i4\', 3), (\'world\', \'|V10\')])\n\n    Subdivide ``int16`` into 2 ``int8``\'s, called x and y.  0 and 1 are\n    the offsets in bytes:\n\n    >>> np.dtype((np.int16, {\'x\':(np.int8,0), \'y\':(np.int8,1)}))\n    dtype((\'<i2\', [(\'x\', \'|i1\'), (\'y\', \'|i1\')]))\n\n    Using dictionaries.  Two fields named \'gender\' and \'age\':\n\n    >>> np.dtype({\'names\':[\'gender\',\'age\'], \'formats\':[\'S1\',np.uint8]})\n    dtype([(\'gender\', \'|S1\'), (\'age\', \'|u1\')])\n\n    Offsets in bytes, here 0 and 25:\n\n    >>> np.dtype({\'surname\':(\'S25\',0),\'age\':(np.uint8,25)})\n    dtype([(\'surname\', \'|S25\'), (\'age\', \'|u1\')])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    def __mul__(self, value):
        'Return self*value.'
        return dtype()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return dtype()
    
    def __setstate__(self, state):
        return None
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def alignment(self):
        'The required alignment (bytes) of this data-type according to the compiler.\n\n    More information is available in the C-API section of the manual.'
        pass
    
    @property
    def base(self):
        pass
    
    @property
    def byteorder(self):
        "A character indicating the byte-order of this data-type object.\n\n    One of:\n\n    ===  ==============\n    '='  native\n    '<'  little-endian\n    '>'  big-endian\n    '|'  not applicable\n    ===  ==============\n\n    All built-in data-type objects have byteorder either '=' or '|'.\n\n    Examples\n    --------\n\n    >>> dt = np.dtype('i2')\n    >>> dt.byteorder\n    '='\n    >>> # endian is not relevant for 8 bit numbers\n    >>> np.dtype('i1').byteorder\n    '|'\n    >>> # or ASCII strings\n    >>> np.dtype('S2').byteorder\n    '|'\n    >>> # Even if specific code is given, and it is native\n    >>> # '=' is the byteorder\n    >>> import sys\n    >>> sys_is_le = sys.byteorder == 'little'\n    >>> native_code = sys_is_le and '<' or '>'\n    >>> swapped_code = sys_is_le and '>' or '<'\n    >>> dt = np.dtype(native_code + 'i2')\n    >>> dt.byteorder\n    '='\n    >>> # Swapped code shows up as itself\n    >>> dt = np.dtype(swapped_code + 'i2')\n    >>> dt.byteorder == swapped_code\n    True"
        pass
    
    @property
    def char(self):
        'A unique character code for each of the 21 different built-in types.'
        pass
    
    @property
    def descr(self):
        "`__array_interface__` description of the data-type.\n\n    The format is that required by the 'descr' key in the\n    `__array_interface__` attribute.\n\n    Warning: This attribute exists specifically for `__array_interface__`,\n    and is not a datatype description compatible with `np.dtype`."
        pass
    
    @property
    def fields(self):
        "Dictionary of named fields defined for this data type, or ``None``.\n\n    The dictionary is indexed by keys that are the names of the fields.\n    Each entry in the dictionary is a tuple fully describing the field::\n\n      (dtype, offset[, title])\n\n    Offset is limited to C int, which is signed and usually 32 bits.\n    If present, the optional title can be any object (if it is a string\n    or unicode then it will also be a key in the fields dictionary,\n    otherwise it's meta-data). Notice also that the first two elements\n    of the tuple can be passed directly as arguments to the ``ndarray.getfield``\n    and ``ndarray.setfield`` methods.\n\n    See Also\n    --------\n    ndarray.getfield, ndarray.setfield\n\n    Examples\n    --------\n    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n    >>> print(dt.fields)\n    {'grades': (dtype(('float64',(2,))), 16), 'name': (dtype('|S16'), 0)}"
        pass
    
    @property
    def flags(self):
        'Bit-flags describing how this data type is to be interpreted.\n\n    Bit-masks are in `numpy.core.multiarray` as the constants\n    `ITEM_HASOBJECT`, `LIST_PICKLE`, `ITEM_IS_POINTER`, `NEEDS_INIT`,\n    `NEEDS_PYAPI`, `USE_GETITEM`, `USE_SETITEM`. A full explanation\n    of these flags is in C-API documentation; they are largely useful\n    for user-defined data-types.'
        pass
    
    @property
    def hasobject(self):
        "Boolean indicating whether this dtype contains any reference-counted\n    objects in any fields or sub-dtypes.\n\n    Recall that what is actually in the ndarray memory representing\n    the Python object is the memory address of that object (a pointer).\n    Special handling may be required, and this attribute is useful for\n    distinguishing data types that may contain arbitrary Python objects\n    and data-types that won't."
        pass
    
    @property
    def isalignedstruct(self):
        'Boolean indicating whether the dtype is a struct which maintains\n    field alignment. This flag is sticky, so when combining multiple\n    structs together, it is preserved and produces new dtypes which\n    are also aligned.'
        pass
    
    @property
    def isbuiltin(self):
        "Integer indicating how this dtype relates to the built-in dtypes.\n\n    Read-only.\n\n    =  ========================================================================\n    0  if this is a structured array type, with fields\n    1  if this is a dtype compiled into numpy (such as ints, floats etc)\n    2  if the dtype is for a user-defined numpy type\n       A user-defined type uses the numpy C-API machinery to extend\n       numpy to handle a new array type. See\n       :ref:`user.user-defined-data-types` in the NumPy manual.\n    =  ========================================================================\n\n    Examples\n    --------\n    >>> dt = np.dtype('i2')\n    >>> dt.isbuiltin\n    1\n    >>> dt = np.dtype('f8')\n    >>> dt.isbuiltin\n    1\n    >>> dt = np.dtype([('field1', 'f8')])\n    >>> dt.isbuiltin\n    0"
        pass
    
    @property
    def isnative(self):
        'Boolean indicating whether the byte order of this dtype is native\n    to the platform.'
        pass
    
    @property
    def itemsize(self):
        'The element size of this data-type object.\n\n    For 18 of the 21 types this number is fixed by the data-type.\n    For the flexible data-types, this number can be anything.'
        pass
    
    @property
    def kind(self):
        "A character code (one of 'biufcmMOSUV') identifying the general kind of data.\n\n    =  ======================\n    b  boolean\n    i  signed integer\n    u  unsigned integer\n    f  floating-point\n    c  complex floating-point\n    m  timedelta\n    M  datetime\n    O  object\n    S  (byte-)string\n    U  Unicode\n    V  void\n    =  ======================"
        pass
    
    @property
    def metadata(self):
        pass
    
    @property
    def name(self):
        'A bit-width name for this data-type.\n\n    Un-sized flexible data-type objects do not have this attribute.'
        pass
    
    @property
    def names(self):
        "Ordered list of field names, or ``None`` if there are no fields.\n\n    The names are ordered according to increasing byte offset. This can be\n    used, for example, to walk through all of the named fields in offset order.\n\n    Examples\n    --------\n    >>> dt = np.dtype([('name', np.str_, 16), ('grades', np.float64, (2,))])\n    >>> dt.names\n    ('name', 'grades')"
        pass
    
    @property
    def ndim(self):
        'Number of dimensions of the sub-array if this data type describes a\n    sub-array, and ``0`` otherwise.\n\n    .. versionadded:: 1.13.0'
        pass
    
    def newbyteorder(self, new_order='S'):
        "newbyteorder(new_order='S')\n\n    Return a new dtype with a different byte order.\n\n    Changes are also made in all fields and sub-arrays of the data type.\n\n    Parameters\n    ----------\n    new_order : string, optional\n        Byte order to force; a value from the byte order specifications\n        below.  The default value ('S') results in swapping the current\n        byte order.  `new_order` codes can be any of:\n\n        * 'S' - swap dtype from current to opposite endian\n        * {'<', 'L'} - little endian\n        * {'>', 'B'} - big endian\n        * {'=', 'N'} - native order\n        * {'|', 'I'} - ignore (no change to byte order)\n\n        The code does a case-insensitive check on the first letter of\n        `new_order` for these alternatives.  For example, any of '>'\n        or 'B' or 'b' or 'brian' are valid to specify big-endian.\n\n    Returns\n    -------\n    new_dtype : dtype\n        New dtype object with the given change to the byte order.\n\n    Notes\n    -----\n    Changes are also made in all fields and sub-arrays of the data type.\n\n    Examples\n    --------\n    >>> import sys\n    >>> sys_is_le = sys.byteorder == 'little'\n    >>> native_code = sys_is_le and '<' or '>'\n    >>> swapped_code = sys_is_le and '>' or '<'\n    >>> native_dt = np.dtype(native_code+'i2')\n    >>> swapped_dt = np.dtype(swapped_code+'i2')\n    >>> native_dt.newbyteorder('S') == swapped_dt\n    True\n    >>> native_dt.newbyteorder() == swapped_dt\n    True\n    >>> native_dt == swapped_dt.newbyteorder('S')\n    True\n    >>> native_dt == swapped_dt.newbyteorder('=')\n    True\n    >>> native_dt == swapped_dt.newbyteorder('N')\n    True\n    >>> native_dt == native_dt.newbyteorder('|')\n    True\n    >>> np.dtype('<i2') == native_dt.newbyteorder('<')\n    True\n    >>> np.dtype('<i2') == native_dt.newbyteorder('L')\n    True\n    >>> np.dtype('>i2') == native_dt.newbyteorder('>')\n    True\n    >>> np.dtype('>i2') == native_dt.newbyteorder('B')\n    True"
        pass
    
    @property
    def num(self):
        'A unique number for each of the 21 different built-in types.\n\n    These are roughly ordered from least-to-most precision.'
        pass
    
    @property
    def shape(self):
        'Shape tuple of the sub-array if this data type describes a sub-array,\n    and ``()`` otherwise.'
        pass
    
    @property
    def str(self):
        'The array-protocol typestring of this data-type object.'
        pass
    
    @property
    def subdtype(self):
        'Tuple ``(item_dtype, shape)`` if this `dtype` describes a sub-array, and\n    None otherwise.\n\n    The *shape* is the fixed shape of the sub-array described by this\n    data type, and *item_dtype* the data type of the array.\n\n    If a field whose dtype object has this attribute is retrieved,\n    then the extra dimensions implied by *shape* are tacked on to\n    the end of the retrieved array.'
        pass
    
    @property
    def type(self):
        'The type object used to instantiate a scalar of this data-type.'
        pass
    

class BestFirstTreeBuilder(TreeBuilder):
    'Build a decision tree in best-first fashion.\n\n    The best node to expand is given by the node at the frontier that has the\n    highest impurity improvement.\n    '
    __class__ = BestFirstTreeBuilder
    def __init__(self, *args, **kwargs):
        'Build a decision tree in best-first fashion.\n\n    The best node to expand is given by the node at the frontier that has the\n    highest impurity improvement.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def build(self):
        'Build a decision tree from the training set (X, y).'
        pass
    

DOUBLE = _mod_numpy.float64
DTYPE = _mod_numpy.float32
class DepthFirstTreeBuilder(TreeBuilder):
    'Build a decision tree in depth-first fashion.'
    __class__ = DepthFirstTreeBuilder
    def __init__(self, *args, **kwargs):
        'Build a decision tree in depth-first fashion.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def build(self):
        'Build a decision tree from the training set (X, y).'
        pass
    

NODE_DTYPE = dtype()
TREE_LEAF = -1
TREE_UNDEFINED = -2
class Tree(_mod_builtins.object):
    "Array-based representation of a binary decision tree.\n\n    The binary tree is represented as a number of parallel arrays. The i-th\n    element of each array holds information about the node `i`. Node 0 is the\n    tree's root. You can find a detailed description of all arrays in\n    `_tree.pxd`. NOTE: Some of the arrays only apply to either leaves or split\n    nodes, resp. In this case the values of nodes of the other type are\n    arbitrary!\n\n    Attributes\n    ----------\n    node_count : int\n        The number of nodes (internal nodes + leaves) in the tree.\n\n    capacity : int\n        The current capacity (i.e., size) of the arrays, which is at least as\n        great as `node_count`.\n\n    max_depth : int\n        The maximal depth of the tree.\n\n    children_left : array of int, shape [node_count]\n        children_left[i] holds the node id of the left child of node i.\n        For leaves, children_left[i] == TREE_LEAF. Otherwise,\n        children_left[i] > i. This child handles the case where\n        X[:, feature[i]] <= threshold[i].\n\n    children_right : array of int, shape [node_count]\n        children_right[i] holds the node id of the right child of node i.\n        For leaves, children_right[i] == TREE_LEAF. Otherwise,\n        children_right[i] > i. This child handles the case where\n        X[:, feature[i]] > threshold[i].\n\n    feature : array of int, shape [node_count]\n        feature[i] holds the feature to split on, for the internal node i.\n\n    threshold : array of double, shape [node_count]\n        threshold[i] holds the threshold for the internal node i.\n\n    value : array of double, shape [node_count, n_outputs, max_n_classes]\n        Contains the constant prediction value of each node.\n\n    impurity : array of double, shape [node_count]\n        impurity[i] holds the impurity (i.e., the value of the splitting\n        criterion) at node i.\n\n    n_node_samples : array of int, shape [node_count]\n        n_node_samples[i] holds the number of training samples reaching node i.\n\n    weighted_n_node_samples : array of int, shape [node_count]\n        weighted_n_node_samples[i] holds the weighted number of training samples\n        reaching node i.\n    "
    __class__ = Tree
    def __getstate__(self):
        'Getstate re-implementation, for pickling.'
        pass
    
    def __init__(self, *args, **kwargs):
        "Array-based representation of a binary decision tree.\n\n    The binary tree is represented as a number of parallel arrays. The i-th\n    element of each array holds information about the node `i`. Node 0 is the\n    tree's root. You can find a detailed description of all arrays in\n    `_tree.pxd`. NOTE: Some of the arrays only apply to either leaves or split\n    nodes, resp. In this case the values of nodes of the other type are\n    arbitrary!\n\n    Attributes\n    ----------\n    node_count : int\n        The number of nodes (internal nodes + leaves) in the tree.\n\n    capacity : int\n        The current capacity (i.e., size) of the arrays, which is at least as\n        great as `node_count`.\n\n    max_depth : int\n        The maximal depth of the tree.\n\n    children_left : array of int, shape [node_count]\n        children_left[i] holds the node id of the left child of node i.\n        For leaves, children_left[i] == TREE_LEAF. Otherwise,\n        children_left[i] > i. This child handles the case where\n        X[:, feature[i]] <= threshold[i].\n\n    children_right : array of int, shape [node_count]\n        children_right[i] holds the node id of the right child of node i.\n        For leaves, children_right[i] == TREE_LEAF. Otherwise,\n        children_right[i] > i. This child handles the case where\n        X[:, feature[i]] > threshold[i].\n\n    feature : array of int, shape [node_count]\n        feature[i] holds the feature to split on, for the internal node i.\n\n    threshold : array of double, shape [node_count]\n        threshold[i] holds the threshold for the internal node i.\n\n    value : array of double, shape [node_count, n_outputs, max_n_classes]\n        Contains the constant prediction value of each node.\n\n    impurity : array of double, shape [node_count]\n        impurity[i] holds the impurity (i.e., the value of the splitting\n        criterion) at node i.\n\n    n_node_samples : array of int, shape [node_count]\n        n_node_samples[i] holds the number of training samples reaching node i.\n\n    weighted_n_node_samples : array of int, shape [node_count]\n        weighted_n_node_samples[i] holds the weighted number of training samples\n        reaching node i.\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        'Reduce re-implementation, for pickling.'
        return ''; return ()
    
    def __setstate__(self, state):
        'Setstate re-implementation, for unpickling.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def apply(self):
        'Finds the terminal region (=leaf node) for each sample in X.'
        pass
    
    @property
    def capacity(self):
        pass
    
    @property
    def children_left(self):
        pass
    
    @property
    def children_right(self):
        pass
    
    def compute_feature_importances(self):
        'Computes the importance of each feature (aka variable).'
        pass
    
    def decision_path(self):
        'Finds the decision path (=node) for each sample in X.'
        pass
    
    @property
    def feature(self):
        pass
    
    @property
    def impurity(self):
        pass
    
    @property
    def max_depth(self):
        pass
    
    @property
    def max_n_classes(self):
        pass
    
    @property
    def n_classes(self):
        pass
    
    @property
    def n_features(self):
        pass
    
    @property
    def n_node_samples(self):
        pass
    
    @property
    def n_outputs(self):
        pass
    
    @property
    def node_count(self):
        pass
    
    def predict(self):
        'Predict target for X.'
        pass
    
    @property
    def threshold(self):
        pass
    
    @property
    def value(self):
        pass
    
    @property
    def weighted_n_node_samples(self):
        pass
    

class TreeBuilder(_mod_builtins.object):
    'Interface for different tree building strategies.'
    __class__ = TreeBuilder
    def __init__(self, *args, **kwargs):
        'Interface for different tree building strategies.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    def __setstate__(self, state):
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def build(self):
        'Build a decision tree from the training set (X, y).'
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/trevor/anaconda3/lib/python3.7/site-packages/sklearn/tree/_tree.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'sklearn.tree._tree'
__package__ = 'sklearn.tree'
def __pyx_unpickle_TreeBuilder():
    pass

__test__ = _mod_builtins.dict()
csc_matrix = _mod_scipy_sparse_csc.csc_matrix
csr_matrix = _mod_scipy_sparse_csr.csr_matrix
def issparse(x):
    'Is x of a sparse matrix type?\n\n    Parameters\n    ----------\n    x\n        object to check for being a sparse matrix\n\n    Returns\n    -------\n    bool\n        True if x is a sparse matrix, False otherwise\n\n    Notes\n    -----\n    issparse and isspmatrix are aliases for the same function.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix, isspmatrix\n    >>> isspmatrix(csr_matrix([[5]]))\n    True\n\n    >>> from scipy.sparse import isspmatrix\n    >>> isspmatrix(5)\n    False\n    '
    pass

