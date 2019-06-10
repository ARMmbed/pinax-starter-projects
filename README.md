# {{ project_name }}

## Getting Started

Make sure you are using a virtual environment of some sort (e.g. `virtualenv` or
`pyenv`).

```
pip install nodeenv
nodeenv -p --prebuilt --node=10.16.0
npm install
pip install -r requirements.txt
./manage.py migrate
./manage.py loaddata sites
npm run dev
```

Browse to http://localhost:3000/


## Using Arm Microsoft Single Sign-on

[Python Social](http://python-social-auth-docs.readthedocs.io/en/latest/backends/azuread.html) is used to enable Arm SSO.

1. Create a new [Azure Active Directory App Registration](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps)
2. Copy the Application ID to `{{ project_name }}/settings.py`
```python
SOCIAL_AUTH_AZUREAD_OAUTH2_KEY = "application_id"
```
3. Create an API Access Key and copy it to `{{ project_name }}/settings.py`
```python
SOCIAL_AUTH_AZUREAD_OAUTH2_SECRET = "api_access_key"
```
4. Set your domain correctly in [Django Sites](https://docs.djangoproject.com/en/2.0/ref/contrib/sites/)
5. Set the Reply URL in the Azure settings to http://example.com/social-auth/complete/azuread-tenant-oauth2/ where example.com is your Django site domain.
6. Enable SSO by setting `ACCOUNT_LOGIN_METHOD` to "armsso" either in the environment or settings.py
