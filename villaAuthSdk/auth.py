# AUTOGENERATED! DO NOT EDIT! File to edit: authSdk.ipynb (unless otherwise specified).

__all__ = ['AuthSdk', 'auth', 'createUser']

# Cell
from nicHelper.wrappers import add_method
from lambdasdk.lambdasdk import Lambda
from awsSchema.apigateway import Event, Response
from nicHelper.dictUtil import printDict
from nicHelper.exception import errorString

# Cell
class AuthSdk:
  def __init__(
    self,
    user = None,
    pw = None,
    region = 'ap-southeast-1'
    ):
    self.lambda_ = Lambda(user = user, pw = pw, region = region)

  def generalInvoke(self, body={}, functionName= ''):
    event = Event.getInput(body=body)
    response = self.lambda_.invoke(functionName=functionName, input=event)
    try: return Response.parseBody(response)
    except: return errorString()


# Cell
@add_method(AuthSdk)
def auth(self,user,pw,functionName= 'villaAuth-Auth-13UCAIBB6FOHA'):
  return self.generalInvoke(body={'user':user,'password':pw},functionName=functionName)

# Cell
@add_method(AuthSdk)
def createUser(self,functionName='villaAuth-CreateUser-ECLM1M2B9LPJ', **kwargs):
  return self.generalInvoke(body=kwargs,functionName=functionName)