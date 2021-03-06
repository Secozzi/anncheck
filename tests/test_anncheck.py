from anncheck import _get_file_info
import re

TEST_PATH = "/function_defs.py"
OPTIONS = {
    'include_asterisk': False,
    'compact': False,
    'include_docstrings': False,
    'exclude_return': False,
    'exclude_main': False,
    'padding': 3,
    'exclude_dunder': False,
    'new_line': False,
    'recursive': False,
    'init_return': False,
    'match_function': None,
    'match_variable': None
}


ansi_escape = re.compile(r"""
    \x1B  # ESC
    (?:   # 7-bit C1 Fe (except CSI)
        [@-Z\\-_]
    |     # or [ for CSI, followed by a control sequence
        \[
        [0-?]*  # Parameter bytes
        [ -/]*  # Intermediate bytes
        [@-~]   # Final byte
    )
""", re.VERBOSE)


def test_anncheck():
    result = _get_file_info(TEST_PATH, **OPTIONS)
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        "  3:Function nothing is missing a return annotation.",
        "  7:Function add is missing annotations for argument a.",
        "  7:Function add is missing annotations for argument b.",
        "  7:Function add is missing a return annotation.",
        " 11:Function add is missing annotations for argument a.",
        " 11:Function add is missing annotations for argument b.",
        " 11:Function add is missing annotations for argument c.",
        " 11:Function add is missing a return annotation.",
        " 15:Function sub is missing annotations for argument b.",
        " 19:Function mul is missing a return annotation.",
        " 27:Function default_arg is missing annotations for argument b.",
        " 35:Function default_comment is missing annotations for argument b.",
        " 39:Function default_comment2 is missing annotations for argument b.",
        " 43:Function default_comma is missing annotations for argument b.",
        " 47:Function space_after is missing annotations for argument a.",
        " 47:Function space_after is missing annotations for argument b.",
        " 47:Function space_after is missing a return annotation.",
        " 50:Function multiline is missing annotations for argument c.",
        " 50:Function multiline is missing annotations for argument d.",
        " 50:Function multiline is missing annotations for argument e.",
        " 59:Function multiline_comment is missing annotations for argument b.",
        " 59:Function multiline_comment is missing annotations for argument d.",
        " 59:Function multiline_comment is missing annotations for argument e.",
        " 59:Function multiline_comment is missing a return annotation.",
        " 68:Function has_typing is missing annotations for argument a.",
        " 68:Function has_typing is missing annotations for argument b.",
        " 68:Function has_typing is missing a return annotation.",
        " 72:Function multiline_type is missing annotations for argument b.",
        " 72:Function multiline_type is missing a return annotation.",
        " 82:Function asterisks is missing annotations for argument a.",
        " 82:Function asterisks is missing annotations for argument c.",
        " 82:Function asterisks is missing a return annotation.",
        " 95:Function nested is missing annotations for argument a.",
        " 95:Function nested is missing a return annotation.",
        " 96:Function nested_2 is missing annotations for argument b.",
        " 96:Function nested_2 is missing a return annotation.",
        " 99:Function async_def is missing a return annotation.",
        "120:Function def_doc3 is missing a return annotation.",
        "128:Function comment_madness is missing a return annotation.",
        "137:Function __init__ is missing annotations for argument a.",
        "140:Function __new__ is missing a return annotation.",
        "145:Function classmethod is missing annotations for argument a.",
        "149:Function static is missing annotations for argument a.",
        "149:Function static is missing annotations for argument b.",
        "151:Function class_async is missing a return annotation.",
        "161:Function last is missing a return annotation.",
        "166:Function inside_main is missing a return annotation.",
        "170:Function inside_main_last is missing a return annotation."
    ]
    assert result == expected


def test_asterisk():
    result = _get_file_info(TEST_PATH, **{**OPTIONS, 'include_asterisk': True})
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        "  3:Function nothing is missing a return annotation.",
        "  7:Function add is missing annotations for argument a.",
        "  7:Function add is missing annotations for argument b.",
        "  7:Function add is missing a return annotation.",
        " 11:Function add is missing annotations for argument a.",
        " 11:Function add is missing annotations for argument b.",
        " 11:Function add is missing annotations for argument c.",
        " 11:Function add is missing a return annotation.",
        " 15:Function sub is missing annotations for argument b.",
        " 19:Function mul is missing a return annotation.",
        " 27:Function default_arg is missing annotations for argument b.",
        " 35:Function default_comment is missing annotations for argument b.",
        " 39:Function default_comment2 is missing annotations for argument b.",
        " 43:Function default_comma is missing annotations for argument b.",
        " 47:Function space_after is missing annotations for argument a.",
        " 47:Function space_after is missing annotations for argument b.",
        " 47:Function space_after is missing a return annotation.",
        " 50:Function multiline is missing annotations for argument c.",
        " 50:Function multiline is missing annotations for argument d.",
        " 50:Function multiline is missing annotations for argument e.",
        " 59:Function multiline_comment is missing annotations for argument b.",
        " 59:Function multiline_comment is missing annotations for argument d.",
        " 59:Function multiline_comment is missing annotations for argument e.",
        " 59:Function multiline_comment is missing a return annotation.",
        " 68:Function has_typing is missing annotations for argument a.",
        " 68:Function has_typing is missing annotations for argument b.",
        " 68:Function has_typing is missing a return annotation.",
        " 72:Function multiline_type is missing annotations for argument b.",
        " 72:Function multiline_type is missing a return annotation.",
        " 82:Function asterisks is missing annotations for argument a.",
        " 82:Function asterisks is missing annotations for argument *.",
        " 82:Function asterisks is missing annotations for argument c.",
        " 82:Function asterisks is missing a return annotation.",
        " 95:Function nested is missing annotations for argument a.",
        " 95:Function nested is missing a return annotation.",
        " 96:Function nested_2 is missing annotations for argument b.",
        " 96:Function nested_2 is missing a return annotation.",
        " 99:Function async_def is missing a return annotation.",
        "120:Function def_doc3 is missing a return annotation.",
        "128:Function comment_madness is missing a return annotation.",
        "137:Function __init__ is missing annotations for argument a.",
        "140:Function __new__ is missing annotations for argument *args.",
        "140:Function __new__ is missing annotations for argument **kwargs.",
        "140:Function __new__ is missing a return annotation.",
        "145:Function classmethod is missing annotations for argument a.",
        "149:Function static is missing annotations for argument a.",
        "149:Function static is missing annotations for argument b.",
        "151:Function class_async is missing a return annotation.",
        "161:Function last is missing a return annotation.",
        "166:Function inside_main is missing a return annotation.",
        "170:Function inside_main_last is missing a return annotation."
    ]
    assert result == expected


def test_include_docstring():
    result = _get_file_info(TEST_PATH, **{**OPTIONS, 'include_docstrings': True})
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        "  3:Function nothing is missing a return annotation.",
        "  7:Function add is missing annotations for argument a.",
        "  7:Function add is missing annotations for argument b.",
        "  7:Function add is missing a return annotation.",
        " 11:Function add is missing annotations for argument a.",
        " 11:Function add is missing annotations for argument b.",
        " 11:Function add is missing annotations for argument c.",
        " 11:Function add is missing a return annotation.",
        " 15:Function sub is missing annotations for argument b.",
        " 19:Function mul is missing a return annotation.",
        " 27:Function default_arg is missing annotations for argument b.",
        " 35:Function default_comment is missing annotations for argument b.",
        " 39:Function default_comment2 is missing annotations for argument b.",
        " 43:Function default_comma is missing annotations for argument b.",
        " 47:Function space_after is missing annotations for argument a.",
        " 47:Function space_after is missing annotations for argument b.",
        " 47:Function space_after is missing a return annotation.",
        " 50:Function multiline is missing annotations for argument c.",
        " 50:Function multiline is missing annotations for argument d.",
        " 50:Function multiline is missing annotations for argument e.",
        " 59:Function multiline_comment is missing annotations for argument b.",
        " 59:Function multiline_comment is missing annotations for argument d.",
        " 59:Function multiline_comment is missing annotations for argument e.",
        " 59:Function multiline_comment is missing a return annotation.",
        " 68:Function has_typing is missing annotations for argument a.",
        " 68:Function has_typing is missing annotations for argument b.",
        " 68:Function has_typing is missing a return annotation.",
        " 72:Function multiline_type is missing annotations for argument b.",
        " 72:Function multiline_type is missing a return annotation.",
        " 82:Function asterisks is missing annotations for argument a.",
        " 82:Function asterisks is missing annotations for argument c.",
        " 82:Function asterisks is missing a return annotation.",
        " 95:Function nested is missing annotations for argument a.",
        " 95:Function nested is missing a return annotation.",
        " 96:Function nested_2 is missing annotations for argument b.",
        " 96:Function nested_2 is missing a return annotation.",
        " 99:Function async_def is missing a return annotation.",
        "108:Function def_doc_inside is missing annotations for argument a.",
        "108:Function def_doc_inside is missing a return annotation.",
        "115:Function def_doc_inside_2 is missing annotations for argument a.",
        "115:Function def_doc_inside_2 is missing a return annotation.",
        "120:Function def_doc3 is missing a return annotation.",
        "128:Function comment_madness is missing a return annotation.",
        "137:Function __init__ is missing annotations for argument a.",
        "140:Function __new__ is missing a return annotation.",
        "145:Function classmethod is missing annotations for argument a.",
        "149:Function static is missing annotations for argument a.",
        "149:Function static is missing annotations for argument b.",
        "151:Function class_async is missing a return annotation.",
        "161:Function last is missing a return annotation.",
        "166:Function inside_main is missing a return annotation.",
        "170:Function inside_main_last is missing a return annotation."
    ]

    assert result == expected


def test_exclude_return():
    result = _get_file_info(TEST_PATH, **{**OPTIONS, 'exclude_return': True})
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        "  7:Function add is missing annotations for argument a.",
        "  7:Function add is missing annotations for argument b.",
        " 11:Function add is missing annotations for argument a.",
        " 11:Function add is missing annotations for argument b.",
        " 11:Function add is missing annotations for argument c.",
        " 15:Function sub is missing annotations for argument b.",
        " 27:Function default_arg is missing annotations for argument b.",
        " 35:Function default_comment is missing annotations for argument b.",
        " 39:Function default_comment2 is missing annotations for argument b.",
        " 43:Function default_comma is missing annotations for argument b.",
        " 47:Function space_after is missing annotations for argument a.",
        " 47:Function space_after is missing annotations for argument b.",
        " 50:Function multiline is missing annotations for argument c.",
        " 50:Function multiline is missing annotations for argument d.",
        " 50:Function multiline is missing annotations for argument e.",
        " 59:Function multiline_comment is missing annotations for argument b.",
        " 59:Function multiline_comment is missing annotations for argument d.",
        " 59:Function multiline_comment is missing annotations for argument e.",
        " 68:Function has_typing is missing annotations for argument a.",
        " 68:Function has_typing is missing annotations for argument b.",
        " 72:Function multiline_type is missing annotations for argument b.",
        " 82:Function asterisks is missing annotations for argument a.",
        " 82:Function asterisks is missing annotations for argument c.",
        " 95:Function nested is missing annotations for argument a.",
        " 96:Function nested_2 is missing annotations for argument b.",
        "137:Function __init__ is missing annotations for argument a.",
        "145:Function classmethod is missing annotations for argument a.",
        "149:Function static is missing annotations for argument a.",
        "149:Function static is missing annotations for argument b."
    ]

    assert result == expected


def test_exclude_main():
    result = _get_file_info(TEST_PATH, **{**OPTIONS, 'exclude_main': True})
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        "  3:Function nothing is missing a return annotation.",
        "  7:Function add is missing annotations for argument a.",
        "  7:Function add is missing annotations for argument b.",
        "  7:Function add is missing a return annotation.",
        " 11:Function add is missing annotations for argument a.",
        " 11:Function add is missing annotations for argument b.",
        " 11:Function add is missing annotations for argument c.",
        " 11:Function add is missing a return annotation.",
        " 15:Function sub is missing annotations for argument b.",
        " 19:Function mul is missing a return annotation.",
        " 27:Function default_arg is missing annotations for argument b.",
        " 35:Function default_comment is missing annotations for argument b.",
        " 39:Function default_comment2 is missing annotations for argument b.",
        " 43:Function default_comma is missing annotations for argument b.",
        " 47:Function space_after is missing annotations for argument a.",
        " 47:Function space_after is missing annotations for argument b.",
        " 47:Function space_after is missing a return annotation.",
        " 50:Function multiline is missing annotations for argument c.",
        " 50:Function multiline is missing annotations for argument d.",
        " 50:Function multiline is missing annotations for argument e.",
        " 59:Function multiline_comment is missing annotations for argument b.",
        " 59:Function multiline_comment is missing annotations for argument d.",
        " 59:Function multiline_comment is missing annotations for argument e.",
        " 59:Function multiline_comment is missing a return annotation.",
        " 68:Function has_typing is missing annotations for argument a.",
        " 68:Function has_typing is missing annotations for argument b.",
        " 68:Function has_typing is missing a return annotation.",
        " 72:Function multiline_type is missing annotations for argument b.",
        " 72:Function multiline_type is missing a return annotation.",
        " 82:Function asterisks is missing annotations for argument a.",
        " 82:Function asterisks is missing annotations for argument c.",
        " 82:Function asterisks is missing a return annotation.",
        " 95:Function nested is missing annotations for argument a.",
        " 95:Function nested is missing a return annotation.",
        " 96:Function nested_2 is missing annotations for argument b.",
        " 96:Function nested_2 is missing a return annotation.",
        " 99:Function async_def is missing a return annotation.",
        "120:Function def_doc3 is missing a return annotation.",
        "128:Function comment_madness is missing a return annotation.",
        "137:Function __init__ is missing annotations for argument a.",
        "140:Function __new__ is missing a return annotation.",
        "145:Function classmethod is missing annotations for argument a.",
        "149:Function static is missing annotations for argument a.",
        "149:Function static is missing annotations for argument b.",
        "151:Function class_async is missing a return annotation.",
        "161:Function last is missing a return annotation."
    ]

    assert result == expected


def test_include_init_return():
    result = _get_file_info(TEST_PATH, **{**OPTIONS, 'init_return': True})
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        "  3:Function nothing is missing a return annotation.",
        "  7:Function add is missing annotations for argument a.",
        "  7:Function add is missing annotations for argument b.",
        "  7:Function add is missing a return annotation.",
        " 11:Function add is missing annotations for argument a.",
        " 11:Function add is missing annotations for argument b.",
        " 11:Function add is missing annotations for argument c.",
        " 11:Function add is missing a return annotation.",
        " 15:Function sub is missing annotations for argument b.",
        " 19:Function mul is missing a return annotation.",
        " 27:Function default_arg is missing annotations for argument b.",
        " 35:Function default_comment is missing annotations for argument b.",
        " 39:Function default_comment2 is missing annotations for argument b.",
        " 43:Function default_comma is missing annotations for argument b.",
        " 47:Function space_after is missing annotations for argument a.",
        " 47:Function space_after is missing annotations for argument b.",
        " 47:Function space_after is missing a return annotation.",
        " 50:Function multiline is missing annotations for argument c.",
        " 50:Function multiline is missing annotations for argument d.",
        " 50:Function multiline is missing annotations for argument e.",
        " 59:Function multiline_comment is missing annotations for argument b.",
        " 59:Function multiline_comment is missing annotations for argument d.",
        " 59:Function multiline_comment is missing annotations for argument e.",
        " 59:Function multiline_comment is missing a return annotation.",
        " 68:Function has_typing is missing annotations for argument a.",
        " 68:Function has_typing is missing annotations for argument b.",
        " 68:Function has_typing is missing a return annotation.",
        " 72:Function multiline_type is missing annotations for argument b.",
        " 72:Function multiline_type is missing a return annotation.",
        " 82:Function asterisks is missing annotations for argument a.",
        " 82:Function asterisks is missing annotations for argument c.",
        " 82:Function asterisks is missing a return annotation.",
        " 95:Function nested is missing annotations for argument a.",
        " 95:Function nested is missing a return annotation.",
        " 96:Function nested_2 is missing annotations for argument b.",
        " 96:Function nested_2 is missing a return annotation.",
        " 99:Function async_def is missing a return annotation.",
        "120:Function def_doc3 is missing a return annotation.",
        "128:Function comment_madness is missing a return annotation.",
        "137:Function __init__ is missing annotations for argument a.",
        "140:Function __new__ is missing a return annotation.",
        "145:Function classmethod is missing annotations for argument a.",
        "149:Function static is missing annotations for argument a.",
        "149:Function static is missing annotations for argument b.",
        "151:Function class_async is missing a return annotation.",
        "156:Function __init__ is missing a return annotation.",
        "161:Function last is missing a return annotation.",
        "166:Function inside_main is missing a return annotation.",
        "170:Function inside_main_last is missing a return annotation."
    ]

    assert result == expected


def test_match_function():
    result = _get_file_info(TEST_PATH, **{**OPTIONS, 'match_function': "^m"})
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        " 19:Function mul is missing a return annotation.",
        " 50:Function multiline is missing annotations for argument c.",
        " 50:Function multiline is missing annotations for argument d.",
        " 50:Function multiline is missing annotations for argument e.",
        " 59:Function multiline_comment is missing annotations for argument b.",
        " 59:Function multiline_comment is missing annotations for argument d.",
        " 59:Function multiline_comment is missing annotations for argument e.",
        " 59:Function multiline_comment is missing a return annotation.",
        " 72:Function multiline_type is missing annotations for argument b.",
        " 72:Function multiline_type is missing a return annotation."
    ]

    assert result == expected


def test_match_variable():
    result = _get_file_info(TEST_PATH, **{**OPTIONS, 'match_variable': "[a-zA-Z]{2,}"})
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        "  3:Function nothing is missing a return annotation.",
        "  7:Function add is missing a return annotation.",
        " 11:Function add is missing a return annotation.",
        " 19:Function mul is missing a return annotation.",
        " 47:Function space_after is missing a return annotation.",
        " 59:Function multiline_comment is missing a return annotation.",
        " 68:Function has_typing is missing a return annotation.",
        " 72:Function multiline_type is missing a return annotation.",
        " 82:Function asterisks is missing a return annotation.",
        " 95:Function nested is missing a return annotation.",
        " 96:Function nested_2 is missing a return annotation.",
        " 99:Function async_def is missing a return annotation.",
        "120:Function def_doc3 is missing a return annotation.",
        "128:Function comment_madness is missing a return annotation.",
        "140:Function __new__ is missing a return annotation.",
        "151:Function class_async is missing a return annotation.",
        "161:Function last is missing a return annotation.",
        "166:Function inside_main is missing a return annotation.",
        "170:Function inside_main_last is missing a return annotation."
    ]

    assert result == expected


def test_padding():
    result = _get_file_info(TEST_PATH, **{**OPTIONS, 'padding': 5})
    result = list(map(lambda x: ansi_escape.sub("", x), result))
    expected = [
        "    3:Function nothing is missing a return annotation.",
        "    7:Function add is missing annotations for argument a.",
        "    7:Function add is missing annotations for argument b.",
        "    7:Function add is missing a return annotation.",
        "   11:Function add is missing annotations for argument a.",
        "   11:Function add is missing annotations for argument b.",
        "   11:Function add is missing annotations for argument c.",
        "   11:Function add is missing a return annotation.",
        "   15:Function sub is missing annotations for argument b.",
        "   19:Function mul is missing a return annotation.",
        "   27:Function default_arg is missing annotations for argument b.",
        "   35:Function default_comment is missing annotations for argument b.",
        "   39:Function default_comment2 is missing annotations for argument b.",
        "   43:Function default_comma is missing annotations for argument b.",
        "   47:Function space_after is missing annotations for argument a.",
        "   47:Function space_after is missing annotations for argument b.",
        "   47:Function space_after is missing a return annotation.",
        "   50:Function multiline is missing annotations for argument c.",
        "   50:Function multiline is missing annotations for argument d.",
        "   50:Function multiline is missing annotations for argument e.",
        "   59:Function multiline_comment is missing annotations for argument b.",
        "   59:Function multiline_comment is missing annotations for argument d.",
        "   59:Function multiline_comment is missing annotations for argument e.",
        "   59:Function multiline_comment is missing a return annotation.",
        "   68:Function has_typing is missing annotations for argument a.",
        "   68:Function has_typing is missing annotations for argument b.",
        "   68:Function has_typing is missing a return annotation.",
        "   72:Function multiline_type is missing annotations for argument b.",
        "   72:Function multiline_type is missing a return annotation.",
        "   82:Function asterisks is missing annotations for argument a.",
        "   82:Function asterisks is missing annotations for argument c.",
        "   82:Function asterisks is missing a return annotation.",
        "   95:Function nested is missing annotations for argument a.",
        "   95:Function nested is missing a return annotation.",
        "   96:Function nested_2 is missing annotations for argument b.",
        "   96:Function nested_2 is missing a return annotation.",
        "   99:Function async_def is missing a return annotation.",
        "  120:Function def_doc3 is missing a return annotation.",
        "  128:Function comment_madness is missing a return annotation.",
        "  137:Function __init__ is missing annotations for argument a.",
        "  140:Function __new__ is missing a return annotation.",
        "  145:Function classmethod is missing annotations for argument a.",
        "  149:Function static is missing annotations for argument a.",
        "  149:Function static is missing annotations for argument b.",
        "  151:Function class_async is missing a return annotation.",
        "  161:Function last is missing a return annotation.",
        "  166:Function inside_main is missing a return annotation.",
        "  170:Function inside_main_last is missing a return annotation."
    ]

    assert result == expected
