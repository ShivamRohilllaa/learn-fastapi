from models import create_tables
from services import create_category, create_post, create_user, create_profile, get_post, get_user, update_post

create_tables()

# add_user_data = create_user('Shivam Rohilla', 'shivamnew@gmail.com')
# add_user_data = create_user('Shivam', 'shivam@gmail.com')
# add_profile_data = create_profile(1, 'im engineer', 'shivam rohilla')
# add_category = create_category('Mango')
# add_post = create_post('new post', 'hello content', 1)

# a=get_post(1)
# print(a)

a = update_post('new update title', 1)
print(a)
# u = get_user(1)
# print(u)