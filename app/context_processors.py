from django.contrib.auth.models import User,Group

def users_context(request):
    user_data_list = []
    
    for user in User.objects.all():
        temp_groups_list = list()
        
        for group in user.groups.all():
            temp_groups_list.append(group.name)
        
        user_context = {
            'user' : user.username,
            'groups' : ''.join(temp_groups_list),
        }
        user_data_list.append(user_context)
    
    return {'user_data_list' : user_data_list}