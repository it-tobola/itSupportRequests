import pandas as pd
import streamlit as st
import backend as b


# Set initial page configurations
st.set_page_config(page_title="TOBOLA IT Support Tickets", layout='wide')

st.header("IT Support Ticket Form")

with st.form("IT Support Tickets"):

    with st.container():
        d_type = st.selectbox("Select Device Type", options=b.devices['Device Type'].unique())
        sub1 = st.form_submit_button("Select Device Type")
    with st.container():
        device = st.selectbox("Select Device", options=b.devices['Device Label'][b.devices['Device Type']==d_type],
                              key='device')
        request_info = st.text_area("Request Information", key='request')
    with st.container():
        submitter = st.selectbox("Person Submitting this Request", options=b.ee['Full Name'], key='requestor')
        confirmation = st.checkbox("By checking this box, I am confirming that the information above is correct to "
                                   "the best of my knowledge")
        sub2 = st.form_submit_button("Submit Request")

    if confirmation and sub2:
        submission = pd.DataFrame()
        submission['Linked Device'] = [st.session_state['device']]
        submission['Request'] = [st.session_state['request']]
        submission['Requestor'] = [st.session_state['requestor']]

        try:
            submission.to_notion(b.tickets_url, api_key=b.notion_token, title='Test', resolve_relation_values=True)
            with st.sidebar:
                st.success('Request Submitted!', icon="✅")
                st.write("You can now close this screen")
        except:
            st.warning('Please try again', icon="⚠️")

    elif (confirmation == False) and sub2:
        st.warning('Please confirm the checkbox to continue', icon="⚠️")
