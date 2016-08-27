# -*- coding: utf-8 -*-
from pprint import pprint

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
import json
# Create your views here.
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
import requests

ACCESS_TOKEN = 'EAAZA7WeAG5PgBAHJUVeVYu82hJKwaSOZBWYLYVRYsKGmN3Up3Mj94sbOgIZCOChnjTF8vkvVP9LGreMHzer6HF0CYhzw30CWynKwDJnaDTvqEtovVJOj2rqRmzL5ikoFfVfS6gGktXzZBlkOMhrk1NH8FvZAMe8t3cl97uKCoZAgZDZD'


@method_decorator(csrf_exempt, name='dispatch')
class BotView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == 'botsoydigital':
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, Access Token is Invalid!')

    def post(self, request):
        data = json.loads(request.body)
        pprint(data)
        # return JsonResponse(data)
        sender = data['entry'][0]['messaging'][0]['sender']['id']
        message = data['entry'][0]['messaging'][0]['message']['text']
        reply(sender, message[::-1])
        return HttpResponse("oh")


class PrivacyView(generic.View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(
            """
            <b>Privacidad de los datos personales:</b>
<p>
            Sus datos personales le corresponden solo a usted y este sitio web es responsable de no revelar ninguna clase de información que le pertenezca (como email, números de ip, etc.), salvo su expresa autorización o fuerzas de naturaleza mayor de tipo legal que lo involucren, como hackeos o suplantaciones.
</p>
<b>
            Responsabilidad de las opiniones vertidas:
</b>
<p>
            Las publicaciones a modo de artículos (también llamados posts) son responsabilidad del autor del blog. Los comentarios, vertidos por los visitantes, son responsabilidad de ellos mismos y en caso alguno viole las reglas mínimas de respeto a los demás y a las buenas costumbres, éstos serían borrados por el editor del blog, sin esperar su consentimiento.
</p>
<b>
            Seguridad de su información personal:
</b>
<p>
            Este sitio web se hace responsable de velar por su seguridad, por la privacidad de su información y por el respeto a sus datos, de acuerdo con las limitaciones que la actual Internet nos provee, siendo conscientes que no estamos excluídos de sufrir algún ataque por parte de crackers o usuarios malintencionados que ejerzan la delincuencia informática.
</p>
<p>
            Obtención de su información:
</p>
<p>
            Todos sus datos personales consignados en este sitio son suministrados por usted mismo, haciendo uso entero de su libertad. La información aqui almacenada solo comprende datos básicos ingresados mediante formularios de contacto, comentarios u otros similares.
</p>
<p>
            Uso de la información:
</p>
<p>
            Al proporcionarnos sus datos personales, estando de acuerdo con la Política de Privacidad aquí consignada, nos autoriza para el siguiente uso de su información: a) para el fin mismo por lo cual se ha suministrado; b) para considerarlo dentro de nuestras estadísticas de tráfico, incrementando así nuestra oferta publicitaria y de mercado; c) para orientar mejor los servicios aquí ofrecidos y valorarlos a su criterio, y d) para enviar e-mails con nuestros boletines, responder inquietudes o comentarios, y mantener informado a nuestros usuarios.
</p>

            """
        )


def reply(user_id, msg):
    data = {
        "recipient": {"id": user_id},
        "message": {"text": msg}
    }
    resp = requests.post("https://graph.facebook.com/v2.6/me/messages?access_token=" + ACCESS_TOKEN, json=data)
    print(resp.content)
