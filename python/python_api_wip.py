# -*- coding: utf-8 -*-

"""
Urban Rivals API - Python
This code is a Work In Progress
For more information on the API visit this site:
    https://www.urban-rivals.com/api/developer/


2020-08-20:
KS - Commiting this code to the repository, at this stage the code succesfully
receives an authorised token from UR, but i have not been able to construct
a valid call. 
"""

# oauth required for UR API
from requests_oauthlib import OAuth1Session
import ujson


# insert your personal client ID
client_id = ''
# insert your personal client secret
client_secret = ''

# change the redirect uri if you require, the urban rivals home page is the default
redirect_uri = 'https://www.urban-rivals.com'

# important urls
request_token_url = 'https://www.urban-rivals.com/api/auth/request_token.php'
authorisation_url = 'https://www.urban-rivals.com/api/auth/authorize.php'
access_token_url = 'http://www.urban-rivals.com/api/auth/access_token.php'
api_target = 'https://www.urban-rivals.com/api/'


# Obtain a request token which will identify you (the client) in the next step. 
# At this stage you will only need your client key and secret.
oauth = OAuth1Session(client_id, client_secret=client_secret)
fetch_response = oauth.fetch_request_token(request_token_url)

# example of fetch_response:
# {
#    "oauth_token": "Z6eEdO8MOmk394WozF5oKyuAv855l4Mlqo7hhlSLik",
#    "oauth_token_secret": "Kd75W4OQfb2oJTV0vzGzeXftVAwgMnEK9MumzYcM"
# }

resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')


# Obtain authorization from the resource owner to access the protected resources.
# This is commonly done by redirecting the user to a specific url to which you 
# add the request token as a query parameter. In this code you will need be the
# person to visit the aurthorisation url and authorise the request.
# Note that some services will give you a verifier at this stage. Urban Rivals
# does not do this which can cause issues at a later stage (further information
# provided at that point). Also the oauth_token given here will be the same as 
# the one in the previous step.
authorisation_url = oauth.authorization_url(authorisation_url)

print('Visit this Authorisation URL and authorise your account to be accessed ',
      authorisation_url)

# This is the point where the OAuth1Session should be initialised with a verifier.
# As previously mentioned, UR has not proivded one. This causes issues when
# trying to call fetch_access_token. To get around these errors, I edited the
# oauth1_session.py module. The edit I made was to comment out the error handling
# that occurs on lines 321 and 322. This allows the fetch_access_token function 
# to be called without throwing an error.
oauth = OAuth1Session(client_id, 
                      client_secret=client_secret,
                      resource_owner_key=resource_owner_key,
                      resource_owner_secret=resource_owner_secret)

# see above paragraph if this function is erroring. 
oauth_tokens = oauth.fetch_access_token(access_token_url)

resource_owner_key = oauth_tokens.get('oauth_token')
resource_owner_secret = oauth_tokens.get('oauth_token_secret')


# use authorised tokens to initialise a session with the api
oauth = OAuth1Session(client_id, 
                      client_secret=client_secret,
                      resource_owner_key=resource_owner_key,
                      resource_owner_secret=resource_owner_secret)


"""---------------------------------------------------------------------

This is as far as I have been able to make it before getting stuck. I have been
unable to correctly construct a call to be passed to the API. All attempts that
I have made to construct a call have resulted in 404 errors which UR defines as:
"non valid call (check your syntax)". 

The code inside this block comment is merely one version of the many variations 
I attempted. 

------------------------------------------------------------------------

call = {'call': 'characters.getCharacters',
        'params' : {'charactersIDs':300}}

json_call = ujson.encode(call)

r = oauth.request('get', url=api_target, params=json_call)

print(r.status_code, r.url, r.text)

----------------------------------------------------------------------"""