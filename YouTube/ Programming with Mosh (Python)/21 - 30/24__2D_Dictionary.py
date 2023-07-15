# Nested dictionary example
student_records = {
    'John': {
        'age': 20,
        'major': 'Computer Science',
        'grades': {
            'Math': 90,
            'English': 85,
            'History': 78
        }
    },
    'Alice': {
        'age': 22,
        'major': 'Physics',
        'grades': {
            'Math': 95,
            'English': 92,
            'Physics': 88
        }
    }
}

# Accessing nested dictionary values
print("John's major:", student_records['John']['major'])
print("John's Math grade:", student_records['John']['grades']['Math'])
print("Alice's age:", student_records['Alice']['age'])
print("Alice's Physics grade:", student_records['Alice']['grades']['Physics'])
