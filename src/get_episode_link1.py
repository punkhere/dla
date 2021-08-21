# Copyright © 2021 BaraniARR
# Encoding = 'utf-8'
# Licensed under MIT License
# Special Thanks for gogoanime

from pyrogram import *
from pyrogram.types import *
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from anikimiapi import AniKimi

# Initialize AniKimi class
anime = AniKimi(
    gogoanime_token="kggbp9liu7ij6sp0tcb9aspb75",
    auth_token="YvPqB3UXYkVOertRpe8y4nh47w4oWBG4oe6smLbN%2FFpAF7jgEM%2Fe8drDdm3evtuhotehb2H7x5CoFjYsDwa1Jg%3D%3D",
    host="https://gogoanime.pe/"  
)

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
    anime_link =  anime.get_episode_link(animeid= str_qry_final, episode_num= ep_num_link_get)
    # print(vidstream_link)
    try:
        dow_url1 = "hdp"
    except:
        pass
    try:
        dow_url2 = "360p"
    except:
        pass
    try:
        dow_url3 = "480p"
    except:
        pass
    try:
        dow_url4 = "720p"
    except:
        pass
    try:
        dow_url5 = "1080p"
    except:
        pass
    try:
        dow_url6 = "streamsb"
    except:
        pass
    try:
        dow_url7 = "xstreamcdn"
    except:
        pass
	try:
		dow_url8 = "streamtape"
		pass
	try:
		dow_url9 = "mixdrop"
		pass
	try:
		dow_url10 = "mp4upload"
		pass
	try:
		dow_url11 = "doodstream"
		pass

    try:
        downlink1 = anime_link.link_hdp
    except:
        pass
    try:
        downlink2 = anime_link.link_360p
    except:
        pass
    try:
        downlink3 = anime_link.link_480p
    except:
        pass
    try:
        downlink4 = anime_link.link_720p
    except:
        pass
    try:
        downlink5 = anime_link.link_1080p
    except:
        pass
    try:
        downlink6 = anime_link.link_streamsb
    except:
        pass
    try:
        downlink7 = anime_link.link_xstreamcdn
    except:
        pass
	try:
		downlink8 = anime_link.link_streamtape
		pass
    try:
		downlink9 = anime_link.link_mixdrop
		pass
	try:
		downlink10 = anime_link.link_mp4upload
		pass
	try:
		downlink11 = anime_link.link_doodstream
		pass
    try:
        str1 = dow_url1.string
        str_spl1 = str1.split()
        str_spl1.remove(str_spl1[0])
        str_original_1 = ""
        quality_name1 = str_original_1.join(str_spl1)
    except:
        pass
    
    try:
        str2 = dow_url2.string
        str_spl2 = str2.split()
        str_spl2.remove(str_spl2[0])
        str_original_2 = ""
        quality_name2 = str_original_2.join(str_spl2)
    except:
        pass
    
    try:
        str3 = dow_url3.string
        str_spl3 = str3.split()
        str_spl3.remove(str_spl3[0])
        str_original_3 = ""
        quality_name3 = str_original_3.join(str_spl3)
    except:
        pass
    
    try:
        str4 = dow_url4.string
        str_spl4 = str4.split()
        str_spl4.remove(str_spl4[0])
        str_original_4 = ""
        quality_name4 = str_original_4.join(str_spl4)
    except:
        pass

    try:
        str5 = dow_url5.string
        str_spl5 = str5.split()
        str_spl5.remove(str_spl5[0])
        str_original_5 = ""
        quality_name5 = str_original_5.join(str_spl5)
    except:
        pass
    
    try:
        str6 = dow_url6.string
        str_spl6 = str6.split()
        str_spl6.remove(str_spl6[0])
        str_original_6 = ""
        quality_name6 = str_original_6.join(str_spl6)
    except:
        pass

    try:
        str7 = dow_url7.string
        str_spl7 = str7.split()
        str_spl7.remove(str_spl7[0])
        str_original_7 = ""
        quality_name7 = str_original_7.join(str_spl7)
    except:
        pass
    try:
        str8 = dow_url8.string
        str_spl8 = str8.split()
        str_spl8.remove(str_spl8[0])
        str_original_8 = ""
        quality_name8 = str_original_8.join(str_spl8)
    except:
        pass
	try:
        str9 = dow_url9.string
        str_spl9 = str9.split()
        str_spl9.remove(str_spl9[0])
        str_original_9 = ""
        quality_name9 = str_original_9.join(str_spl9)
    except:
        pass
	try:
        str10 = dow_ur10.string
        str_spl10 = str10.split()
        str_spl10.remove(str_spl10[0])
        str_original_10 = ""
        quality_name10 = str_original_10.join(str_spl10)
    except:
        pass
	try:
        str11 = dow_url11.string
        str_spl11 = str11.split()
        str_spl11.remove(str_spl11[0])
        str_original_11 = ""
        quality_name11 = str_original_11.join(str_spl11)
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
	 res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name8}','lnk':f'{downlink8}'})
    except:
        pass
	 res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name9}','lnk':f'{downlink9}'})
    except:
        pass
     res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name10}','lnk':f'{downlink10}'})
    except:
        pass
	 res_list.append({'num':f'{ep_num_link_get}','qual':f'{quality_name11}','lnk':f'{downlink11}'})
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
