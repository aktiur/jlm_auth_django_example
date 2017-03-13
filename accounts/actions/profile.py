from __future__ import unicode_literals


def extract_profile(jlm_profile):
    location = jlm_profile.get('location', {})

    profile = {
        'email': jlm_profile['email'],
        'first_name': jlm_profile.get('first_name', ''),
        'last_name': jlm_profile.get('last_name', ''),
        'city': location.get('city', ''),
        'country_code': location.get('country_code')
    }

    return profile


def update_profile(user, profile):
    changed = False

    for prop, value in profile.items():
        if getattr(user, prop) != value:
            changed = True
            setattr(user, prop, value)

    if changed:
        user.save()
