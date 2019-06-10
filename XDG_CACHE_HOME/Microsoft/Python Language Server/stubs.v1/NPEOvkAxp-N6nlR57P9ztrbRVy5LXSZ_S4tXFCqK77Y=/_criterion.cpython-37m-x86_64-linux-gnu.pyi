import builtins as _mod_builtins

class ClassificationCriterion(Criterion):
    'Abstract criterion for classification.'
    __class__ = ClassificationCriterion
    def __init__(self, *args, **kwargs):
        'Abstract criterion for classification.'
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
    

class Criterion(_mod_builtins.object):
    'Interface for impurity criteria.\n\n    This object stores methods on how to calculate how good a split is using\n    different metrics.\n    '
    __class__ = Criterion
    def __getstate__(self):
        pass
    
    def __init__(self, *args, **kwargs):
        'Interface for impurity criteria.\n\n    This object stores methods on how to calculate how good a split is using\n    different metrics.\n    '
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
    

class Entropy(ClassificationCriterion):
    'Cross Entropy impurity criterion.\n\n    This handles cases where the target is a classification taking values\n    0, 1, ... K-2, K-1. If node m represents a region Rm with Nm observations,\n    then let\n\n        count_k = 1 / Nm \\sum_{x_i in Rm} I(yi = k)\n\n    be the proportion of class k observations in node m.\n\n    The cross-entropy is then defined as\n\n        cross-entropy = -\\sum_{k=0}^{K-1} count_k log(count_k)\n    '
    __class__ = Entropy
    def __init__(self, *args, **kwargs):
        'Cross Entropy impurity criterion.\n\n    This handles cases where the target is a classification taking values\n    0, 1, ... K-2, K-1. If node m represents a region Rm with Nm observations,\n    then let\n\n        count_k = 1 / Nm \\sum_{x_i in Rm} I(yi = k)\n\n    be the proportion of class k observations in node m.\n\n    The cross-entropy is then defined as\n\n        cross-entropy = -\\sum_{k=0}^{K-1} count_k log(count_k)\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class FriedmanMSE(MSE):
    "Mean squared error impurity criterion with improvement score by Friedman\n\n    Uses the formula (35) in Friedman's original Gradient Boosting paper:\n\n        diff = mean_left - mean_right\n        improvement = n_left * n_right * diff^2 / (n_left + n_right)\n    "
    __class__ = FriedmanMSE
    def __init__(self, *args, **kwargs):
        "Mean squared error impurity criterion with improvement score by Friedman\n\n    Uses the formula (35) in Friedman's original Gradient Boosting paper:\n\n        diff = mean_left - mean_right\n        improvement = n_left * n_right * diff^2 / (n_left + n_right)\n    "
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class Gini(ClassificationCriterion):
    'Gini Index impurity criterion.\n\n    This handles cases where the target is a classification taking values\n    0, 1, ... K-2, K-1. If node m represents a region Rm with Nm observations,\n    then let\n\n        count_k = 1/ Nm \\sum_{x_i in Rm} I(yi = k)\n\n    be the proportion of class k observations in node m.\n\n    The Gini Index is then defined as:\n\n        index = \\sum_{k=0}^{K-1} count_k (1 - count_k)\n              = 1 - \\sum_{k=0}^{K-1} count_k ** 2\n    '
    __class__ = Gini
    def __init__(self, *args, **kwargs):
        'Gini Index impurity criterion.\n\n    This handles cases where the target is a classification taking values\n    0, 1, ... K-2, K-1. If node m represents a region Rm with Nm observations,\n    then let\n\n        count_k = 1/ Nm \\sum_{x_i in Rm} I(yi = k)\n\n    be the proportion of class k observations in node m.\n\n    The Gini Index is then defined as:\n\n        index = \\sum_{k=0}^{K-1} count_k (1 - count_k)\n              = 1 - \\sum_{k=0}^{K-1} count_k ** 2\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class MAE(RegressionCriterion):
    'Mean absolute error impurity criterion\n\n       MAE = (1 / n)*(\\sum_i |y_i - f_i|), where y_i is the true\n       value and f_i is the predicted value.'
    __class__ = MAE
    def __init__(self, *args, **kwargs):
        'Mean absolute error impurity criterion\n\n       MAE = (1 / n)*(\\sum_i |y_i - f_i|), where y_i is the true\n       value and f_i is the predicted value.'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class MSE(RegressionCriterion):
    'Mean squared error impurity criterion.\n\n        MSE = var_left + var_right\n    '
    __class__ = MSE
    def __init__(self, *args, **kwargs):
        'Mean squared error impurity criterion.\n\n        MSE = var_left + var_right\n    '
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __pyx_vtable__ = _mod_builtins.PyCapsule()
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

class RegressionCriterion(Criterion):
    'Abstract regression criterion.\n\n    This handles cases where the target is a continuous value, and is\n    evaluated by computing the variance of the target values left and right\n    of the split point. The computation takes linear time with `n_samples`\n    by using ::\n\n        var = \\sum_i^n (y_i - y_bar) ** 2\n            = (\\sum_i^n y_i ** 2) - n_samples * y_bar ** 2\n    '
    __class__ = RegressionCriterion
    def __init__(self, *args, **kwargs):
        'Abstract regression criterion.\n\n    This handles cases where the target is a continuous value, and is\n    evaluated by computing the variance of the target values left and right\n    of the split point. The computation takes linear time with `n_samples`\n    by using ::\n\n        var = \\sum_i^n (y_i - y_bar) ** 2\n            = (\\sum_i^n y_i ** 2) - n_samples * y_bar ** 2\n    '
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
    

__builtins__ = {}
__doc__ = None
__file__ = '/home/trevor/anaconda3/lib/python3.7/site-packages/sklearn/tree/_criterion.cpython-37m-x86_64-linux-gnu.so'
__name__ = 'sklearn.tree._criterion'
__package__ = 'sklearn.tree'
__test__ = _mod_builtins.dict()
