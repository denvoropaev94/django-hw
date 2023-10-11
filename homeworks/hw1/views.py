from django.shortcuts import render
from django.http import HttpResponse
import random
import logging


logger = logging.getLogger(__name__)


def index(request):
    index_html = """
    Real Madrid (Spanish: Real Madrid Club de Fútbolis
    a Spanish professional football club based in the city of Madrid. 
    Recognized by FIFA as the best football club of the 20th century.
    """
    logger.info('Index page accessed!')
    return HttpResponse(f'<h1>Real Madrid</h1><br><h2>{index_html}</h2>')


def about(request):
    html_h1 = """
    Real Madrid wrote a new chapter into the footballing history books
    when they got their hands on a 14th European Cup in 2022. 
    Our team extended their dominance of the competition with a win over Liverpool in Paris. 
    The early years of the decade also saw a 35th LaLiga title, 
    fifth European Super Cup, eighth Club World Cup, 20th Copa del Rey and a 12th Spanish Super Cup.
    """
    html_big = """
    Under Carlo Ancelotti’s guidance, Real Madrid clinched their 14th European Cup. 
    In the Italian coach’s second spell at the club, he lifted the continental trophy in 2022
    when his side overcame Liverpool in the final in Paris. 
    The trophy success capped a spectacular 2021/22 campaign, in which the side had first won
    its 12th Spanish Super Cup. This came in the tournament played in Saudi Arabia in January 2022. 
    First the Whites overcame Barcelona in the semi-finals after extra-time (2-3), 
    with Vini Jr., Benzema and Valverde on target, and the Uruguayan scoring the winning goal. 
    In the final, Madrid faced Athletic and the madridistas clinched the trophy
    courtesy of goals from Modrić and Benzema (0-2). And then came the club's 35th LaLiga title. 
    With four games still to play, the Whites clinched the title in front of their home fans
    with a 4-0 victory over Espanyol.The successes continued to come at the start of the 2022/23 campaign
    ,with the European Super Cup victory over Eintracht Frankfurt (2-0). 
    """
    logger.info('Access to the club page!')
    return HttpResponse(f'<h1>Some history</h1><br><h3>{html_h1}</h3><br><p>{html_big}</p>')
