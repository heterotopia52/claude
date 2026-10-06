def get_user(users, name):
    for user in users:
        if user["name"] == name:
            return user

    return None


def process_users(users):
    result = []

    for user in users:
        if user["active"] == True:
            result.append(user)

    return result