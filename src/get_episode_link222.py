# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# gets lists of Episdoes link when episode number and anime id is passed as callback_data

def get_ep_link(client, callback_query):
    query = callback_query
    data = query.data
    query.answer(f"Please wait till I fetch Links...")
    data_spl_ep = data.split("_")
    ep_num_link_get = int(data_spl_ep[1])
    data_spl_ep.remove(data_spl_ep[0])
    data_spl_ep.remove(data_spl_ep[0])
    str_qry = ""
    str_qry_final = str_qry.join(data_spl_ep)
    # print(str_qry_final)
    animelink = f'https://gogoanime.ai/category/{str_qry_final}'
    response = requests.get(animelink)
    plainText = response.text
    soup = BeautifulSoup(plainText, "lxml")
    lnk = soup.find(id="episode_page")
    source_url = lnk.find("li").a
    tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
    # print(tit_url)
    ep_num_tot = source_url.get("ep_end")
    last_ep = int(ep_num_tot)
    # print(last_ep)
    # print(ep_num_link_get)
    episode = ep_num_link_get
    # print("Generating Links from", start, "to", end)
    animename = animelink.split("/")
    ur = f'https://xapi-v1.herokuapp.com/anime/{str_qry_final}/ep/{ep_num_link_get}?direct_link=false'
    ud = f'https://xapi-v1.herokuapp.com/anime/{str_qry_final}/ep/{ep_num_link_get}?direct_link=true'
    r = requests.get(ur).json()
    rd = requests.get(ud).json()
    k = []
    do = []
    for key in r:
    	k.append(key)
    for dol in rd:
    	do.append(dol)
    
    try:
        dow_url1 = k[0]
    except:
        pass
    try:
        dow_url2 = k[1]
    except:
        pass
    try:
        dow_url3 = k[2]
    except:
        pass
    try:
        dow_url4 = k[3]
    except:
        pass
    try:
        dow_url5 = k[4]
    except:
        pass
    try:
        dow_url6 = k[5]
    except:
        pass
    try:
        dow_url7 = k[6]
    except:
        pass
    try:
     	di_url1 = ("Download Link 1: "+do[0])
    except:
     	pass
    try:
    	di_url2 = ("Download Link 2: "+do[1])
    except:
    	pass

    try:
        downlink1 = r.get(dow_url1)
    except:
        pass
    try:
        downlink2 = r.get(dow_url2)
    except:
        pass
    try:
        downlink3 = r.get(dow_url3)
    except:
        pass
    try:
        downlink4 = r.get(dow_url4)
    except:
        pass
    try:
        downlink5 = r.get(dow_url5)
    except:
        pass
    try:
        downlink6 = r.get(dow_url6)
    except:
        pass
    try:
        downlink7 = r.get(dow_url7)
    except:
        pass
    try:
    	dir1 = rd.get(do[0])
    except:
    	pass
    try:
    	dir2 = rd.get(do[1])
    
    try:
        quality_name1 = dow_url1
    except:
        pass
    
    try:
        quality_name2 = dow_url2
    except:
        pass
    
    try:
        quality_name3 = dow_url3
    except:
        pass
    
    try:
        quality_name4 = dow_url4
    except:
        pass

    try:
        quality_name5 = dow_url5
    except:
        pass
    
    try:
        quality_name6 = dow_url6
    except:
        pass

    try:
        quality_name7 = dow_url7
    except:
        pass
    try:
    	quality_name8 = di_url1
    except:
    	pass
    try:
    	quality_name9 = di_url2
    except:
    	pass
    
    res_list = []
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name1}','lnk':f'{downlink1}'})
    except:
        pass
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name2}','lnk':f'{downlink2}'})
    except:
        pass
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name3}','lnk':f'{downlink3}'})
    except:
        pass
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name4}','lnk':f'{downlink4}'})
    except:
        pass
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name5}','lnk':f'{downlink5}'})
    except:
        pass
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name6}','lnk':f'{downlink6}'})
    except:
        pass
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name7}','lnk':f'{downlink7}'})
    except:
        pass
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name8}','lnk':f'{dir1}'})
    except:
        pass
    try:
        res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name9}','lnk':f'{dir2}'})
    except:
        pass
    
    
    if ep_num_link_get == last_ep:
        key = []
        for links in res_list:
            ep_number = links.get('num')
            quality = links.get('qual')
            download_links = links.get('lnk')
            key.append((InlineKeyboardButton(f"Ep{ep_number} {quality}", url=f"{download_links}")))
        n = 3
        keys = [key[i:i + n] for i in range(0, len(key), n)]
        keys.append([(InlineKeyboardButton("⏪ Previous Ep", callback_data=f"eps_{ep_num_link_get - 1}_{str_qry_final}")),
                    (InlineKeyboardButton("↔️Back to list↔️", callback_data=f"dl_{str_qry_final}"))])
        reply_markup = InlineKeyboardMarkup(keys)
        query.edit_message_text(text=f"""You are now watching **Episode {ep_num_link_get}** of **{tit_url}** :-

Please share the bot if you like it ☺️.

__Note: Select HDP link for faster streaming.__

**This the Last Episode of the Series 🥳🥳🥳**""", reply_markup=reply_markup, parse_mode="markdown")
    elif ep_num_link_get == 1:
        key = []
        for links in res_list:
            ep_number = links.get('num')
            quality = links.get('qual')
            download_links = links.get('lnk')
            key.append((InlineKeyboardButton(f"Ep{ep_number} {quality}", url=f"{download_links}")))
        n = 3
        keys = [key[i:i + n] for i in range(0, len(key), n)]
        keys.append([(InlineKeyboardButton("↔️Back To list↔️", callback_data=f"dl_{str_qry_final}")),
             (InlineKeyboardButton("Next Ep ⏩", callback_data=f"eps_{ep_num_link_get + 1}_{str_qry_final}"))])
        reply_markup = InlineKeyboardMarkup(keys)
        query.edit_message_text(text=f"""You are now watching **Episode {ep_num_link_get}** of **{tit_url}** :-

Please share the bot if you like it ☺️.

__Note: Select HDP link for faster streaming.__""", reply_markup=reply_markup, parse_mode="markdown")
    else:
        key = []
        for links in res_list:
            ep_number = links.get('num')
            quality = links.get('qual')
            download_links = links.get('lnk')
            key.append((InlineKeyboardButton(f"Ep{ep_number} {quality}", url=f"{download_links}")))
        n = 3
        keys = [key[i:i + n] for i in range(0, len(key), n)]
        keys.append([(InlineKeyboardButton("⏪ Previous Ep", callback_data=f"eps_{ep_num_link_get - 1}_{str_qry_final}")),
             (InlineKeyboardButton("↔️Back To list↔️", callback_data=f"dl_{str_qry_final}")),
             (InlineKeyboardButton("Next Ep ⏩", callback_data=f"eps_{ep_num_link_get + 1}_{str_qry_final}"))])
        reply_markup = InlineKeyboardMarkup(keys)
        query.edit_message_text(text=f"""You are now watching **Episode {ep_num_link_get}** of **{tit_url}** :-

Please share the bot if you like it ☺️.

__Note: Select HDP link for faster streaming.__""", reply_markup=reply_markup, parse_mode="markdown")
