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
    do = r['Referer']
    dow = do.replace('streaming.php', 'download')
    ur = f"https://animeapi-demo.herokuapp.com/gogoanime/watch/{str_qry_final}-episode-{ep_num_link_get}"
    r = requests.get(ur).json()
    k = []

    for links in r:
        {k.append(dow),
        k.append(r['sources'][0]['file']),
        k.append(f"http://simple-anime.herokuapp.com/videos/{str_qry_final}-episode-{ep_num_link_get}")
        }
    
    
    try:
        dow_url1 = "streaming link 1"
    except:
        pass
    try:
        dow_url2 = "streaming link 2"
    except:
        pass
    try:
        dow_url3 = "streaming link 3"
    except:
        pass

    try:
        downlink1 = k[0]
    except:
        pass
    try:
        downlink2 = k[1]
    except:
        pass
    try:
        downlink3 = k[2]
    except:
        pass
    
    
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
