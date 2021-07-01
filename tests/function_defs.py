import typing as ty

def nothing():
    # Check if no variables
    pass

def add(a, b):
    # Check variables
    return a + b

def add(a, b, c):
    # Check function with same name, happens with classes
    return a + b + c

def sub(a: int, b) -> int:
    # Check partially annotated
    return a - b

def mul(a: int, b:int):
    # No return
    return a * b

def div(a: int, b: int)-> float:
    # Fully annotated
    return a / b

def default_arg(a: int, b="test") ->None:
    # Default argument
    pass

def default_ann(a: int, b: str = "test")->None:
    # Default argument and annotation
    pass

def default_comment(a: int, b="#Comment") -> None:
    # Comment inside default argument
    pass

def default_comment2(a: int, b='#Comment') -> None:
    # Comment inside default argument
    pass

def default_comma(a: int, b="te,st") -> None:
    # Comma inside default argument
    pass

def multiline(
        a: int, b: str,
        c,
        d,
        e = list
) -> None:
    # Multiline definition
    pass

def multiline_comment(
        a: int, b, # Comment
        c: dict,   # Test
        d,         # Test 2
        e=list     # Test 3
):
    # Multiline definition with comments
    pass

def has_typing(path: str, a, options: ty.Dict[str, ty.Union[str, bool]], b, c: str):
    # Complex annotation
    pass

def multiline_type(
        path: str,
        options: ty.Dict[
            str, ty.Union[str, bool]
        ],
        a: int,
        b
):
    pass

def asterisks(
    a,
    b: int,
    *,
    c = 23,
):
    pass

def def_comment(a: int, b: str) -> int:
    # Function definition inside comment
    # def inside_comment(x): pass
    pass

def nested(a):
    def nested_2(b):
        pass

async def async_def():
    # Keyword before def
    # Only works with "async" as its the only
    # Valid word before 'def'
    # async def dont_match(): pass
    pass

def def_doc(a: int) -> int:
    """
    def def_doc_inside(a):
        pass
    """
    pass

def def_doc2(a: int) -> int:
    '''
    def def_doc_inside_2(a):
        pass
    '''
    pass

def def_doc3():
    """Text
    '''
    nested doc
    '''
    :return:
    Text"""

def comment_madness():
    "Normal string"
    # Nested # Comments # Another def f1(x): pass
    # Comma's inside comment def f2(x): pass
    # qoute "inside" comment def f3(x): pass
    # pass
    pass

class A:
    def __init__(self, a) -> None:
        pass

    def __new__(cls,
                *args, **kwargs):
        return False

    @classmethod
    def classmetho(cls, a) -> int:
        pass

    @staticmethod
    def static(a, b) -> int: pass

    #
    #

    async def class_async(self):
        pass


class B:
    def __init__(self, a: str):
        # No return annotation
        pass


def last():
    # Last function to check line numbers
    pass

if __name__ == "__main__":
    def inside_main():
        # Inside main
        pass

    def inside_main_last(): """last function for line numbers, check also if last line is a function def """