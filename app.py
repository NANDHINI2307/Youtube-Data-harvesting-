import streamlit as st
import mysql.connector
from database.mysql import migrate_channel_data_to_mysql, search_data_in_mysql
from utils.youtube_api import get_youtube_channel_data

# Replace with your Google API key
google_api_key = "AIzaSyC4WCc-uKGrjVLWDQ5arWspLAN4havKRps"

def main():
    st.title("YouTube Channel Analysis App")

    # Navigation sidebar
    navigation = st.sidebar.selectbox("Navigation", ["Collect Data", "Migrate to MySQL", "Search MySQL Data"])
    
    if navigation == "Collect Data":
        st.header("Collect Data from YouTube Channels")

        # Input for YouTube Channel ID
        channel_id = st.text_input("Enter YouTube Channel ID")

        if st.button("Collect Data"):
            # Fetch YouTube data
            channel_data = get_youtube_channel_data(channel_id, google_api_key)
            
            # Store data in MySQL
            migrate_channel_data_to_mysql(channel_data)
            st.success(f"Data from {channel_data['channel_name']} stored in MySQL.")

    elif navigation == "Migrate to MySQL":
        st.header("Migrate Data to MySQL Database")

        # Select channel for migration
        selected_channel = st.selectbox("Select Channel for Migration", ["Channel 1", "Channel 2"])
        
        if st.button("Migrate Data"):
            # Migrate data to MySQL
            migrate_channel_data_to_mysql(selected_channel)
            st.success(f"Data from {selected_channel} migrated to MySQL database.")

    elif navigation == "Search MySQL Data":
        st.header("Search and Retrieve Data from MySQL Database")

        # Search options
        search_option = st.selectbox("Search Options", ["Search by Video Title", "Search by Likes"])

        if search_option == "Search by Video Title":
            title_query = st.text_input("Enter Video Title")
            result = search_data_in_mysql("video_title", title_query)
        else:
            likes_query = st.number_input("Minimum Likes")
            result = search_data_in_mysql("likes", likes_query)
        
        if st.button("Search"):
            if result:
                st.table(result)
            else:
                st.warning("No results found.")

if __name__ == "__main__":
    main()
