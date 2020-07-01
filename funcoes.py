from bs4 import BeautifulSoup
import requests

def gerardicascorona(resposta):
    page_link = 'https://www.google.com/search?sxsrf=ALeKk00eRLTp6FqN9HeearwFJUF3sKscvQ%3A1592662203906&ei=uxjuXtvfNoXI5OUP0aK-mAY&q=dica+corona&oq=dica+corona&gs_lcp=CgZwc3ktYWIQAzoFCAAQsQM6AggAOgQIIxAnOgQIABBDOgUIABCDAToHCAAQsQMQQzoGCAAQFhAeUMyWFViiohVgm6MVaABwAHgAgAGIAYgBnAmSAQMzLjiYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwibqaSHyZDqAhUFJLkGHVGRD2MQ4dUDCAw&uact=5'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    page_response = requests.get(page_link, timeout=5, headers=headers)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    resposta = page_content.find_all("div", class_="yccsuf")[0].text
    return resposta


def gerarsintomas(resposta):
    page_link = "https://www.google.com/search?sxsrf=ALeKk03oZ1CcPK1WjKD1f5iDww4co3XDtw%3A1592664029720&ei=3R_uXrrFK_3N5OUPpYqNyAk&q=sintomas+covid+19&oq=sintomas+covid+19&gs_lcp=CgZwc3ktYWIQAzIFCAAQsQMyBQgAEIMBMgIIADICCAAyAggAMgIIADICCAAyAggAMgUIABCDATICCAA6CggAELADEIMBEEM6CAgAELADEIMBOgUIABCwA1C2TFjiTmD5UGgBcAB4AIABa4gBrgKSAQMyLjGYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwj6p_Ptz5DqAhX9JrkGHSVFA5kQ4dUDCAw&uact=5"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    page_response = requests.get(page_link, timeout=5, headers=headers)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    resposta = page_content.find("div", class_="Z0mB9b").text
    return resposta


def gerarcasosbrasil(resposta):
    page_link = "https://news.google.com/covid19/map?hl=pt-BR&gl=BR&ceid=BR%3Apt-419&mid=%2Fm%2F015fr"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    page_response = requests.get(page_link, timeout=5, headers=headers)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    resposta = page_content.find_all("td", class_="l3HOY")[5].text
    return resposta

def gerarcasosmundo(resposta):
    page_link = "https://news.google.com/covid19/map?hl=pt-BR&gl=BR&ceid=BR%3Apt-419&mid=%2Fm%2F015fr"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    page_response = requests.get(page_link, timeout=5, headers=headers)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    resposta = page_content.find_all("td", class_="l3HOY")[0].text
    return resposta

def gerarmortes(resposta):
    page_link = "https://news.google.com/covid19/map?hl=pt-BR&gl=BR&ceid=BR%3Apt-419&mid=%2Fm%2F015fr"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    page_response = requests.get(page_link, timeout=5, headers=headers)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    resposta = page_content.find_all("div", class_="UvMayb")[2].text
    return resposta