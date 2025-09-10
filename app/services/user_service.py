from app.repositories import user_repository
import math

def find_user_by_id(user_id):
    users = user_repository.get_all_users()
    for user in users:
        if user['id'] == user_id:
            return user
    return None

def find_users(page, page_size, q, role, is_active):
    users = user_repository.get_all_users()

    if q:
        q_lower = q.lower()
        users = [
            user for user in users
            if q_lower in user['name'].lower() or q_lower in user['email'].lower()
        ]

    if role:
        users = [user for user in users if user['role'].lower() == role.lower()]

    if is_active is not None:
        is_active_bool = str(is_active).lower() == 'true'
        users = [user for user in users if user['is_active'] == is_active_bool]

    total_items = len(users)
    total_pages = math.ceil(total_items / page_size) if page_size > 0 else 0
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    paginated_users = users[start_index:end_index]

    return {
        "data": paginated_users,
        "pagination": {
            "page": page,
            "page_size": page_size,
            "total_items": total_items,
            "total_pages": total_pages,
        }
    }
