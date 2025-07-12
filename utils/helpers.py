def get_user_by_skill(skill_query, users):
    return [user for user in users if skill_query.lower() in user.skills_offered.lower()]