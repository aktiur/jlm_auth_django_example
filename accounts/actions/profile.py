from __future__ import unicode_literals


def extract_profile(jlm_profile):
    location = jlm_profile.get('location', {})

    try:
        profile = {
            'email': jlm_profile['email'],
            'first_name': jlm_profile.get('first_name') or '',
            'last_name': jlm_profile.get('last_name') or '',
            'city': location.get('city') or '',
            'country_code': location.get('country_code') or ''
        }

        return profile
    except KeyError:
        raise ValueError('The profile was not of the correct format')

def update_profile(user, profile):
    changed = False

    for prop, value in profile.items():
        if getattr(user, prop) != value:
            changed = True
            setattr(user, prop, value)

    if changed:
        user.save()
