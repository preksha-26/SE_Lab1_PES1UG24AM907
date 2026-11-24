from hypothesis import given, strategies as st
from course_registration_parser import format_course_code, total_credits, parse_student_record

inputs = st.one_of(st.text(), st.none(), st.integers(), st.booleans(),
                   st.lists(st.integers()), st.dictionaries(st.text(), st.integers()))


@given(inputs)
def test_format_course_code_no_crash(s):
    try:
        result = format_course_code(s)
    except Exception as exc:
        raise AssertionError(f"format_course_code crashed on {s!r}: {exc}") from exc
    assert result is None or isinstance(result, str)

@given(inputs)
def test_total_credits_no_crash(s):
    try:
        result = total_credits(s)
    except Exception as exc:
        raise AssertionError(f"total_credits crashed on {s!r}: {exc}") from exc
    assert result is None or (isinstance(result, int) and result >= 0)

@given(inputs)
def test_parse_student_record_no_crash(s):
    try:
        result = parse_student_record(s)
    except Exception as exc:
        raise AssertionError(f"parse_student_record crashed on {s!r}: {exc}") from exc
    assert result is None or (isinstance(result, dict) and
                              set(result) == {"srn", "name", "status"})
