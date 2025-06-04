# your_app/context_processors.py

def user_profile(request):
    profile_name = request.session.get('profile_name', None)
    return {'profile_name': profile_name}
