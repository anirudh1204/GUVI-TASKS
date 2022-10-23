# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:21:43 2022

@author: Nikhitha
"""

import pandas as pd
import os
import snscrape.modules.twitter as sntwitter
import streamlit as st
sod=["Scraping","Download data"]
options=["Username","Keyword"]
st.set_page_config(page_title="APP")
st.header("WELCOME TO TWITTER SCRAPER")
st.subheader("What would you like to do:")
choice=st.sidebar.selectbox("SELECT:",sod)
tweets_list1 = []
tweets_list2 = []
if choice=="Scraping":
    c1=st.selectbox("Search by:",options)
    if c1=="Username":
        username=st.text_input("Give username:")
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:'+username).get_items()):
            if i>10:
                break
            tweets_list1.append([tweet.date, tweet.id, tweet.content,tweet.username,tweet.url])
        tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text',"Username",'URL'])
        st.dataframe(tweets_df1)
    elif c1=="Keyword":
        keyword=st.text_input("Enter keyword:")
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('{}'.format(keyword) +'since:2022-10-10 until:2022-10-15').get_items()):
            if i>10:
                break
            tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
        tweets_df1 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
        st.dataframe(tweets_df1)
elif choice=="Download data:":
    c2=st.selectbox("Search by:",options)
    if c2=="Username":
        username=st.text_input("Give username:")
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:username').get_items()):
            if i>10:
                break
            tweets_list2.append([tweet.date, tweet.id, tweet.content,tweet.username,tweet.url,username])
            tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text',"Username",'URL'])
            st.dataframe(tweets_df2)
    elif c2=="Keyword":
        keyword=st.text_input("Enter keyword:")
        for i,tweet in enumerate(sntwitter.TwitterSearchScraper('keyword since:2021-01-01 until:2021-05-31').get_items()):
            if i>10:
                break
            tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
            tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
            st.dataframe(tweets_df2)
        



