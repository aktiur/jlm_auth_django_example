# jlm_auth_django_example

Ce  projet Django démontre comment intégrer l'authentification JLM2017 à votre application.
Il a été principalement testé avec Python 3, mais devrait fonctioner sous Python 2.7.

L'authentification, via OAuth2, vous permet notamment de récupérer le profil de l'utilisateur tel
qu'il a été rempli sur le site jlm2017.fr.

Vous pouvez copier telle quelle l'application accounts
à votre propre projet Django, ainsi que les paramètres nécessaires (dans le fichier settings.py),
et l'authentification sera directement disponible dans votre propre projet.

Si vous souhaitez effectivement intégrer l'authentication à votre projet, vous devez rentrer en contact
avec l'équipe jlm2017.fr pour obtenir vos identifiants client sur le [chat coders JLM2017](https://chat.coders.jlm2017.fr/).

## Tester cette application

Pour tester cette application, suivez les étapes suivantes :

1. Clonez ce dépôt
2. Créez un virtual env et installez les prérequis décrits dans le fichier ``requirements.txt``
3. Appliquez les migrations pour créer la base de données de test (``python manage.py migrate``)
4. Lancez le serveur de test (``python manage.py runserver``)
5. Rendez vous sur <http://localhost:8000>
