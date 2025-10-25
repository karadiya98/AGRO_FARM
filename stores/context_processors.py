# your_app/context_processors.py

def user_profile(request):
    profile_name = request.session.get('profile_name', None)
    otp = request.session.get('otp', None)
    email_for_otp= request.session.get('email_for_otp', None)
    
    return {'profile_name': profile_name, 'otp': otp ,'email_for_otp' :email_for_otp}
