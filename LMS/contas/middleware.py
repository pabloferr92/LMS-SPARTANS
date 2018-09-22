from core.models.sessao import Sessao
from core.loginHelper import LoginHelper

class SpartansMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.startswith("/static/"):
            if "SPARTANSSESSION" in request.COOKIES:
                try:
                    sessao = Sessao.objects.get(id=request.COOKIES["SPARTANSSESSION"])
                    sessao.usuario = LoginHelper().pegarUsuarioPelaSessao(sessao)
                    request.sessao = sessao
                except:
                    print("nao encontrou a sessao no banco");
                    return self.get_response(request)
        return self.get_response(request)
