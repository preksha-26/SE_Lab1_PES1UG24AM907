def format_course_code(code):
    """
    Formats 'cs 301' as 'CS301'.
    Return None for invalid input rather than raising an exception.
    """
    if not isinstance(code, str):
        return None
    parts = code.split()
    if len(parts) != 2:
        return None
    dept, number = parts
    if not dept.isascii() or not dept.isalpha() or not number.isascii() or not number.isdecimal():
        return None
    return dept.upper() + number

def total_credits(text):
    """
    Adds up comma-separated course credits.
    Return None if any credit is missing, negative or not a whole number.
    """
    if not isinstance(text, str):
        return None
    parts = [credit.strip() for credit in text.split(',')]
    if any(not credit.isdecimal() for credit in parts):
        return None
    try:
        return sum(int(credit) for credit in parts)
    except ValueError:
        # Python may reject extremely long integer strings.
        return None

def parse_student_record(line):
    """
    Parses 'SRN|name|status' into a dictionary.
    Return None unless exactly three nonempty fields are present.
    """
    if not isinstance(line, str):
        return None
    parts = [part.strip() for part in line.split('|')]
    if len(parts) != 3 or not all(parts):
        return None
    return {"srn": parts[0].strip().upper(),
            "name": parts[1].strip(),
            "status": parts[2].strip().lower()}

def main():
    print("==== Running format_course_code ====")
    value = input("Enter a course code as DEPT NUMBER (e.g. cs 301): ")
    print("Formatted course code:", format_course_code(value))

    print("\n==== Running total_credits ====")
    value = input("Enter course credits separated by commas (e.g. 4,3,4): ")
    print("Total credits:", total_credits(value))

    print("\n==== Running parse_student_record ====")
    value = input("Enter a student record as SRN|name|status (e.g. pes1ug23cs001|Asha|regular): ")
    print("Student record:", parse_student_record(value))

if __name__ == "__main__":
    main()
