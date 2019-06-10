import builtins as _mod_builtins
import scipy.sparse.csc as _mod_scipy_sparse_csc

class BaseDenseSplitter(Splitter):
    __class__ = BaseDenseSplitter
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce_cython__(self):
        pass
    
    def __setstate_cython__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class BaseSparseSplitter(Splitter):
    __class__ = BaseSparseSplitter
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce_cython__(self):
        pass
    
    def __setstate_cython__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class BestSparseSplitter(BaseSparseSplitter):
    'Splitter for finding the best split, using the sparse data.'
    __class__ = BestSparseSplitter
    def __init__(self, *args, **kwargs):
        'Splitter for finding the best split, using the sparse data.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class BestSplitter(BaseDenseSplitter):
    'Splitter for finding the best split.'
    __class__ = BestSplitter
    def __init__(self, *args, **kwargs):
        'Splitter for finding the best split.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class RandomSparseSplitter(BaseSparseSplitter):
    'Splitter for finding a random split, using the sparse data.'
    __class__ = RandomSparseSplitter
    def __init__(self, *args, **kwargs):
        'Splitter for finding a random split, using the sparse data.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class RandomSplitter(BaseDenseSplitter):
    'Splitter for finding the best random split.'
    __class__ = RandomSplitter
    def __init__(self, *args, **kwargs):
        'Splitter for finding the best random split.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce__(self):
        return ''; return ()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Splitter(_mod_builtins.object):
    'Abstract splitter class.\n\n    Splitters are called by tree builders to find the best splits on both\n    sparse and dense data, one split at a time.\n    '
    __class__ = Splitter
    def __getstate__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        'Abstract splitter class.\n\n    Splitters are called by tree builders to find the best splits on both\n    sparse and dense data, one split at a time.\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    def __reduce_cython__(self):
        pass
    
    def __setstate__(self, state):
        return None
    
    def __setstate_cython__(self):
        pass
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def criterion(self):
        pass
    
    @property
    def max_features(self):
        pass
    
    @property
    def min_samples_leaf(self):
        pass
    
    @property
    def min_weight_leaf(self):
        pass
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/trevor/anaconda3/lib/python3.7/site-packages/sklearn/tree/_splitter.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'sklearn.tree._splitter'
__package__ = 'sklearn.tree'
__test__ = _mod_builtins.dict()
csc_matrix = _mod_scipy_sparse_csc.csc_matrix
