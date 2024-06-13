from flask import Blueprint

from ..console.enterprise import oauth
from libs.external_api import ExternalApi
bp = Blueprint('enterprise', __name__, url_prefix='/enterprise_sso')
api = ExternalApi(bp)

#/enterprise/sso/oauth2/login

# Import auth controllers
from .auth import  data_source_oauth
