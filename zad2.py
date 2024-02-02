def check_permissions(required_permission):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Tutaj można umieścić kod do sprawdzania uprawnień użytkownika
            user_permissions = ["admin"]  # tutaj przykładowa lista uprawnień użytkownika

            if required_permission in user_permissions:
                return func(*args, **kwargs)
            else:
                print(f"Error: Permission denied! Required permission: {required_permission}")

        return wrapper

    return decorator

@check_permissions("admin")
def delete_file(file_name):
    # a tu symulacja usuwania pliku...
    print(f"Deleting file: {file_name}")

delete_file("important_document.txt")  # Output: Error: Permission denied! Required permission: admin